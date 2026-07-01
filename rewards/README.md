# Rewards & Tokenomics

Subvox rewards contributors with **SUBVOX** tokens.

## Token supply

| Metric | Value |
|--------|-------|
| Token name | SUBVOX |
| Network | Solana (devnet for testing, mainnet TBD) |
| Decimals | 6 |
| Initial supply | TBD at launch |

## How to earn

### 1. Share your Groq key

Add your Groq API key to the community pool and earn **55% of every translation** that uses your key.

Each key has two parts:
- **personal_ratio** (default 50%): reserved for your personal use
- **shared_ratio** (100 - personal_ratio): shared with the community pool

You earn on both sides: your personal translations use your own key, and when the pool uses your shared capacity, you get paid.

### 2. Share your cookies

Some platforms (YouTube, etc.) require authentication cookies to download videos. Share your encrypted cookies and earn SUBVOX each time they are used.

Your cookies are encrypted with Fernet (AES-128) and stored securely. You can revoke access at any time.

### 3. Hold SUBVOX tokens

Hold SUBVOX tokens to earn a share of the **10% holders pool**, distributed daily.

**Reward weight:**
- Passion tier (500K+ SUBVOX): 1x weight
- Builder tier (1M+ SUBVOX + Groq key): 2x weight

Daily distribution: the holders pool (10% of all translation fees from the last 24 hours) is split proportionally based on balance * weight.

### 4. Contribute code

Pending -- mission system is being built. See `GET /rewards` in the API once launched.

## Revenue split per translation

Every translation payment (in SUBVOX) is split automatically:

| Share | Recipient | Detail |
|-------|-----------|--------|
| **55%** | Groq key provider | Goes to the wallet that provided the Groq key for this job |
| **20%** | Platform fee | Operational costs, hosting, development |
| **20%** | Holders pool | Distributed daily to all token holders |
| **5%** | Burned | Tokens permanently removed from circulation |

## Pricing

Translation cost depends on video duration:

| Duration | Price (SUBVOX) | Free? |
|----------|---------------|-------|
| < 2 min | 0 | Yes (Decouverte tier) |
| 2-5 min | 500 | No |
| 5-15 min | 1,500 | No |
| 15-30 min | 3,000 | No |
| 30-60 min | 6,000 | No |
| 60-90 min | 10,000 | No |

Multi-language discount: 20% off each additional language.

## Tiers

| Tier | Min balance | Watermark? | Daily limit | Rewards weight | Requires Groq key? |
|------|------------|-----------|-------------|----------------|-------------------|
| **Decouverte** | 0 SUBVOX | Yes | 3/day | 0x | No |
| **Passion** | 500,000 SUBVOX | No | Unlimited | 1x | No |
| **Builder** | 1,000,000 SUBVOX | No | Unlimited | 2x | Yes |

## How rewards are distributed

1. Every translation generates a payment with 75/15/10 split
2. The 10% holders pool accumulates in `subvox_transactions`
3. A daily cron job (`distribute_holder_rewards`) splits the pool
4. Holders receive their share based on balance * weight
5. Distribution is recorded in the database and visible on the history page

## Claiming

Feature coming soon. Connect your Solana wallet and link your GitHub account on the web app.