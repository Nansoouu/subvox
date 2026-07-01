# Subvox -- 한국어 README

<a href="../README.md"><img src="https://img.shields.io/badge/English-🇬🇧-blue" alt="English"></a>
<a href="README.fr.md"><img src="https://img.shields.io/badge/Francais-🇫🇷-blue" alt="Francais"></a>
<a href="README.es.md"><img src="https://img.shields.io/badge/Espanol-🇪🇸-green" alt="Espanol"></a>
<a href="README.pt.md"><img src="https://img.shields.io/badge/Portugues-🇵🇹-brightgreen" alt="Portugues"></a>
<a href="README.de.md"><img src="https://img.shields.io/badge/Deutsch-🇩🇪-orange" alt="Deutsch"></a>
<a href="README.it.md"><img src="https://img.shields.io/badge/Italiano-🇮🇹-red" alt="Italiano"></a>
<a href="README.ru.md"><img src="https://img.shields.io/badge/Russian-🇷🇺-purple" alt="Russian"></a>
<a href="README.zh.md"><img src="https://img.shields.io/badge/中文-🇨🇳-critical" alt="中文"></a>
<a href="README.ja.md"><img src="https://img.shields.io/badge/日本語-🇯🇵-blueviolet" alt="日本語"></a>
<a href="README.ko.md"><img src="https://img.shields.io/badge/한국어-🇰🇷-brightblue" alt="한국어"></a>
<a href="README.ar.md"><img src="https://img.shields.io/badge/العربية-🇸🇦-lightgrey" alt="العربية"></a>

---

전체 버전은 영어 메인 README를 읽어주세요. 다음은 한국어 핵심 정보입니다.

Subvox는 커뮤니티를 위한 **오픈소스 동영상 자막 엔진**입니다. 동영상 URL을 붙여넣고 언어를 선택하면 몇 분 안에 자막이 포함된 동영상을 받을 수 있습니다.

## 왜 Subvox인가요?

동영상 번역은 **수십억 명**의 사람들과 관련됩니다. 한국어 튜토리얼, 독일어 컨퍼런스, 아랍어 강의, 스페인어 블로그. 언어는 장벽이 되어서는 안 됩니다.

**문제:** 기존 도구(Veed, Kapwing, Descript, Opus Clip)는 시간을 제한하고, 내보내기를 제한하며, 비싼 구독에 가둡니다.

**해결책:** 모두가 이익을 보는 분산형 커뮤니티.

| 누가 | 무엇을 얻나요 |
|-----|-------------|
| **헤비 유저** | 저렴한 가격으로 무제한 동영상 번역. 21개 언어. |
| **Groq 키 보유자** | 사용하지 않는 키를 공유하고 번역당 75%를 획득하세요. |
| **토큰 보유자** | 500K+ SUBVOX를 보유하고 매일 보상을 받으세요. |
| **기여자** | 버그 신고, 코드 작성, 번역. SUBVOX 획득. |
| **모두** | 투명하고 감사 가능한 시스템. 모든 사람이 보상을 받도록 보장합니다. |

## 파이프라인 작동 방식

### 1. 다운로드
yt-dlp를 통해 다운로드. 암호화된 쿠키를 공유하고 사용할 때마다 SUBVOX 획득.

### 2. 전사
Groq Whisper를 통해 전사. **커뮤니티 Groq 풀**이 무료 크레딧 제공. 키를 공유하고 비용의 75% 획득.

### 3. 번역
DeepSeek를 통해 자막 번역.

### 4. 삽입
FFmpeg를 통해 동영상에 자막 삽입.

### 5. 전달
자막이 포함된 동영상과 다운로드 가능한 SRT/VTT 파일 제공.

## 커뮤니티 경제

각 번역은 SUBVOX를 생성하며 자동으로 분배됩니다:

| 비율 | 받는 사람 |
|-----|---------|
| **75%** | Groq 키 제공자 |
| **15%** | 플랫폼(호스팅, 개발, 운영) |
| **10%** | 보유자 풀(매일 분배) |

## SUBVOX 가격

| 동영상 길이 | 가격 (SUBVOX) |
|-----------|--------------|
| < 2분 | **무료** (Discovery 등급) |
| 2-5분 | 500 |
| 5-15분 | 1,500 |
| 15-30분 | 3,000 |
| 30-60분 | 6,000 |
| 60-90분 | 10,000 |

**다국어 할인:** 추가 언어당 20% 할인.

## 수익 창출 방법

**1. Groq 키 공유** -- 키를 사용한 번역당 75% 획득.

**2. 쿠키 공유** -- 제한된 플랫폼 잠금 해제 및 SUBVOX 획득.

**3. SUBVOX 보유** -- 보유자는 수수료의 10%를 매일 분배받습니다.

## 등급

| 등급 | 최소 잔액 | 보상 가중치 | 혜택 |
|-----|---------|----------|-----|
| **Discovery** | 0 SUBVOX | 보상 없음 | <2분 무료, 워터마크, 3회/일 |
| **Passion** | 500,000 SUBVOX | ×1 | 무제한 시간, 워터마크 없음 |
| **Builder** | 1,000,000 SUBVOX + Groq 키 | ×2 | 보상 ×2, Groq 키 +75% |

## 공식 링크

| 플랫폼 | 링크 |
|-------|------|
| **웹사이트** | 곧 출시 |
| **X / Twitter** | 곧 출시 |
| **Discord** | 곧 출시 |
| **GitHub** | [github.com/Nansoouu/subvox](https://github.com/Nansoouu/subvox) |

> **공식 참조 지점**
> 이 저장소는 Subvox의 **유일한 공식 소스**입니다.
> **다른 곳에서 찾은 Subvox 주소를 절대 신뢰하지 마세요.**
