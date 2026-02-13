# 📁 筆記存放區

本資料夾用於存放各類筆記，並透過 backup_tool.py 自動同步至 GitHub。

---

## 目錄結構

```
notes/
├── ai_news/              ← AI 新聞摘要（每日自動同步）
│   ├── README.md         ← AI 新聞說明
│   ├── ai_news_*.html   ← 每日新聞檔案
│   └── weekly/           ← 每週合併摘要
│       └── ai_news_YYYYMMDD.html
├── your_notes.md         ← 你的筆記（手動新增）
└── ...
```

---

## 新增筆記

將 .md 檔案放在 notes/ 資料夾內即可。

範例：
```bash
cp ~/Documents/MarkdownNotes/你的筆記.md notes/
```

---

## 自動同步

每日執行 ./run_backup.sh backup 時會自動：
1. 掃描 ~/Documents/MarkdownNotes/ 資料夾
2. 複製新檔案到 notes/
3. Commit 並 Push 到 GitHub

---

## AI 新聞

請參考 ai_news/README.md
