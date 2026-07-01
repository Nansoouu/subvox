#!/usr/bin/env python3
"""Inject competitive landscape section into all translated READMEs."""
import json, os, sys, time, httpx, re

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
MAIN = os.path.join(ROOT, "README.md")
READMES = os.path.join(ROOT, "docs", "readmes")

# Extract the competitive landscape section from main README
with open(MAIN) as f:
    main = f.read()

# Find the section between "## Competitive Landscape" and "## Why Subvox?"
match = re.search(r'(## Competitive Landscape.*?)(?=\n## Why Subvox\?)', main, re.DOTALL)
if not match:
    print("ERROR: Could not find Competitive Landscape section in main README")
    sys.exit(1)

section_en = match.group(1)

# Read English section to inject into non-English files
# For FR: just copy English section (will be translated separately via the ANALYSIS.md link)

# Target structure: find "---\n\n## Why Subvox?" and insert before it
target_marker = "\n---\n\n## Why Subvox?"

for fname in sorted(os.listdir(READMES)):
    if not fname.endswith(".md"):
        continue
    fp = os.path.join(READMES, fname)
    with open(fp) as f:
        content = f.read()
    
    # Check if already has the section
    if "## Competitive Landscape" in content:
        print(f"  ✓ {fname} — already has section")
        continue
    
    # Find insertion point
    idx = content.find(target_marker)
    if idx == -1:
        print(f"  ✗ {fname} — cannot find insertion point")
        continue
    
    # Insert English section (it will use the analysis link for details)
    new = content[:idx] + section_en + content[idx:]
    
    with open(fp, "w") as f:
        f.write(new)
    
    print(f"  → {fname} — injected")

print("\n✅ Done — competitive landscape added to all files")
