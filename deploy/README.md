# Running the eval harness on a DigitalOcean droplet

`scripts/eval_harness.py` just makes HTTP calls to OpenRouter/Anthropic/OpenAI
and waits — no GPU, no local model weights. For a run spanning a couple of
days, the goal is reliability (survives SSH disconnects, reboots, and crashes)
more than horsepower, so the cheapest droplet size is the right choice.

I can't create the droplet myself — I have no DigitalOcean credentials or API
access from here — so this is a prepared setup you run. Everything below is
copy-paste.

## 1. Create the droplet

**Web console:** New Droplet → Ubuntu 24.04 (LTS) x64 → **Basic, $6/mo (1 vCPU / 1GB)**
is plenty (pure network I/O + light PDF text extraction) → any region → add
your SSH key → Create.

**Or with `doctl`** (if you have the CLI installed and authenticated):
```bash
doctl compute ssh-key list                     # find your key's ID/fingerprint
doctl compute droplet create eval-harness \
    --region nyc3 \
    --image ubuntu-24-04-x64 \
    --size s-1vcpu-1gb \
    --ssh-keys <your-ssh-key-id> \
    --wait
doctl compute droplet get eval-harness --format PublicIPv4 --no-header
```

Note the droplet's IP address — you'll use it for every step below.

## 2. Bootstrap it

The provisioning script lives in this repo, which isn't on the droplet yet —
copy just that one file up first:

```bash
scp deploy/provision.sh root@<droplet-ip>:/root/provision.sh
ssh root@<droplet-ip> bash /root/provision.sh
```

It installs Python/git, creates a dedicated non-root `evalrunner` user, and
generates an SSH deploy key. It'll stop and print a public key — **add that as
a read-only Deploy Key** on the GitHub repo (Settings → Deploy keys → Add
deploy key; leave "Allow write access" unchecked), then re-run the same
command to finish: clone the repo, create a venv, install
`requirements-eval.txt`, and install the systemd unit.

(If the repo is actually public, you can skip the deploy-key dance and just
change `REPO_URL` in `provision.sh` to the HTTPS clone URL before copying it up.)

`provision.sh` defaults to cloning this feature branch
(`claude/research-scraper-test-setup-i4bh9m`) since that's where this tooling
currently lives. Once it's merged to `main`, either edit `BRANCH` in the
script or pass it as an env var: `BRANCH=main bash /root/provision.sh`.

## 3. Set your API keys, and which models to run

Two separate files, deliberately — one holds secrets and is never in git,
the other holds run parameters (which models/articles/judges) and *is*
tracked in git, since "try a new model" shouldn't require opening a file
with your API keys in it.

```bash
ssh root@<droplet-ip>
nano /etc/eval-harness.env
```
Fill in `OPENROUTER_API_KEY`, `ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, and
`EVAL_HARNESS_CONTACT_EMAIL` (a real address — NCBI's usage guidelines
specifically ask for this so they can warn you before blocking your IP; see
[eval/SOURCES.md](../eval/SOURCES.md)). You only need to touch this file
again if a key changes.

```bash
nano /opt/learning-wiki/deploy/run-config.env
```
This is where `RUN_ARGS` lives — exactly what you'd otherwise type after
`python3 scripts/eval_harness.py run` locally (same flags: `--models`,
`--articles`, `--limit`, `--judges`, `--overwrite`, etc., see
[eval/README.md](../eval/README.md)). Since it's a normal repo file, the
usual way to change it going forward is: edit it (or have it edited for you),
`git commit` + push, then on the droplet `git pull` and
`sudo systemctl restart eval-harness` — already-completed pairs are cached
and won't be redone. A quick one-off change works too: edit it directly on
the droplet and restart, same as any config file — it just won't be in git
history unless you also commit it from wherever you edited it.

## 4. Start it and confirm it's running

```bash
sudo systemctl enable --now eval-harness
journalctl -u eval-harness -f
```

`enable` means it also resumes automatically if the droplet reboots (e.g. for
an unattended kernel update) — since every (model, article) pair is cached to
disk as it completes, a restart just skips finished work and picks up where
it left off, so this is safe to leave for days unattended. `Ctrl-C` only stops
following the log, not the service.

Check status any time with `systemctl status eval-harness`, or stop it with
`sudo systemctl stop eval-harness`.

**One-time, only if this droplet was provisioned before the live-dashboard
feature existed:** confirm the dashboard web server is installed and running —
`provision.sh` now sets this up automatically on a fresh droplet, but an
already-provisioned one needs it added once:
```bash
ssh root@<droplet-ip> 'cd /opt/learning-wiki && sudo -u evalrunner git pull origin claude/research-scraper-test-setup-i4bh9m && cp deploy/eval-harness-web.service /etc/systemd/system/ && systemctl daemon-reload && systemctl enable --now eval-harness-web'
```

## 5. Watch it live

From your Mac, in the repo root:

```bash
deploy/live_view.sh <droplet-ip> do-batch-1
```

This opens an SSH tunnel to the droplet's dashboard server and launches
`report.html` in your browser. The dashboard **regenerates after every
completed article/model pair** and **auto-refreshes every 20 seconds**
(preserving whichever tab and expanded row you had open), so it reads as a
live view of the batch rather than something you need to manually refresh.
Leave the terminal tab running; `Ctrl-C` closes the tunnel (safe to reopen
anytime — nothing on the droplet depends on it staying open).

**Fallback (a static one-off snapshot instead of the live view):**
```bash
deploy/sync_results.sh <droplet-ip>
python3 scripts/eval_harness.py report --run-id do-batch-1
open eval/runs/do-batch-1/report.html
```

## 6. Self-driving prompt search (optional)

Once you have a baseline run you're not happy with, `auto-optimize` (see
[eval/README.md](../eval/README.md)) can search for a better prompt
unattended — several diverse candidate revisions per round, run in
parallel, best one kept — and write a final recommendation summary for you
to read whenever you check back:

```bash
nano deploy/auto-optimize-config.env    # set --baseline-run to a real run-id, tune search params
git add deploy/auto-optimize-config.env && git commit -m "..." && git push
```
```bash
ssh root@<droplet-ip>
cd /opt/learning-wiki && sudo -u evalrunner git pull
sudo systemctl start eval-auto-optimize
journalctl -u eval-auto-optimize -f
```

Unlike `eval-harness`, this unit is **not** `enable`d at boot and has **no**
`Restart=` — it's a bounded, one-off search you trigger by hand each time,
not an always-on service; nothing relaunches it after it finishes or fails.
Read the final result any time (during or after the run) at
`eval/runs/auto-optimize-summary-<baseline-run>.md`, or browse individual
candidates' dashboards the same way as any other run through
`live_view.sh`.

**Or skip the SSH round-trip entirely** — the landing page
(`http://localhost:8080/`) has a **"Launch N more rounds"** button that
starts a search directly from the browser. It continues from wherever the
last search left off (tracked in `eval/runs/.auto_optimize_state.json`),
falling back to whatever `--baseline-run` is configured in
`auto-optimize-config.env` if nothing has run yet — so the config file is
still where you set the starting point and tune candidates/concurrency/
judges, but you don't need to re-SSH in just to launch another batch of
rounds once it's running. This only works because `eval-harness-web` runs
a small custom server (`deploy/dashboard_server.py`) instead of Python's
plain `http.server` — **if this droplet was provisioned before this
feature existed**, update it once:
```bash
ssh root@<droplet-ip>
cd /opt/learning-wiki && sudo -u evalrunner git pull
sudo cp deploy/eval-harness-web.service /etc/systemd/system/
sudo systemctl daemon-reload && sudo systemctl restart eval-harness-web
```

## 7. Tear down when you're done

The droplet has no reason to exist once the batch is done and synced —
stop paying for it:

```bash
doctl compute droplet delete eval-harness
# or: Web console -> Droplets -> eval-harness -> Destroy
```

## Notes

- **Cost:** a $6/mo droplet prorates to about $0.20/day — a couple of days
  costs pennies. The real cost of a multi-day run is the OpenRouter/judge API
  spend, which is identical whether it runs on the droplet or your laptop.
- **Secrets never touch the repo:** `/etc/eval-harness.env` lives only on the
  droplet, mode `640` owned by `root:evalrunner` (group-readable by the
  service user so ad-hoc commands like `status`/`optimize` can load it too,
  still unreadable by anyone else); `deploy/eval-harness.env.example` in git
  is a template with empty values.
- **If it crashes:** `Restart=on-failure` in the systemd unit retries after
  60s. Cached results make retries free — check `journalctl -u eval-harness`
  for the actual error if it keeps failing (e.g. a bad model slug, an
  exhausted API key).
