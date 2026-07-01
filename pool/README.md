# Community Pools

This directory contains the public code for Subvox community resource pools.

## Groq pool

The Groq pool provides **free transcription credits** to the community. Subvox holds a shared Groq API key that registered users can use for up to 2 hours of transcription per day.

**How it works:**

1. A user submits a video for translation
The pipeline checks if the user has Groq pool access
- If yes, transcription uses the community Groq key (free for the user)
- If no, the user must have their own key or a connected wallet

**Code:** `pool/groq/`

> Note: The actual API key is stored securely and never exposed in this repo.

## GPU pool (planned)

The GPU pool will provide shared GPU compute for burning subtitles on long videos (>30 min).

**How it will work:**
- Community members can contribute GPU compute time
- Contributors earn SUBTEST tokens proportional to GPU time donated
- Users with long videos get faster burns via the pool

## Pool rules

- Pool resources are for legitimate video translation use only
- Rate limits apply per user per day
- Abuse = permanent ban from the pool
