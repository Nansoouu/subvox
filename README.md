<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Nansoouu/subvox/main/assets/logo-white.svg">
    <img alt="Subvox" src="https://raw.githubusercontent.com/Nansoouu/subvox/main/assets/logo.svg" width="280">
  </picture>
</p>

<h3 align="center">The open-source video subtitle studio</h3>

<p align="center">
  Paste any video URL &rarr; get subtitled video in 21 languages, in minutes.
  Community-driven, transparent, decentralized.
</p>

<p align="center">
  <a href="#how-it-works">How it works</a> &middot;
  <a href="#try-it">Try it</a> &middot;
  <a href="#community-pools">Community pools</a> &middot;
  <a href="#contributing">Contributing</a> &middot;
  <a href="#roadmap">Roadmap</a>
</p>

<p align="center">
  <a href="https://github.com/Nansoouu/subvox-pipeline">
    <img src="https://img.shields.io/badge/code-subvox--pipeline-blue?style=flat-square" alt="Pipeline">
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/license-MIT-green?style=flat-square" alt="License">
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/status-alpha-orange?style=flat-square" alt="Status">
  </a>
</p>

---

## What is Subvox?

Subvox is an **open-source video subtitle engine** that translates any video into 21 languages.

**How it works in 30 seconds:**

```
1. Paste a video URL (X/Twitter, TikTok, YouTube, Instagram, Vimeo...)
2. Pick a target language (21 languages supported)
3. Wait 1-10 minutes
4. Get a video with burned-in subtitles + downloadable SRT/VTT
```

**The engine (subvox-pipeline):**
- Downloads the video via yt-dlp
- Transcribes speech via Groq Whisper (with local fallback planned)
- Translates subtitles via DeepSeek/LLaMA
- Burns subtitles into the video via FFmpeg libass
- Uploads to Supabase storage

The pipeline engine code is **fully open-source** at [Nansoouu/subvox-pipeline](https://github.com/Nansoouu/subvox-pipeline).

---

## Try it

| Platform | URL |
|----------|-----|
| **Web app** | [subvox.app](https://subvox.app) |
| **API** | `https://api.subvox.app/docs` |
| **CLI** | Coming soon (`pip install subvox`) |

---

## Community pools

Subvox is built around a **transparent, community-owned economy**.

| Pool | What it does | How it's funded |
|------|-------------|-----------------|
| **Groq pool** | Free transcription credits for the community | Top-ups from revenue |
| **GPU pool** (planned) | GPU compute for long videos | Community contributions |
| **Rewards pool** | Token rewards for contributors | Percentage of platform fees |

All pool logic is **public** and auditable in this repo's `pool/` directory.

---

## Supported languages

| Language | Code |
|----------|------|
| English | en |
| French | fr |
| Spanish | es |
| Portuguese | pt |
| German | de |
| Italian | it |
| Dutch | nl |
| Polish | pl |
| Russian | ru |
| Arabic | ar |
| Hindi | hi |
| Chinese (Simplified) | zh |
| Japanese | ja |
| Korean | ko |
| Turkish | tr |
| Vietnamese | vi |
| Thai | th |
| Indonesian | id |
| Romanian | ro |
| Hungarian | hu |
| Ukrainian | uk |

---

## Contributing

Subvox is 100% community-driven. No VC, no corporate agenda.

**Ways to contribute:**

| Type | Where | Ideal for |
|------|-------|-----------|
| **Code** | [subvox-pipeline](https://github.com/Nansoouu/subvox-pipeline) | Developers |
| **Translations** | [subvox-pipeline](https://github.com/Nansoouu/subvox-pipeline) | Multilingual folks |
| **Design** | [subvox-pipeline](https://github.com/Nansoouu/subvox-pipeline) | Creatives |
| **Documentation** | This repo (`docs/`) | Writers |
| **GPU compute** | Reach out on Discord | Infrastructure helpers |

**Contributors get token rewards** (SUBTEST on Solana devnet). See `rewards/` for details.

---

## Architecture

```
User ──▶ Frontend (Next.js) ──▶ Pipeline API ──▶ Celery Worker
                                        │
                                        ├── Download (yt-dlp)
                                        ├── Transcribe (Groq Whisper)
                                        ├── Translate (DeepSeek/LLaMA)
                                        ├── Burn subtitles (FFmpeg)
                                        └── Upload (Supabase)

Privacy layer ▶ Economy API (auth, billing, credentials)
```

- **Pipeline** — [Nansoouu/subvox-pipeline](https://github.com/Nansoouu/subvox-pipeline) (open-source)
- **Economy** — Private (auth, billing, credentials)
- **Frontend** — Private (Next.js UI)
- **Community** — **This repo** (documentation, pools, governance)

---

## Roadmap

See [ROADMAP.md](docs/ROADMAP.md) for the full picture.

**Current focus:**
- [x] Pipeline works end-to-end (local)
- [x] Community Groq pool active
- [x] 21 language support
- [ ] Automated tests
- [ ] GPU support for long videos
- [ ] YouTube cookies/proxy support
- [ ] Translation without API key (local LLaMA)
- [ ] Transcription cache (SHA256 + whisper.cpp)

---

## License

MIT — see [LICENSE](LICENSE).

Built with love by [Nansou](https://github.com/Nansoouu) and contributors.
