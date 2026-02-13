# 🤖 AI 新聞摘要

本資料夾存放每日 AI 新聞摘要，透過 OpenClaw 系統自動產生並同步。

---

## 📰 資料來源（分類整理）

### 1️⃣ 深度與應用導向（適合生成產業報告）

| 來源 | 網址 |
|------|------|
| The Decoder | [the-decoder.com](https://the-decoder.com) |
| 特色 | 更新速度快，深入探討技術應用場景，結構清晰適合全文提取 |

| 來源 | 網址 |
|------|------|
| The Rundown AI | [rundown.ai](https://rundown.ai) |
| 特色 | 全球領先的 AI 日報，「5分鐘讀完」精煉格式，涵蓋最新工具與模型更新 |

---

### 2️⃣ 產業與商業趨勢（適合你的職涯規劃）

| 來源 | 網址 |
|------|------|
| AI Business News | [artificialintelligence-news.com](https://www.artificialintelligence-news.com) |
| 特色 | 側重 AI 在企業、能源及技術管理層面新聞，對技術管理職很有參考價值 |

| 來源 | 網址 |
|------|------|
| Superhuman AI | [superhuman.ai](https://superhuman.ai) |
| 特色 | 專注生產力工具與工作流自動化，常有「如何用 AI 取代繁雜任務」的教學 |

---

### 3️⃣ 技術與開源前沿（適合 Mac mini 玩家）

| 來源 | 網址 |
|------|------|
| Hugging Face Blog | [huggingface.co/blog](https://huggingface.co/blog) |
| 特色 | 掌握最新開源模型（如 DeepSeek, Llama 系列）首發動態 |

| 來源 | 網址 |
|------|------|
| OpenClaw 官方 X | [@openclaw](https://x.com/openclaw) |
| 特色 | 官方動態、技能更新、安全修復第一手資訊 |

| 來源 | 網址 |
|------|------|
| OpenClaw Discord | [discord.gg/openclaw](https://discord.gg/openclaw) |
| 特色 | 社群討論、疑難解答、最新的 Agent 技能分享 |

---

### 4️⃣ 經典來源（持續追蹤）

| 來源 | 網址 |
|------|------|
| OpenAI | [openai.com/blog/rss.xml](https://openai.com/blog/rss.xml) |
| Anthropic | [anthropic.com/rss.xml](https://www.anthropic.com/rss.xml) |
| Google AI | [googleaiblog.blogspot.com](http://googleaiblog.blogspot.com/atom.xml) |
| DeepMind | [deepmind.google/blog/rss.xml](https://deepmind.google/blog/rss.xml) |
| Microsoft AI | [blogs.microsoft.com/ai/feed](https://blogs.microsoft.com/ai/feed/) |
| Meta AI | [ai.meta.com/blog/rss.xml](https://ai.meta.com/blog/rss.xml) |
| MIT Tech Review | [technologyreview.com/AI](https://www.technologyreview.com/topic/artificial-intelligence/feed) |
| LangChain | [blog.langchain.dev/rss.xml](https://blog.langchain.dev/rss.xml) |

---

## 📂 檔案結構

```
ai_news/
├── README.md                         ← 本說明檔
├── ai_news_YYYYMMDD_HHMMSS.html    ← 每日新聞（自動產生）
└── weekly/
    └── ai_news_YYYYMMDD.html        ← 每週合併摘要（週日）
```

### 檔案命名規則

- **每日**：以當天日期命名，如 ai_news_20260213_090501.html
- **每週**：以該週週日日期命名，如 ai_news_20260215.html

---

## 🔄 同步方式

每日自動同步腳本：scripts/ai_news_sync.py

```bash
# 每日同步
python3 scripts/ai_news_sync.py daily

# 每週合併
python3 scripts/ai_news_sync.py weekly
```

---

## 📊 統計資訊

| 項目 | 說明 |
|------|------|
| 更新時間 | 每天 09:00（台北時間） |
| 來源數量 | 17+ 個 RSS/網站 |
| 每日篇數 | 約 20-30 篇新聞 |
| 格式 | HTML（含關鍵詞標籤） |

---

## 🎯 關鍵詞標籤

新聞會自動擷取以下關鍵詞：

AI, GPT, LLM, Agent, RAG, ML, Model, Training, Inference, Deployment, Generative, Claude, Safety, Reasoning, Benchmark, Performance, Open Source, Research, DeepSeek, Llama, Workflow Automation, Productivity

---

## 📍 原始資料位置

原始 HTML 檔案同步自：

/Users/the_mini_bot/.openclaw/workspace/cdp_project/data/ai_news_*.html

---

## 🔗 相關連結

- GitHub Repo：anappleaday1984/mini_bot
- OpenClaw 專案：CDP 數據分析平台
- RSS 聚合腳本：scripts/ai_news_sync.py

---

## 📝 更新紀錄

| 日期 | 動作 |
|------|------|
| 2026-02-13 | 初始設定，建立每日同步機制 |
| 2026-02-13 | 新增每週合併功能 |
| 2026-02-13 | 擴充資料來源，分為三大類 |

---

*自動產生 by OpenClaw CDP System*
