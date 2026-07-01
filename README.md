<div align="center">

# Subvox

**The open-source video subtitle studio**
*Translate any video into 21 languages, in minutes. 1800+ platforms supported.*

[![Status](https://img.shields.io/badge/status-alpha-orange?style=flat-square)](/#)
[![License](https://img.shields.io/badge/license-MIT-green?style=flat-square)](LICENSE)

<a href="docs/readmes/README.fr.md"><img src="https://img.shields.io/badge/Francais-🇫🇷-blue" alt="Francais"></a>
<a href="docs/readmes/README.es.md"><img src="https://img.shields.io/badge/Espanol-🇪🇸-green" alt="Espanol"></a>
<a href="docs/readmes/README.pt.md"><img src="https://img.shields.io/badge/Portugues-🇵🇹-brightgreen" alt="Portugues"></a>
<a href="docs/readmes/README.de.md"><img src="https://img.shields.io/badge/Deutsch-🇩🇪-orange" alt="Deutsch"></a>
<a href="docs/readmes/README.it.md"><img src="https://img.shields.io/badge/Italiano-🇮🇹-red" alt="Italiano"></a>

---

**[Get started](#get-started) : [Why Subvox?](#why-subvox) : [How it works](#how-the-pipeline-works) : [Earn](#earn) : [Token & tiers](#subvox-token--tiers)**

---

</div>

> **OFFICIAL POINT OF REFERENCE**
> This repository is the **only official source** for Subvox. All official wallet addresses, token contracts, and links are listed here and nowhere else.
> **Never trust Subvox addresses found anywhere else.** If it's not in this repo, it's a scam.

---

## Why Subvox?

Video translation affects **billions of people**. A Korean tutorial, a German conference, an Arabic lecture, a Spanish vlog. Language should never be a barrier.

**The problem:** Existing tools (Veed, Kapwing, Descript, Opus Clip) restrict you to a few minutes, limit your exports, and lock you into expensive subscriptions. They charge a fortune for what should be accessible.

**The solution:** A decentralized community where everyone wins.

| Who | What they get |
|-----|---------------|
| **Heavy users** | Translate unlimited videos at a fraction of competitor prices. No time limits. 21 languages. |
| **Groq key holders** | Share keys you are not using and earn 75% of every translation that uses them. Passive income. |
| **Token holders** | Stake 500K+ SUBVOX and earn daily rewards from 10% of all platform fees. |
| **Bug fixers & contributors** | Report bugs, write code, translate languages. Earn SUBVOX that has real monetary value. |
| **Everyone** | Transparent, auditable, on-chain. We certify that everyone gets paid and the system works. |

No subscription. No hidden fees. No corporate agenda. Built by the community, for the community.

---

## How the pipeline works

Every translation goes through 5 steps. Here is how the **community** powers each one:

### 1. Download
Your video URL is downloaded via yt-dlp. Community members can share encrypted cookies to unlock restricted platforms (YouTube, etc.).

**You earn:** Share your cookies and get rewarded each time they are used.

### 2. Transcribe
Speech is transcribed to text via Groq Whisper. The **community Groq pool** provides free transcription credits.

**You earn:** Share your Groq API key with the pool. 75% of the translation cost goes to the key provider.

### 3. Translate
Subtitles are translated into the target language via DeepSeek (with local LLaMA fallback planned).

### 4. Burn
Subtitles are burned into the video via FFmpeg. GPU support for long videos is planned.

### 5. Deliver
Your subtitled video is ready with downloadable SRT/VTT files.

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

Add your Groq API key to the community pool and earn **75% of every translation** that uses your key.

| Your key's capacity | What you earn |
|--------------------|---------------|
| 50% personal / 50% shared | Half your key for yourself, half for the pool (you earn on both) |
| 30 min daily limit | Up to 30 min/day reserved for you, rest shared |
| Unlimited | Full personal access + full pool rewards on shared portion |

**How:** Connect your wallet on the web app (coming soon), go to Billing > Groq Pool, paste your key, set your personal ratio.

### 2. Share your cookies

Some platforms (YouTube, etc.) require authentication cookies to download videos. Share your encrypted cookies and earn SUBVOX each time they are used.

**How:** Your cookies are encrypted with Fernet (AES) and stored securely. You can revoke access at any time.

### 3. Hold SUBVOX tokens

Hold SUBVOX tokens to earn a share of the **10% holders pool**, distributed daily.

| Tier | Minimum balance | Reward weight | Benefits |
|------|----------------|---------------|----------|
| **Decouverte** | 0 SUBVOX | No rewards | Free for videos < 2 min, watermark, 3/day |
| **Passion** | 500,000 SUBVOX | 1x weight | Unlimited duration, no watermark, SRT export |
| **Builder** | 1,000,000 SUBVOX + Groq key | 2x weight | 2x rewards, +75% revenue on your Groq key |

**How it works:** Every 24 hours, the holders pool is split proportionally. If you hold 10% of all weighted SUBVOX, you get 10% of that day's pool.

---

## SUBVOX token & tiers

### Pricing

Translation costs are calculated by video duration. Prices are in SUBVOX, per language.

| Video duration | Price (SUBVOX) |
|---------------|----------------|
| < 2 min | **Free** (Decouverte tier) |
| 2-5 min | 500 |
| 5-15 min | 1,500 |
| 15-30 min | 3,000 |
| 30-60 min | 6,000 |
| 60-90 min | 10,000 |

**Multi-language discount:** 20% off each additional language.

### Token

| Property | Value |
|----------|-------|
| Token name | SUBVOX |
| Network | Solana (devnet for testing, mainnet TBD) |
| Token address | Coming soon |
| Decimals | 6 |

### Revenue split per translation

| Share | Who gets it | What for |
|-------|------------|----------|
| **75%** | Groq key provider | The person who shared their Groq key for this translation |
| **15%** | Platform | Hosting, development, operations |
| **10%** | Holders pool | Distributed daily to all SUBVOX token holders |

The distribution happens **automatically** every 24 hours via a cron job. No manual intervention.

### How to get SUBVOX

| Method | Description |
|--------|-------------|
| **Contribute code** | Submit a PR to [subvox-pipeline](https://github.com/Nansoouu/subvox-pipeline) |
| **Share a Groq key** | Add your key to the pool, earn 75% per translation |
| **Share cookies** | Unlock restricted platforms and earn rewards |
| **Report bugs** | Valid bug reports earn tokens |
| **Community work** | Translations, docs, design, moderation |

> **Important:** SUBVOX is a community utility token. It has no guaranteed monetary value. Never pay money for SUBVOX.

---

## Community

Subvox is built **for the community, by the community**. No VC, no corporate agenda.

### How to participate

| Activity | Where |
|----------|-------|
| **Report a bug** | [subvox-pipeline issues](https://github.com/Nansoouu/subvox-pipeline/issues) |
| **Suggest a feature** | Same repo, label `enhancement` |
| **Submit code** | Fork, branch, PR |
| **Translate the project** | Help us add more languages |
| **Share Groq key** | Add to pool, earn 75% per translation |
| **Share cookies** | Unlock platforms, earn rewards |

---

## Supported languages

English, French, Spanish, Portuguese, German, Italian, Dutch, Polish, Russian, Arabic, Hindi, Chinese (Simplified), Japanese, Korean, Turkish, Vietnamese, Thai, Indonesian, Romanian, Hungarian, Ukrainian.

---

## Architecture

For developers who want to dive into the code:

```
Frontend (Next.js)  -->  Pipeline API (FastAPI)  -->  Celery Worker
                                                         |
                                                         |--> Download (yt-dlp)
                                                         |--> Transcribe (Groq Whisper)
                                                         |--> Translate (DeepSeek + LLaMA)
                                                         |--> Burn subtitles (FFmpeg)
                                                         |--> Deliver
```

| Repository | Visibility | Purpose |
|-----------|-----------|---------|
| [subvox](https://github.com/Nansoouu/subvox) | Public | **This repo** -- community hub, docs, pools |
| [subvox-pipeline](https://github.com/Nansoouu/subvox-pipeline) | Public | Pipeline engine (open-source) |

---

## License

MIT -- see [LICENSE](LICENSE).

Built with love by [Nansou](https://github.com/Nansoouu) and the Subvox community.