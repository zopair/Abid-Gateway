#!/usr/bin/env bash
set -euo pipefail
: "${GPG_KEY_ID:?Set GPG_KEY_ID to your local signing key fingerprint}"
git config --local user.signingkey "$GPG_KEY_ID"
git config --local gpg.format openpgp
git config --local commit.gpgsign true
echo "Local commits use GPG key $GPG_KEY_ID. Never commit private keys/passphrases."
