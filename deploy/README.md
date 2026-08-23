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

## 3. Set your API keys and run parameters

```bash
ssh root@<droplet-ip>
nano /etc/eval-harness.env
```

Fill in `OPENROUTER_API_KEY`, `ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, and edit
`RUN_ARGS` to the actual batch you want — e.g. to scale past the 10-article
smoke test once you've picked a model:

```
RUN_ARGS=--models qwen/qwen3-30b-a3b --judges opus gpt --run-id do-batch-1
```

`RUN_ARGS` is exactly what you'd otherwise type after
`python3 scripts/eval_harness.py run` locally — same flags
(`--models`, `--articles`, `--limit`, `--judges`, `--overwrite`, etc.), see
[eval/README.md](../eval/README.md).

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

## 5. Pull results back to your laptop

From your Mac, in the repo root:

```bash
deploy/sync_results.sh <droplet-ip>
python3 scripts/eval_harness.py report --run-id do-batch-1
```

This only copies `eval/runs/` (the cached JSON results) — it doesn't touch
anything else on the droplet, so you can run it as often as you like while
the batch is still going, to check progress without waiting for it to finish.

## 6. Tear down when you're done

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
  droplet, mode `600`, readable by root; `deploy/eval-harness.env.example` in
  git is a template with empty values.
- **If it crashes:** `Restart=on-failure` in the systemd unit retries after
  60s. Cached results make retries free — check `journalctl -u eval-harness`
  for the actual error if it keeps failing (e.g. a bad model slug, an
  exhausted API key).
