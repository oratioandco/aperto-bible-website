#!/usr/bin/env bash
# Regenerate the fixed trial-scope sample chapters in src/content/ from the
# latest USFM published to the public oratioandco/aperto-bible repo.
#
# Trial scope (fixed): LUK 1, LUK 15, PSA 23, PSA 137, PSA 139, ACT 17
# in languages de, en, pl.
#
# Invoked by .github/workflows/deploy.yml on repository_dispatch
# (usfm-updated) / workflow_dispatch so the live site refreshes automatically
# whenever new USFM is published. Safe to run locally too.
set -euo pipefail

SRC_REPO="${USFM_SOURCE_REPO:-https://github.com/oratioandco/aperto-bible.git}"
LANGS=(de en pl)

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$repo_root"

tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT

echo "Fetching published USFM from $SRC_REPO ..."
git clone --depth 1 --filter=blob:none --sparse "$SRC_REPO" "$tmp/src" >/dev/null 2>&1
git -C "$tmp/src" sparse-checkout set texts >/dev/null 2>&1

# Stage the public layout texts/<lang>/<NN-CODE>/<file> into the layout the
# parser expects: <stage>/AB-<LANG>/<file>.
stage="$tmp/usfm"
for lang in "${LANGS[@]}"; do
  mkdir -p "$stage/AB-${lang^^}"
  cp "$tmp/src/texts/$lang/"*/*"_ab-$lang.usfm" "$stage/AB-${lang^^}/" 2>/dev/null || true
done

gen() {
  python3 scripts/usfm-to-website-json.py \
    --book "$1" --chapter "$2" --language "$3" \
    --usfm-dir "$stage" --output-dir src/content
}

for lang in "${LANGS[@]}"; do
  gen luke   1   "$lang"
  gen luke   15  "$lang"
  gen psalms 23  "$lang"
  gen psalms 137 "$lang"
  gen psalms 139 "$lang"
  gen acts   17  "$lang"
done

echo "Trial-scope content regenerated. Changed files (vs working tree):"
git --no-pager diff --stat -- src/content || true
