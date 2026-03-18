#!/usr/bin/env python3
# Extracts a named ## section from both the current and last-committed versions of a Draft.md.
# Usage: get_section.py <path-to-Draft.md> <new-section-name> [old-section-name]
# If old-section-name is omitted it defaults to new-section-name (no rename).
import subprocess, os, sys

if len(sys.argv) < 3:
    print("Usage: get_section.py <path-to-Draft.md> <new-section-name> [old-section-name]", file=sys.stderr)
    sys.exit(1)

draft_path = os.path.abspath(sys.argv[1])
new_section = sys.argv[2]
old_section = sys.argv[3] if len(sys.argv) > 3 else new_section

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

def extract_section(text, section_name):
    lines = text.split('\n')
    in_section = False
    result = []
    for line in lines:
        if line.startswith('## '):
            if in_section:
                break
            if line.strip() == f'## {section_name}':
                in_section = True
        if in_section:
            result.append(line)
    return '\n'.join(result)

print("=== OLD ===")
print(extract_section(old_content, old_section))
print("\n=== NEW ===")
print(extract_section(new_content, new_section))
