#!/usr/bin/env bash
# provision.sh — one-time bootstrap for a fresh Ubuntu 24.04 DigitalOcean droplet.
#
# This script isn't in the repo yet when you first SSH in (chicken-and-egg), so
# copy it up before the repo is cloned:
#   scp deploy/provision.sh root@<droplet-ip>:/root/provision.sh
#   ssh root@<droplet-ip> bash /root/provision.sh
#
# Safe to re-run — it skips steps that already succeeded. It will stop once and
# ask you to add a deploy key to GitHub; re-run it after that to finish.
set -euo pipefail

APP_USER="evalrunner"
APP_DIR="/opt/learning-wiki"
REPO_URL="git@github.com:Learning-Design-Alliance/learning-wiki.git"
BRANCH="${BRANCH:-claude/research-scraper-test-setup-i4bh9m}"

if [ "$(id -u)" -ne 0 ]; then
  echo "Run as root (or with sudo)." >&2
  exit 1
fi

echo "== 1. System packages =="
apt-get update -y
apt-get install -y python3 python3-venv python3-pip git rsync

echo "== 2. Dedicated non-root user =="
if ! id -u "$APP_USER" >/dev/null 2>&1; then
  useradd --system --create-home --shell /usr/sbin/nologin "$APP_USER"
fi

echo "== 3. Deploy key for git =="
DEPLOY_KEY="/home/$APP_USER/.ssh/id_ed25519"
if [ ! -f "$DEPLOY_KEY" ]; then
  sudo -u "$APP_USER" mkdir -p "/home/$APP_USER/.ssh"
  sudo -u "$APP_USER" ssh-keygen -t ed25519 -N "" -f "$DEPLOY_KEY" -C "eval-harness-droplet"
  sudo -u "$APP_USER" ssh-keyscan -H github.com >> "/home/$APP_USER/.ssh/known_hosts" 2>/dev/null
  echo
  echo "=== Add this public key as a READ-ONLY Deploy Key on the GitHub repo, then re-run this script ==="
  echo "    GitHub repo -> Settings -> Deploy keys -> Add deploy key (leave 'Allow write access' unchecked)"
  echo
  cat "$DEPLOY_KEY.pub"
  echo
  exit 0
fi

echo "== 4. Clone or update repo =="
mkdir -p "$APP_DIR"
chown "$APP_USER:$APP_USER" "$APP_DIR"

export GIT_SSH_COMMAND="ssh -i $DEPLOY_KEY -o IdentitiesOnly=yes"
if [ ! -d "$APP_DIR/.git" ]; then
  sudo -u "$APP_USER" env GIT_SSH_COMMAND="$GIT_SSH_COMMAND" git clone --branch "$BRANCH" "$REPO_URL" "$APP_DIR"
else
  sudo -u "$APP_USER" env GIT_SSH_COMMAND="$GIT_SSH_COMMAND" git -C "$APP_DIR" fetch origin "$BRANCH"
  sudo -u "$APP_USER" git -C "$APP_DIR" checkout "$BRANCH"
  sudo -u "$APP_USER" env GIT_SSH_COMMAND="$GIT_SSH_COMMAND" git -C "$APP_DIR" pull origin "$BRANCH"
fi

echo "== 5. Python virtualenv + deps =="
sudo -u "$APP_USER" python3 -m venv "$APP_DIR/venv"
sudo -u "$APP_USER" "$APP_DIR/venv/bin/pip" install --upgrade pip --quiet
sudo -u "$APP_USER" "$APP_DIR/venv/bin/pip" install -r "$APP_DIR/requirements-eval.txt" --quiet

echo "== 6. Secrets file (created once, never overwritten by re-runs) =="
ENV_FILE="/etc/eval-harness.env"
if [ ! -f "$ENV_FILE" ]; then
  cp "$APP_DIR/deploy/eval-harness.env.example" "$ENV_FILE"
  chmod 600 "$ENV_FILE"
  echo "Created $ENV_FILE — edit it with real API keys and your contact email."
fi
# Which models to run lives in deploy/run-config.env instead (tracked in git,
# not a secret) — already up to date from the clone/pull above.

echo "== 7. systemd units =="
cp "$APP_DIR/deploy/eval-harness.service" /etc/systemd/system/eval-harness.service
cp "$APP_DIR/deploy/eval-harness-web.service" /etc/systemd/system/eval-harness-web.service
chmod +x "$APP_DIR/deploy/run.sh"
systemctl daemon-reload
systemctl enable --now eval-harness-web

cat <<EOF

Provisioning done. Next steps:
  1. sudo nano $ENV_FILE                    # set real API keys + contact email
  2. nano $APP_DIR/deploy/run-config.env    # set which models to run (edit + git commit/pull to change later)
  3. sudo systemctl enable --now eval-harness
  4. journalctl -u eval-harness -f    # watch progress
The dashboard web server (eval-harness-web, localhost:8080 on the droplet) is
already running — view it live from your Mac with:
  deploy/live_view.sh <droplet-ip> <run-id>
See deploy/README.md for the full walkthrough, including pulling results back
and tearing the droplet down when the run is done.
EOF
