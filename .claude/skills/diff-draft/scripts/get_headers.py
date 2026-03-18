#!/usr/bin/env python3
# Prints the ## section headers from both the current and last-committed versions of a Draft.md.
# Usage: get_headers.py <path-to-Draft.md>
import subprocess, os, sys

if len(sys.argv) < 2:
    print("Usage: get_headers.py <path-to-Draft.md>", file=sys.stderr)
    sys.exit(1)

draft_path = os.path.abspath(sys.argv[1])

repo_root = subprocess.run(
    ['git', 'rev-parse', '--show-toplevel'],
    capture_output=True, text=True, cwd=os.path.dirname(draft_path)
).stdout.strip()
git_rel_path = os.path.relpath(draft_path, repo_root)

with open(draft_path) as f:
    new_content = f.read()

result = subprocess.run(
    ['git', 'show', f'HEAD:{git_rel_path}'],
    capture_output=True, text=True, cwd=repo_root
)
if result.returncode != 0:
    print("GIT ERROR:", result.stderr, file=sys.stderr)
    sys.exit(1)

old_content = result.stdout

def get_headers(text):
    return [line.strip() for line in text.split('\n') if line.startswith('## ')]

print("OLD HEADERS:")
for h in get_headers(old_content):
    print(f"  {h}")
print("NEW HEADERS:")
for h in get_headers(new_content):
    print(f"  {h}")
