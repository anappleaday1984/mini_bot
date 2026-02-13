# Mini Bot Notes Backup

本地 Markdown 筆記自動備份工具

## 功能

- 📁 監控本地筆記資料夾
- 🔄 自動複製到本地 Repo
- 📝 自動 Git Commit
- ☁️ 自動 Push 到 GitHub
- ⏰ 支援定時備份
- 🤖 AI 新聞每日同步 + 每週合併

---

## AI 新聞同步功能

### 資料來源

```
/Users/the_mini_bot/.openclaw/workspace/cdp_project/data/ai_news_*.html
```

### 同步邏輯

| 頻率 | 動作 | 輸出位置 |
|------|------|----------|
| 每日 | 複製最新新聞 | `notes/ai_news/ai_news_YYYYMMDD_HHMMSS.html` |
| 每週 | 合併為單一檔案 | `notes/ai_news/weekly/ai_news_YYYYMMDD.html` |

### 檔案命名規則

- **每日**：`ai_news_YYYYMMDD_HHMMSS.html`
- **每週**：以該週週日為檔名，如 `ai_news_20260215.html`（2/15 為週日）

### 使用方法

```bash
cd ~/mini_bot_backup

# 每日同步
python3 scripts/ai_news_sync.py daily

# 每週合併
python3 scripts/ai_news_sync.py weekly

# 兩者都執行
python3 scripts/ai_news_sync.py both
```

### Crontab 排程範例

```bash
# 每天晚上 9 點同步每日新聞
0 21 * * * cd ~/mini_bot_backup && python3 scripts/ai_news_sync.py daily >> ~/logs/ai_news_daily.log 2>&1

# 每週日晚上 10 點合併每週摘要
0 22 * * 0 cd ~/mini_bot_backup && python3 scripts/ai_news_sync.py weekly >> ~/logs/ai_news_weekly.log 2>&1
```

---

## 一般備份功能

### 設定環境變數

```bash
export GITHUB_TOKEN="ghp_你的token"
```

### 執行備份

```bash
# 執行一次備份
./run_backup.sh backup

# 僅掃描筆記
./run_backup.sh scan

# 僅推送到 GitHub
./run_backup.sh push
```

### 定時備份

```bash
# 加入 crontab，每天晚上 10 點備份
crontab -e

# 加入這行：
0 22 * * * /Users/the_mini_bot/mini_bot_backup/run_backup.sh backup >> ~/backup_cron.log 2>&1
```

---

## 筆記存放位置

一般筆記請放在：`~/Documents/MarkdownNotes/`

AI 新聞會自動同步，無需手動放置。

---

## GitHub Repo

🔗 https://github.com/anappleaday1984/mini_bot

---

## Repo 結構

```
mini_bot_backup/
├── notes/
│   └── ai_news/
│       ├── ai_news_20260213_090501.html  ← 每日新聞
│       └── weekly/
│           └── ai_news_20260215.html      ← 每週合併（週日）
├── scripts/
│   ├── ai_news_sync.py                   ← AI 新聞同步
│   └── backup_tool.py                     ← 一般備份
├── config.json                           ← 設定檔
├── run_backup.sh                          ← 備份執行腳本
└── README.md
```

---

## 日誌位置

- AI 新聞同步：`~/logs/ai_news_daily.log`
- 每週合併：`~/logs/ai_news_weekly.log`
- 一般備份：`./logs/backup.log`
