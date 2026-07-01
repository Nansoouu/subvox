#!/usr/bin/env python3
"""Replace flag emojis in shields.io badges with ISO country codes.
Flag emojis don't render on iOS Safari in badge URLs."""
import re, os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")

FLAG_TO_ISO = {
    "\U0001f1eb\U0001f1f7": "FR", "\U0001f1ec\0001f1e7": "GB",
    "\U0001f1ea\U0001f1f8": "ES", "\U0001f1e7\U0001f1f7": "BR",
    "\U0001f1e9\U0001f1ea": "DE", "\U0001f1ee\U0001f1f9": "IT",
    "\U0001f1f3\U0001f1f1": "NL", "\U0001f1f5\U0001f1f1": "PL",
    "\U0001f1f7\U0001f1fa": "RU", "\U0001f1fa\U0001f1e6": "UA",
    "\U0001f1e6\U0001f1f8": "SA", "\U0001f1ee\U0001f1f3": "IN",
    "\U0001f1ee\U0001f1f7": "IR", "\U0001f1ee\U0001f1f1": "IL",
    "\U0001f1e8\U0001f1f3": "CN", "\U0001f1ef\U0001f1f5": "JP",
    "\U0001f1f0\U0001f1f7": "KR", "\U0001f1f9\U0001f1f7": "TR",
    "\U0001f1fb\U0001f1f3": "VN", "\U0001f1ee\U0001f1e9": "ID",
    "\U0001f1fa\U0001f1f8": "US", "\U0001f1f2\U0001f1fd": "MX",
    "\U0001f1e8\U0001f1e6": "CA",
}

# Build regex for flag pairs
import unicodedata
flag_chars = "".join(chr(c) for c in range(0x1F1E6, 0x1F200))
flag_re = re.compile(r"([" + flag_chars + "]{2})")

files = ["README.md"] + [f"docs/readmes/{f}" for f in os.listdir(os.path.join(ROOT, "docs/readmes")) if f.endswith(".md")]

for fname in files:
    path = os.path.join(ROOT, fname)
    with open(path) as f:
        content = f.read()
    
    # Only replace flags inside shields.io URLs
    def replace_in_url(m):
        url = m.group(0)
        flag = flag_re.search(url)
        if flag and flag.group(1) in FLAG_TO_ISO:
            iso = FLAG_TO_ISO[flag.group(1)]
            url = url.replace(flag.group(1), iso)
        return url
    
    new_content = re.sub(r'https://img\.shields\.io/badge/[^")\s]+', replace_in_url, content)
    
    if new_content != content:
        with open(path, "w") as f:
            f.write(new_content)
        print(f"  ✓ {fname}")
    else:
        print(f"  - {fname} (no change)")

print("\n✅ Done")
