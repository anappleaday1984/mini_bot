# OpenClaw Cron Jobs Summary

**Last Updated**: 2026-02-14
**Repository**: anappleaday1984/mini_bot

---

## 📊 Active Cron Jobs (9 Total)

### 🐳 Sandbox Jobs (Isolated Sessions)

| # | Job Name | Schedule | Session | Description |
|---|----------|----------|---------|-------------|
| 1 | AI News Daily Summary | `0 9 * * *` | isolated | Fetches AI news from 5 RSS sources, generates daily summary |
| 2 | Job Tracker - Every 24H | `0 9 * * *` | isolated | Monitors 104/1111/LinkedIn for Data/AI/ML jobs (salary >= 2M TWD, Taipei/Tainan) |
| 3 | Job Monitor - 7-Eleven | `0 9 * * 3,6` | isolated | Monitors 7-Eleven job postings (Data/AI/ML keywords) |
| 4 | Competitor Analysis - 9AM | `0 9 * * *` | isolated | FamilyMart vs 7-Eleven App/CDP analysis |
| 5 | Competitor Analysis - 12PM | `0 12 * * *` | isolated | 3-hour update: App updates, digital activities, pain points |
| 6 | Competitor Analysis - 3PM | `0 15 * * *` | isolated | 3-hour update: CDP-related news comparison |
| 7 | Competitor Analysis - 6PM | `0 18 * * *` | isolated | 3-hour update: Latest findings and recommendations |
| 8 | Market Analysis Weekly | `0 21 * * 0` | isolated | Weekly US stock industry reports (AI, Energy, Semiconductor) |

### 🔔 Main Session Jobs

| # | Job Name | Schedule | Description |
|---|----------|----------|-------------|
| 1 | HBL 決賽索票追蹤 | `2026-02-17T01:00:00Z` | One-time reminder for HBL finals ticket registration |
| 2 | LINE Reminders | `50 11 * * *` | Periodic LINE reminders for cron docs |

---

## 📈 Feature Summary

### 🤖 AI News Tracking
- **Sources**: 5 AI-focused RSS feeds
- **Output**: Daily markdown summary with tables
- **Schedule**: 9:00 AM daily
- **Location**: `notes/ai_news/highlights/`

### 💼 Job Search Monitoring
- **Platforms**: 104, 1111, LinkedIn
- **Filter**: Annual salary >= 2,000,000 TWD
- **Locations**: Taipei, Tainan
- **Keywords**: 數據, Data, AI, ML, Engineer, CDP, MarTech
- **Schedule**: Every 24 hours at 9:00 AM
- **Notification**: Telegram via @Teleclaw_a_bot

### 📺 YouTube Channel Monitoring
- **Channels (7 total)**:
  - OpenAI
  - Google DeepMind
  - TradingKey 財經
  - Silicon Valley 101
  - 游庭皓的財經皓角
  - Anthropic
  - Meta AI
- **Schedule**: Daily at 8:00 AM
- **Notification**: Telegram when new videos found

### 📊 Competitor Analysis (FamilyMart vs 7-Eleven)
- **Focus Areas**:
  - App update logs (3 months)
  - CDP/Customer Data Platform initiatives
  - Digital membership activities
  - Personalization efforts
  - Pain point detection (8 categories)
- **Keywords (20+)**:
  - App: 7-ELEVMEN, OpenPoint, FamiPort
  - Membership: 會員生態圈, 跨國累點, 歸戶
  - CDP: Customer Data Platform, 數據驅動
  - Pain Points: 當機, 效能, 登入, 更新, 支付
- **Schedule**: Every 3 hours (9:00, 12:00, 15:00, 18:00)
- **Output**: `competitor_analysis/reports/`

### 📈 Market Analysis
- **Sectors**: AI, Energy, Semiconductor
- **Stocks Tracked**:
  - AI: NVDA, AMD, MSFT, GOOGL, META, PLTR, AI
  - Energy: XOM, CVX, COP, SLB, EOG
  - Semiconductor: SOXX, SMH, INTC, QCOM, TSM
- **Schedule**: Sunday 9:00 PM
- **Output**: `notes/market_analysis/`

---

## 🛠️ Technical Stack

- **Platform**: OpenClaw Gateway
- **Language**: Python 3.9
- **APIs Used**:
  - Brave Search API
  - Telegram Bot API
  - Yahoo Finance
  - RSS Feeds
- **Storage**: Local filesystem + GitHub sync

---

## 📁 Project Structure

```
mini_bot/
├── cdp_project/
│   ├── scripts/
│   │   ├── ai_news_daily.py
│   │   ├── youtube_monitor.py
│   │   └── realtime.py
│   ├── notes/
│   │   └── ai_news/
│   └── competitor_analysis/
│       ├── competitor_monitor.py
│       ├── data/
│       └── reports/
├── skills/
│   ├── market_analysis/
│   ├── job_monitor/
│   └── job_tracker/
├── workspace/
│   ├── notes/
│   │   ├── market_analysis/
│   │   └── job_tracker/
│   └── logs/
└── CRON_JOBS_SUMMARY.md
```

---

## 🔑 Environment Variables

```bash
export TELEGRAM_TOKEN="your_bot_token"
export TELEGRAM_CHAT_ID="your_chat_id"
export BRAVE_API_KEY="your_brave_api_key"
export GITHUB_TOKEN="your_github_token"
```

---

## 📅 Next Scheduled Runs

| Job | Next Run |
|-----|----------|
| AI News Daily | 2026-02-14 09:00 GMT+8 |
| Job Tracker | 2026-02-14 09:00 GMT+8 |
| Competitor Analysis | 2026-02-14 09:00 GMT+8 |
| YouTube Monitor | 2026-02-14 08:00 GMT+8 (next day) |
| Market Analysis | 2026-02-16 21:00 GMT+8 |

---

*Generated on 2026-02-14*
