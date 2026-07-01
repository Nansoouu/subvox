# Subvox Roadmap

## Phase 1 — Foundations (now)

| Priority | Topic | Status |
|----------|-------|--------|
| P0 | Pipeline end-to-end works | Done |
| P0 | Groq pool community credits | Done |
| P1 | Automated tests | In progress |
| P1 | CI pipeline | Planned |
| P2 | API documentation (Swagger) | Done |
| P2 | Usage examples | Planned |
| P2 | README badges | Done |

## Phase 2 — Key features (next month)

| Priority | Topic | Description |
|----------|-------|-------------|
| P0 | GPU support + long video splitting | Burn is slow on 30min+ videos. Parallel segments + GPU (videotoolbox/nvenc/vaapi) |
| P0 | YouTube/Vimeo/Dailymotion support | yt-dlp with cookies + proxy |
| P1 | Translation without API key | Fallback to local LLaMA via Ollama |
| P1 | Visible queue | Web UI to see job status |
| P1 | Job cancellation | Stop a translation in progress |
| P1 | SRT/VTT export only | Download subtitles without the video |
| P2 | Multi-language simultaneous | Translate to 5+ languages in one click |
| P2 | Auto source language detection | Detect video language before translation |

## Phase 3 — Ecosystem (3-6 months)

| Topic | Description |
|-------|-------------|
| Plugin system | Anyone can add a translation engine |
| Webhook API | Notify external apps when translation is ready |
| Smart cache | Don't re-transcribe already-done videos |
| Official CLI | `pip install subvox` |
| Rewards program | Contributors earn SUBTEST tokens |

## Token rewards

See `rewards/tokenomics.md` for the full breakdown.

---

*This roadmap is living — it evolves with feedback and contributions.*
