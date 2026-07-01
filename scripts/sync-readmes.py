#!/usr/bin/env python3
"""Translate the main README.md into all 18 languages via DeepSeek.
Usage: python3 scripts/sync-readmes.py
"""
import json, os, sys, time, httpx, re

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
MAIN = os.path.join(ROOT, "README.md")
READMES = os.path.join(ROOT, "docs", "readmes")

# Get DeepSeek key
auth = json.load(open(os.path.expanduser("~/.hermes/auth.json")))
cp = auth.get("credential_pool", {})
ds = cp.get("deepseek", [])
KEY = ds[0].get("access_token") if ds else os.environ.get("DEEPSEEK_API_KEY")
if not KEY:
    print("ERROR: No DeepSeek key")
    sys.exit(1)

LANGS = {
    "ar": {"name": "Arabic", "flag": "🇸🇦", "badge": "lightgrey"},
    "de": {"name": "German", "flag": "🇩🇪", "badge": "orange"},
    "es": {"name": "Spanish", "flag": "🇪🇸", "badge": "green"},
    "fa": {"name": "Persian", "flag": "🇮🇷", "badge": "green"},
    "fr": {"name": "French", "flag": "🇫🇷", "badge": "blue"},
    "he": {"name": "Hebrew", "flag": "🇮🇱", "badge": "blue"},
    "hi": {"name": "Hindi", "flag": "🇮🇳", "badge": "orange"},
    "id": {"name": "Indonesian", "flag": "🇮🇩", "badge": "red"},
    "it": {"name": "Italian", "flag": "🇮🇹", "badge": "red"},
    "ja": {"name": "Japanese", "flag": "🇯🇵", "badge": "blueviolet"},
    "ko": {"name": "Korean", "flag": "🇰🇷", "badge": "brightblue"},
    "nl": {"name": "Dutch", "flag": "🇳🇱", "badge": "brightblue"},
    "pl": {"name": "Polish", "flag": "🇵🇱", "badge": "purple"},
    "pt": {"name": "Portuguese", "flag": "🇵🇹", "badge": "brightgreen"},
    "ru": {"name": "Russian", "flag": "🇷🇺", "badge": "purple"},
    "tr": {"name": "Turkish", "flag": "🇹🇷", "badge": "red"},
    "uk": {"name": "Ukrainian", "flag": "🇺🇦", "badge": "yellow"},
    "vi": {"name": "Vietnamese", "flag": "🇻🇳", "badge": "brightgreen"},
    "zh": {"name": "Chinese (Simplified)", "flag": "🇨🇳", "badge": "critical"},
}

def build_banner(code, name):
    """Build language selector banner for translated README."""
    # All languages including English for the banner
    ALL_LANGS = {
        "en": {"name": "English", "flag": "🇬🇧", "badge": "blue"},
        "fr": {"name": "Français", "flag": "🇫🇷", "badge": "blue"},
        "es": {"name": "Español", "flag": "🇪🇸", "badge": "green"},
        "pt": {"name": "Português", "flag": "🇵🇹", "badge": "brightgreen"},
        "de": {"name": "Deutsch", "flag": "🇩🇪", "badge": "orange"},
        "it": {"name": "Italiano", "flag": "🇮🇹", "badge": "red"},
        "nl": {"name": "Nederlands", "flag": "🇳🇱", "badge": "brightblue"},
        "pl": {"name": "Polski", "flag": "🇵🇱", "badge": "purple"},
        "ru": {"name": "Русский", "flag": "🇷🇺", "badge": "purple"},
        "uk": {"name": "Українська", "flag": "🇺🇦", "badge": "yellow"},
        "ar": {"name": "العربية", "flag": "🇸🇦", "badge": "lightgrey"},
        "hi": {"name": "हिन्दी", "flag": "🇮🇳", "badge": "orange"},
        "fa": {"name": "فارسی", "flag": "🇮🇷", "badge": "green"},
        "he": {"name": "עברית", "flag": "🇮🇱", "badge": "blue"},
        "zh": {"name": "中文", "flag": "🇨🇳", "badge": "critical"},
        "ja": {"name": "日本語", "flag": "🇯🇵", "badge": "blueviolet"},
        "ko": {"name": "한국어", "flag": "🇰🇷", "badge": "brightblue"},
        "tr": {"name": "Türkçe", "flag": "🇹🇷", "badge": "red"},
        "vi": {"name": "Tiếng Việt", "flag": "🇻🇳", "badge": "brightgreen"},
        "id": {"name": "Bahasa Indonesia", "flag": "🇮🇩", "badge": "red"},
    }
    order = ["en", "fr", "es", "pt", "de", "it", "nl", "pl", "ru", "uk",
             "ar", "hi", "fa", "he", "zh", "ja", "ko", "tr", "vi", "id"]
    lines = []
    for lc in order:
        info = ALL_LANGS[lc]
        href = "../README.md" if lc == "en" else (f"README.{lc}.md" if lc == code else f"README.{lc}.md")
        label_enc = info["name"].replace(" ", "%20")
        lines.append(f'<a href="{href}"><img src="https://img.shields.io/badge/{label_enc}-{info["flag"]}-{info["badge"]}" alt="{info["name"]}"></a>')
    return "  \n".join(lines) + "\n\n"

def translate_markdown(text, lang_name):
    """Translate markdown content while preserving structure."""
    prompt = f"""Translate this entire Markdown document to {lang_name}. Keep ALL markdown syntax intact:
- Keep headings, lists, tables, links, code blocks
- Keep HTML tags like <div>, <img>, <br/>, <em>
- Keep all image src paths EXACTLY as they are (do NOT change paths)
- Keep all URLs and anchor links exactly as they are
- Keep badges and shields.io URLs exactly as they are
- Translate ONLY the visible text content

DOCUMENT:
{text}

Return the FULL translated document in {lang_name}. Do NOT omit any section."""

    for attempt in range(3):
        try:
            r = httpx.post("https://api.deepseek.com/v1/chat/completions",
                headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"},
                json={"model": "deepseek-chat", "messages": [
                    {"role": "system", "content": f"Professional translator. Translate Markdown to {lang_name}. Keep ALL HTML, Markdown, URLs, image paths exactly as-is."},
                    {"role": "user", "content": prompt}
                ], "temperature": 0.15, "max_tokens": 8000}, timeout=120)
            return r.json()["choices"][0]["message"]["content"].strip()
        except Exception as e:
            print(f"  Retry {attempt+1}: {e}")
            time.sleep(3)
    return None


def main():
    with open(MAIN) as f:
        main_content = f.read()

    # Extract the content AFTER the language selector badges (find "---" after badges)
    # The main README has badges followed by --- then content
    parts = main_content.split("---\n", 2)
    if len(parts) >= 3:
        body = "---\n".join(parts[2:])  # Content after second ---
    else:
        body = main_content

    # Screenshots section to inject
    screenshots = """## Screenshots

<div align="center">
  <img src="public/screenshots/download_subvox.png" alt="Download mode" style="border-radius:12px;border:1px solid rgba(255,255,255,0.1);max-width:100%;height:auto;margin-bottom:16px">
  <br/>
  <img src="public/screenshots/translate_mode_subvox.png" alt="Translate mode" style="border-radius:12px;border:1px solid rgba(255,255,255,0.1);max-width:100%;height:auto;margin-bottom:16px">
  <br/>
  <img src="public/screenshots/reward_subvox.png" alt="Rewards page" style="border-radius:12px;border:1px solid rgba(255,255,255,0.1);max-width:100%;height:auto">
  <br/>
  <em>Download · Translate · Earn — all in one platform</em>
</div>

---

"""

    for code, info in sorted(LANGS.items()):
        print(f"\n  → {code} ({info['name']})...")

        # Build the full translated document
        banner = build_banner(code, info["name"])

        # Translate the body
        print(f"    Translating...")
        translated = translate_markdown(body, info["name"])
        if not translated:
            print(f"    ✗ Failed after 3 retries")
            continue

        # Combine: banner + screenshots + translated body
        full = banner + screenshots + translated

        # Write
        fp = os.path.join(READMES, f"README.{code}.md")
        with open(fp, "w") as f:
            f.write(full)
        print(f"    ✓ Written ({len(full)} chars)")

        time.sleep(1)  # rate limit

    print("\n✅ All done")


if __name__ == "__main__":
    main()
