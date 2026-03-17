#!/usr/bin/env python3
"""
Assembles Draft.md files into a single Document.md.

Usage:
    python3 assemble.py '<json_map>' <output_path>

Where <json_map> is a JSON array of section objects:
    [
        {"level": 1, "header": "Title", "folder": null, "has_draft": false},
        {"level": 2, "header": "Introduction", "folder": "/path/to/1-introduction", "has_draft": true},
        ...
    ]
"""

import json, re, os, sys

def render_draft(path):
    with open(path) as f:
        text = f.read()
    # Remove Type metadata line
    text = re.sub(r'^\*\*Type\*\*:.*\n?', '', text, flags=re.MULTILINE)
    # Parse **Lead:** ... **Development:** ... pairs
    pattern = re.compile(
        r'\*\*Lead:\*\*\s*(.*?)\s*\*\*Development:\*\*\s*(.*?)(?=\*\*Lead:\*\*|\Z)',
        re.DOTALL
    )
    paragraphs = []
    for m in pattern.finditer(text):
        lead = m.group(1).strip()
        dev = m.group(2).strip()
        para = (lead + ' ' + dev) if dev else lead
        para = re.sub(r'\n+', ' ', para).strip()
        paragraphs.append(para)
    return '\n\n'.join(paragraphs)

def assemble(sections, out_path):
    lines = []
    filled = []
    empty = []

    for sec in sections:
        heading = '#' * sec['level'] + ' ' + sec['header']
        lines.append(heading)
        if sec['folder'] is not None:
            if sec['has_draft']:
                draft_path = os.path.join(sec['folder'], 'Draft.md')
                prose = render_draft(draft_path)
                lines.append('')
                lines.append(prose)
                filled.append(sec['header'])
            else:
                empty.append(sec['header'])
        lines.append('')

    output = '\n'.join(lines).rstrip() + '\n'
    with open(out_path, 'w') as f:
        f.write(output)

    print(f"Sections filled: {len(filled)}")
    print(f"Sections empty:  {len(empty)}")
    for e in empty:
        print(f"  - {e}")
    print(f"\nWrote {out_path}")

if __name__ == '__main__':
    sections = json.loads(sys.argv[1])
    out_path = sys.argv[2]
    assemble(sections, out_path)
