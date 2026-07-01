<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Nansoouu/subvox/main/assets/logo-white.svg">
    <img alt="Subvox" src="https://raw.githubusercontent.com/Nansoouu/subvox/main/assets/logo.svg" width="280">
  </picture>
</p>

<h3 align="center">
  The open-source video subtitle studio<br>
  <small>Translate any video into 21 languages, in minutes.</small>
</h3>

<p align="center">
  <strong>
    <a href="https://subvox.app">subvox.app</a> &middot;
    <a href="#get-started">Get started</a> &middot;
    <a href="#official-links">Official links</a> &middot;
    <a href="#community">Community</a> &middot;
    <a href="#token">$SUBTEST token</a>
  </strong>
</p>

<p align="center">
  <a href="https://x.com/subvoxapp">
    <img src="https://img.shields.io/badge/X-@subvoxapp-000000?style=flat-square&logo=x" alt="X/Twitter">
  </a>
  <a href="(discord link)">
    <img src="https://img.shields.io/badge/Discord-subvox-5865F2?style=flat-square&logo=discord" alt="Discord">
  </a>
  <a href="#">
    <img src="https://img.shields.io/badge/status-alpha-orange?style=flat-square" alt="Status">
  </a>
  <a href="LICENSE">
    <img src="https://img.shields.io/badge/license-MIT-green?style=flat-square" alt="License">
  </a>
</p>

---

## What is Subvox?

Subvox is an **open-source subtitle engine** for the community, by the community. Paste any video URL, pick a language, and get a subtitled video in minutes.

No subscription. No hidden fees. Transparent and decentralized.

### Supported platforms

```
X/Twitter  TikTok  YouTube  Instagram  Vimeo  Dailymotion  and any public video URL
```

### How it works

1. **Paste a URL** — from X, TikTok, YouTube, Instagram, or anywhere
2. **Pick a language** — 21 languages supported
3. **Wait 1-10 minutes** — the pipeline handles everything
4. **Get your video** — with burned-in subtitles + downloadable SRT/VTT

---

## Get started

| Method | URL |
|--------|-----|
| **Web app** | [subvox.app](https://subvox.app) |
| **API (Swagger)** | `https://api.subvox.app/docs` |
| **CLI** | Coming soon — `pip install subvox` |

---

## Official links

| Platform | Link |
|----------|------|
| **Website** | [subvox.app](https://subvox.app) |
| **X / Twitter** | [@subvoxapp](https://x.com/subvoxapp) |
| **Discord** | [Join the server](discord-link) (coming soon) |
| **GitHub** | [github.com/Nansoouu](https://github.com/Nansoouu) |
| **Email** | (contact email) |

### Official Solana wallets

| Network | Address | Purpose |
|---------|---------|---------|
| **Devnet** | `(devnet wallet address)` | SUBTEST token, test transactions |
| **Mainnet** | `(mainnet wallet address)` | Future SUBVOX token, platform revenue |

> These are the **only official Subvox wallets**. We will never ask you to send funds to any other address.

### SUBTEST token

| Property | Value |
|----------|-------|
| Token name | SUBTEST |
| Network | Solana devnet |
| Token address | `(token mint address)` |
| Decimals | 6 |

SUBTEST is a devnet utility token used to power community rewards and test transactions. It has no monetary value.

---

## Community

Subvox is built **for the community, by the community**. No VC, no corporate agenda.

### How to participate

| Activity | Where |
|----------|-------|
| **Report a bug** | [subvox-pipeline issues](https://github.com/Nansoouu/subvox-pipeline/issues) |
| **Suggest a feature** | Same repo, label `enhancement` |
| **Submit code** | Fork, branch, PR — see `COMMUNITY.md` |
| **Translate** | Help us add more languages |
| **Donate GPU** | Join the Discord |

### Token rewards

Contributors earn **SUBTEST** tokens for merged PRs, bug reports, and community work.

| Contribution | SUBTEST |
|-------------|---------|
| Add a language | 10 |
| Write tests | 10 |
| Fix a bug | 15 |
| Minor feature | 50 |
| Cache implementation | 75 |
| YouTube full support | 200 |
| Plugin system | 500 |

See [rewards/](rewards/) for full tokenomics.

---

## Architecture (technical)

For developers who want to dive into the code:

```
Frontend (Next.js)  →  Pipeline API (FastAPI)  →  Celery Worker
                                                     │
                                                     ├── Download (yt-dlp)
                                                     ├── Transcribe (Groq Whisper)
                                                     ├── Translate (DeepSeek + LLaMA fallback)
                                                     ├── Burn subtitles (FFmpeg)
                                                     └── Upload (Supabase)
```

| Repository | Visibility | Purpose |
|-----------|-----------|---------|
| [subvox](https://github.com/Nansoouu/subvox) | Public | **This repo** — community hub, docs, pools |
| [subvox-pipeline](https://github.com/Nansoouu/subvox-pipeline) | Public | Pipeline engine (open-source) |
| subvox-economy | Private | Auth, billing, credentials |

---

## Supported languages

English, French, Spanish, Portuguese, German, Italian, Dutch, Polish, Russian, Arabic, Hindi, Chinese (Simplified), Japanese, Korean, Turkish, Vietnamese, Thai, Indonesian, Romanian, Hungarian, Ukrainian.

---

## License

MIT — see [LICENSE](LICENSE).

Built with love by [Nansou](https://github.com/Nansoouu) and the Subvox community.
