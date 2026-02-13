# 🤖 AI 新聞摘要

本資料夾存放每日 AI 新聞摘要，透過 OpenClaw 系統自動產生並同步。

---

## 📰 資料來源

| 來源 | 網址 |
|------|------|
| OpenAI | <https://openai.com/blog/rss.xml> |
| Anthropic | <https://www.anthropic.com/rss.xml> |
| Google AI | <http://googleaiblog.blogspot.com/atom.xml> |
| DeepMind | <https://deepmind.google/blog/rss.xml> |
| Microsoft AI | <https://blogs.microsoft.com/ai/feed/> |
| Meta AI | <https://ai.meta.com/blog/rss.xml> |
| Hugging Face | <https://huggingface.co/blog/rss.xml> |
| MIT Tech Review | <https://www.technologyreview.com/topic/artificial-intelligence/feed> |
| AI Weekly | <https://aiweekly.co/issues/rss.xml> |
| Wired AI | <https://www.wired.com/feed/category/ai/latest/rss> |
| LangChain | <https://blog.langchain.dev/rss.xml> |

---

## 📂 檔案結構

```
ai_news/
├── README.md                         ← 本說明檔
├── ai_news_YYYYMMDD_HHMMSS.html     ← 每日新聞（自動產生）
└── weekly/
    └── ai_news_YYYYMMDD.html        ← 每週合併摘要（週日）
```

### 檔案命名規則

- **每日**：以當天日期命名，如 `ai_news_20260213_090501.html`
- **每週**：以該週週日日期命名，如 `ai_news_20260215.html`

---

## 🔄 同步方式

每日自動同步腳本：`scripts/ai_news_sync.py`

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
| 來源數量 | 14 個 RSS Feed |
| 每日篇數 | 約 15-20 篇新聞 |
| 格式 | HTML（含關鍵詞標籤） |

---

## 🎯 關鍵詞標籤

新聞會自動擷取以下關鍵詞：

- AI, GPT, LLM, Agent, RAG, ML, Model, Training
- Inference, Deployment, Generative, Claude, Safety
- Reasoning, Benchmark, Performance, Open Source, Research

---

## 📍 原始資料位置

原始 HTML 檔案同步自：

```
/Users/the_mini_bot/.openclaw/workspace/cdp_project/data/ai_news_*.html
```

---

## 🔗 相關連結

- **GitHub Repo**：[anappleaday1984/mini_bot](https://github.com/anappleaday1984/mini_bot)
- **OpenClaw 專案**：[ CDP 數據分析平台](openclaw-project)
- **RSS 聚合腳本**：`scripts/ai_news_sync.py`

---

## 📝 更新紀錄

| 日期 | 動作 |
|------|------|
| 2026-02-13 | 初始設定，建立每日同步機制 |
| 2026-02-13 | 新增每週合併功能 |

---

*自動產生 by OpenClaw CDP System*
