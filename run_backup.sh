#!/bin/bash
# Markdown Notes Backup Runner
# 使用方法: ./run_backup.sh [backup|scan|push]

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

# 載入環境變數
source ~/.zshrc

# 執行備份
python3 backup_tool.py "$@"

# 狀態檢查
if [ $? -eq 0 ]; then
    echo "✅ 備份完成！"
else
    echo "❌ 備份失敗，請檢查 logs/backup.log"
fi
