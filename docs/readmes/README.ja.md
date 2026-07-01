# Subvox -- 日本語 README

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

完全版は英語のメイン README をお読みください。以下は日本語での主要情報です。

Subvox はコミュニティのための**オープンソース動画字幕エンジン**です。動画URLを貼り付け、言語を選び、数分で字幕付き動画を取得できます。

## なぜ Subvox なのか？

動画翻訳は**何十億人**に関わる問題です。韓国語のチュートリアル、ドイツ語の会議、アラビア語の講義、スペイン語のブログ。言語は障壁であるべきではありません。

**問題点:** 既存のツール (Veed, Kapwing, Descript, Opus Clip) は時間制限、書き出し制限があり、高額なサブスクリプションに縛られます。

**解決策:** 誰もが得をする分散型コミュニティ。

| 誰が | 何を得るか |
|------|----------|
| **ヘビーユーザー** | 低価格で無制限の動画翻訳。21言語。 |
| **Groq キー所有者** | 未使用のキーを共有し、翻訳ごとに55%を獲得。 |
| **トークン保有者** | 500K+ SUBVOX を保有し、毎日報酬を獲得。 |
| **貢献者** | バグ報告、コード作成、翻訳。SUBVOX を獲得。 |
| **全員** | 透明で監査可能なシステム。全員が報酬を得られることを保証。 |

## パイプラインの仕組み

### 1. ダウンロード
yt-dlp 経由でダウンロード。暗号化されたクッキーを共有し、使用ごとに SUBVOX を獲得。

### 2. 文字起こし
Groq Whisper 経由で文字起こし。**コミュニティ Groq プール**が無料クレジットを提供。キーを共有し、コストの55%を獲得。

### 3. 翻訳
DeepSeek 経由で字幕を翻訳。

### 4. 書き込み
FFmpeg 経由で字幕を動画に書き込み。

### 5. 配信
字幕付き動画とダウンロード可能な SRT/VTT ファイルが準備完了。

## コミュニティ経済

各翻訳で SUBVOX が生成され、自動的に分配されます：

| 割合 | 受取人 |
|------|-------|
| **55%** | Groq キー提供者 |
| **20%** | プラットフォーム（ホスティング、開発、運用） |
| **20%** | 保有者プール（毎日分配） |
| **5%** | 焼却（流通から永久に削除） |

## SUBVOX 料金

| 動画時間 | 料金 (SUBVOX) |
|---------|--------------|
| < 2分 | **無料** (Discovery ティア) |
| 2-5分 | 500 |
| 5-15分 | 1,500 |
| 15-30分 | 3,000 |
| 30-60分 | 6,000 |
| 60-90分 | 10,000 |

**多言語割引：** 追加言語ごとに20%オフ。

## 稼ぎ方

**1. Groq キーを共有** -- あなたのキーを使用した翻訳ごとに55%を獲得。

**2. クッキーを共有** -- 制限されたプラットフォームを解放し SUBVOX を獲得。

**3. SUBVOX を保有** -- 保有者は手数料の10%を毎日分配。

## ティア

| ティア | 最低残高 | 報酬倍率 | 特典 |
|-------|---------|---------|------|
| **Discovery** | 0 SUBVOX | 報酬なし | <2分無料、透かし、3回/日 |
| **Passion** | 500,000 SUBVOX | ×1 | 無制限時間、透かしなし |
| **Builder** | 1,000,000 SUBVOX + Groqキー | ×2 | 報酬×2、Groqキー+55% |

## 公式リンク

| プラットフォーム | リンク |
|--------------|------|
| **ウェブサイト** | 近日公開 |
| **X / Twitter** | 近日公開 |
| **Discord** | 近日公開 |
| **GitHub** | [github.com/Nansoouu/subvox](https://github.com/Nansoouu/subvox) |

> **公式リファレンスポイント**
> このリポジトリは Subvox の**唯一の公式ソース**です。
> **他の場所で見つけた Subvox アドレスを決して信頼しないでください。**
