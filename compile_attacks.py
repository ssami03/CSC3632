#!/usr/bin/env python3
# compile_attacks.py
# Create a single Compile.md by concatenating relevant files from known-cyber-attacks repo.

import os
import sys

REPO_DIR = "./known-cyber-attacks"   # adjust if you cloned somewhere else
OUT_FILE = "Compile.md"
EXTS = (".md", ".markdown", ".txt", ".html", ".htm")

def read_text(path):
    try:
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception:
        with open(path, "r", encoding="latin-1") as f:
            return f.read()

def extract_title(text, filename):
    # Prefer first Markdown header (# or ##), else first non-empty line, else filename
    for line in text.splitlines():
        s = line.strip()
        if not s:
            continue
        if s.startswith("#"):
            return s.lstrip("#").strip()
        return s
    return filename

def main(repo_dir=REPO_DIR, out_file=OUT_FILE):
    if not os.path.isdir(repo_dir):
        print(f"Repo folder not found: {repo_dir}", file=sys.stderr)
        sys.exit(1)

    files = []
    for root, dirs, filenames in os.walk(repo_dir):
        for fn in sorted(filenames):
            if fn.lower().endswith(EXTS):
                files.append(os.path.join(root, fn))

    if not files:
        print("No matching files found.", file=sys.stderr)
        sys.exit(0)

    with open(out_file, "w", encoding="utf-8") as out:
        out.write("# Compile of known-cyber-attacks repository\n\n")
        out.write(f"Generated from: {repo_dir}\n\n")
        for p in files:
            try:
                text = read_text(p)
            except Exception as e:
                print(f"Skipping {p} (read error): {e}", file=sys.stderr)
                continue
            rel = os.path.relpath(p, repo_dir)
            title = extract_title(text, rel)
            out.write(f"## {title}\n")
            out.write(f"**Source:** {rel}\n\n")
            out.write(text + "\n\n")
            out.write("---\n\n")
    print(f"Wrote {out_file} (merged {len(files)} files)")

if __name__ == "__main__":
    main()
