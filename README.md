<div align="center">

# ✦ Subvox ✦

**The open-source video subtitle studio**  
*Translate any video into 21 languages, in minutes. 1800+ platforms supported.*

[![Status](https://img.shields.io/badge/status-alpha-orange?style=flat-square)](/#)
[![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)](LICENSE)

---

**[subvox.app](/#) &middot; [Get started](#get-started) &middot; [Earn](#earn) &middot; [HOLD token](#hold-token) &middot; [Community](#community)**

---

</div>

> **⚠️ OFFICIAL POINT OF REFERENCE**  
> This repository is the **only official source** for Subvox. All official wallet addresses, token contracts, and links are listed here and nowhere else.  
> **Never trust Subvox addresses found anywhere else.** If it's not in this repo, it's a scam.

---

## What is Subvox?

Subvox is an **open-source subtitle engine** for the community, by the community. Paste any video URL, pick a language, and get a subtitled video in minutes.

**1800+ platforms supported** — X/Twitter, TikTok, YouTube, Instagram, Vimeo, Dailymotion, Facebook, and thousands more via yt-dlp.

No subscription. No hidden fees. Transparent and decentralized.

### How it works

1. **Paste a URL** — from any of 1800+ supported platforms
2. **Pick a language** — 21 languages supported
3. **Wait 1-10 minutes** — the pipeline handles everything
4. **Get your video** — with burned-in subtitles + downloadable SRT/VTT

---

## Get started

| Method | Status |
|--------|--------|
| **Web app** | Coming soon |
| **API** | Coming soon |
| **CLI** | Coming soon |

---

## Official links

| Platform | Link |
|----------|------|
| **Website** | Coming soon |
| **X / Twitter** | Coming soon |
| **Discord** | Coming soon |
| **GitHub** | [github.com/Nansoouu/subvox](https://github.com/Nansoouu/subvox) |

### Official Solana wallets

| Network | Address | Purpose |
|---------|---------|---------|
| **Devnet** | Coming soon | SUBTEST token, test transactions |
| **Mainnet** | Coming soon | Future SUBVOX token, platform revenue |

> These are the **only official Subvox wallets**. We will never ask you to send funds to any other address. Beware of impersonators.

---

## Earn

Subvox is designed so that **anyone can earn** by contributing to the ecosystem. No coding required.

### 1. Share your Groq key

If you have a Groq API key with free credits, share it with the community pool and earn rewards proportional to usage.

| Your contribution | You earn |
|-----------------|----------|
| 1 hour of Groq transcription | SUBTEST tokens |
| 10 hours | Bonus multiplier |

**How:** Connect your wallet on the web app (coming soon), link your Groq key, and set your reward rate.

### 2. Share your cookies

Some platforms (YouTube, etc.) require cookies to download videos. Share your cookies securely and earn rewards when they're used.

| Your contribution | You earn |
|-----------------|----------|
| Valid YouTube cookies | SUBTEST tokens per use |
| Multi-region cookies | Premium rate |

**How:** Your cookies are encrypted and stored securely. You can revoke access at any time.

### 3. Hold SUBTEST tokens

Hold SUBTEST tokens to earn a share of platform revenue.

| Tokens held | Revenue share |
|------------|--------------|
| 100+ SUBTEST | Basic tier |
| 1,000+ SUBTEST | Premium tier (x2 multiplier) |
| 10,000+ SUBTEST | Whale tier (x5 multiplier) |

**How it works:** A percentage of every paid translation goes to a rewards pool. Token holders receive their share proportionally.

---

## HOLD token

SUBTEST is a utility token on **Solana devnet** that powers the Subvox community economy.

| Property | Value |
|----------|-------|
| Token name | SUBTEST |
| Network | Solana devnet |
| Token address | Coming soon |
| Decimals | 6 |

### Token utility

- **Earn rewards** — Holders receive a share of platform revenue
- **Community credits** — Use SUBTEST to run translations when the free pool is busy
- **Governance** — Future voting power on pool allocation decisions

### How to get SUBTEST

| Method | Description |
|--------|-------------|
| **Contribute code** | Submit a PR to [subvox-pipeline](https://github.com/Nansoouu/subvox-pipeline) |
| **Share resources** | Groq keys, cookies, GPU compute |
| **Report bugs** | Valid bug reports earn tokens |
| **Community work** | Translations, docs, design, moderation |

> **Important:** SUBTEST is a devnet token with **no monetary value**. It is a community utility token, not an investment. Never pay money for SUBTEST.

---

## Community

Subvox is built **for the community, by the community**. No VC, no corporate agenda.

### How to participate

| Activity | Where |
|----------|-------|
| **Report a bug** | [subvox-pipeline issues](https://github.com/Nansoouu/subvox-pipeline/issues) |
| **Suggest a feature** | Same repo, label `enhancement` |
| **Submit code** | Fork, branch, PR |
| **Translate** | Help us add more languages |
| **Share resources** | Groq keys, cookies, GPU time |

### Token rewards for contributors

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

## Supported languages

English, French, Spanish, Portuguese, German, Italian, Dutch, Polish, Russian, Arabic, Hindi, Chinese (Simplified), Japanese, Korean, Turkish, Vietnamese, Thai, Indonesian, Romanian, Hungarian, Ukrainian.

Translations of this README are available in:

- [English](docs/readmes/README.en.md)
- [French / Francais](docs/readmes/README.fr.md)
- [Spanish / Espanol](docs/readmes/README.es.md)
- [Portuguese / Portugues](docs/readmes/README.pt.md)
- [German / Deutsch](docs/readmes/README.de.md)
- [Italian / Italiano](docs/readmes/README.it.md)
- And more coming soon

---

## Architecture

For developers who want to dive into the code:

```
Frontend (Next.js)  →  Pipeline API (FastAPI)  →  Celery Worker
                                                     │
                                                     ├── Download (yt-dlp)
                                                     ├── Transcribe (Groq Whisper)
                                                     ├── Translate (DeepSeek + LLaMA fallback)
                                                     ├── Burn subtitles (FFmpeg)
                                                     └── Upload
```

| Repository | Visibility | Purpose |
|-----------|-----------|---------|
| [subvox](https://github.com/Nansoouu/subvox) | Public | **This repo** — community hub, docs, pools |
| [subvox-pipeline](https://github.com/Nansoouu/subvox-pipeline) | Public | Pipeline engine (open-source) |

---

## License

MIT — see [LICENSE](LICENSE).

Built with love by [Nansou](https://github.com/Nansoouu) and the Subvox community.