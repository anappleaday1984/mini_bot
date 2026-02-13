# Mini Bot Notes Backup

本地 Markdown 筆記自動備份工具

## 功能

- 📁 監控本地筆記資料夾
- 🔄 自動複製到本地 Repo
- 📝 自動 Git Commit
- ☁️ 自動 Push 到 GitHub
- ⏰ 支援定時備份

## 使用方法

### 1. 設定環境變數

```bash
export GITHUB_TOKEN="ghp_你的token"
```

### 2. 設定筆記路徑

編輯 `config.json`：
```json
{
  "notes_folder": "/你的/筆記/路徑"
}
```

### 3. 執行備份

```bash
# 執行一次備份
./run_backup.sh backup

# 僅掃描筆記
./run_backup.sh scan

# 僅推送到 GitHub
./run_backup.sh push
```

### 4. 定時備份（排程）

```bash
# 加入 crontab，每天晚上 10 點備份
crontab -e

# 加入這行：
0 22 * * * /Users/the_mini_bot/mini_bot_backup/run_backup.sh backup >> ~/backup_cron.log 2>&1
```

## 筆記存放位置

筆記請放在：`~/Documents/MarkdownNotes/`

支援 `.md` 格式的 Markdown 檔案。

## GitHub Repo

🔗 https://github.com/anappleaday1984/mini_bot

## 日誌位置

- 執行日誌：`logs/backup.log`
- Cron 日誌：`~/backup_cron.log`（如有設定）
