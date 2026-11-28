#!/bin/bash
# Full auto-sync: secondbrain repo + tablet obsidian-vault
# Runs from /root/secondbrain

set -e

echo "🔄 Starting full auto-sync..."

# 1. Stage everything in secondbrain
cd /root/secondbrain
git add -A

# 2. Commit with auto-sync message
git commit -m "auto-sync: $(date '+%Y-%m-%d %H:%M')" || true

# 3. Pull latest from origin (rebase local commits on top)
git pull --rebase origin main || true

# 4. Push to GitHub
git push origin main

echo "✅ secondbrain repo synced"

# 5. Also sync tablet's obsidian-vault folder
if [ -d "/mnt/sdcard/obsidian-vault" ]; then
    echo "📱 Syncing tablet vault..."
    cd /mnt/sdcard/obsidian-vault
    git add -A
    git commit -m "tablet auto-sync: $(date '+%Y-%m-%d %H:%M')" || true
    git pull --rebase origin main || true
    git push origin main || true
    echo "✅ Tablet vault synced"
else
    echo "⚠️ Tablet vault not found at /mnt/sdcard/obsidian-vault"
fi

echo "🎉 Full auto-sync complete"