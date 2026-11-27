#!/bin/bash
# Sync Obsidian Vault to GitHub (run from /root/secondbrain)

cd /root/secondbrain
git add obsidian-vault/
git commit -m "Obsidian sync: $(date '+%Y-%m-%d %H:%M')" || true
git push origin main