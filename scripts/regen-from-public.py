#!/usr/bin/env python3
"""
Regenerate the website's Bible chapter JSONs from the USFM published in the
public `oratioandco/aperto-bible` repo, so the website's verse text mirrors what
aperto-bible-dev auto-publishes.

Designed for CI (the website's deploy.yml, on the `usfm-updated` dispatch): runs
before `astro build`, fetches every USFM file currently in public main, and
regenerates the matching `src/content/<slug>-<chapter>-<lang>.json` verse files
in place. Existing committed JSONs that have no published USFM (e.g. legacy
chapters outside the trial scope) are left untouched, so the build always has
content to render.

Pure standard library — no pip install. Reuses the existing converter
(usfm-to-website-json.py) unchanged via subprocess.

Env:
  USFM_REF        git ref to read from aperto-bible (default: main)
  OUTPUT_DIR      where to write the regenerated JSONs (default: src/content)
  GITHUB_TOKEN /  optional — relieves anonymous GitHub API rate limits
  USFM_AUTH_TOKEN

Exit code is 0 unless a real failure should block the deploy; a transient API
error warns and falls back to the committed JSONs (build still succeeds).
"""
import json
import os
import re
import shutil
import subprocess
import sys
import urllib.request
from pathlib import Path

REPO = "oratioandco/aperto-bible"
REF = os.environ.get("USFM_REF", "main")
API_BASE = f"https://api.github.com/repos/{REPO}"
RAW_BASE = f"https://raw.githubusercontent.com/{REPO}"
SCRIPTS = Path(__file__).resolve().parent
OUTPUT_DIR = Path(os.environ.get("OUTPUT_DIR", "src/content"))
STAGING = Path("_usfm_public")  # AB-<LANG>/ layout the converter expects
TOKEN = os.environ.get("GITHUB_TOKEN") or os.environ.get("USFM_AUTH_TOKEN")

# usfm-code stem (NN+CODE, e.g. 42LUK) -> book slug the converter accepts.
CODE_TO_SLUG = {"42LUK": "luke", "19PSA": "psalms", "44ACT": "acts"}

# texts/<lang>/<NN>-<CODE>/<NN><CODE><chap>_ab-<lang>.usfm
PATH_RE = re.compile(
    r"^texts/([a-z]{2})/\d{2}-[A-Z]{3}/(\d{2}[A-Z]{3})(\d+)_ab-([a-z]{2})\.usfm$"
)


def _get(url: str) -> str:
    req = urllib.request.Request(url)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", "aperto-website-regen")
    if TOKEN:
        req.add_header("Authorization", f"Bearer {TOKEN}")
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8")


def fetch_usfm_paths() -> list[str]:
    """List every .usfm path in the public repo at REF (recursive tree)."""
    data = json.loads(_get(f"{API_BASE}/git/trees/{REF}?recursive=1"))
    return [b["path"] for b in data.get("tree", []) if str(b.get("path", "")).endswith(".usfm")]


def main() -> int:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    shutil.rmtree(STAGING, ignore_errors=True)

    try:
        paths = fetch_usfm_paths()
    except Exception as e:
        # Transient API failure: warn, keep committed JSONs, don't fail the build.
        print(f"::warning::Could not fetch USFM tree from {REPO}@{REF} ({e}); "
              f"building with committed JSONs.")
        return 0

    jobs: set[tuple[str, int, str]] = set()  # (slug, chapter, lang)
    for rel in paths:
        m = PATH_RE.match(rel)
        if not m:
            continue
        lang, stem, chap, slang = m.groups()
        slug = CODE_TO_SLUG.get(stem)
        if not slug:
            continue  # a book the website doesn't render
        # Stage in the AB-<LANG>/ layout the converter reads.
        ab_dir = STAGING / f"AB-{lang.upper()}"
        ab_dir.mkdir(parents=True, exist_ok=True)
        try:
            (ab_dir / Path(rel).name).write_text(
                _get(f"{RAW_BASE}/{REF}/{rel}"), encoding="utf-8"
            )
        except Exception as e:
            print(f"::warning::Could not fetch {rel} ({e}); skipping.")
            continue
        jobs.add((slug, int(chap), slang))

    # Regenerate each chapter via the existing converter (unchanged).
    regen = 0
    for slug, chapter, lang in sorted(jobs):
        r = subprocess.run(
            [sys.executable, str(SCRIPTS / "usfm-to-website-json.py"),
             "--book", slug, "--chapter", str(chapter), "--language", lang,
             "--usfm-dir", str(STAGING), "--output-dir", str(OUTPUT_DIR)],
            capture_output=True, text=True,
        )
        if r.returncode != 0:
            print(f"::warning::converter failed for {slug} {chapter} {lang}: "
                  f"{r.stderr.strip() or r.stdout.strip()}")
        else:
            regen += 1
            print(r.stdout.strip().splitlines()[-1] if r.stdout.strip() else f"  OK {slug}-{chapter}-{lang}")

    print(f"Regenerated {regen} chapter JSON(s) in {OUTPUT_DIR} from {REPO}@{REF}.")
    shutil.rmtree(STAGING, ignore_errors=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
