#!/usr/bin/env python3
"""
AI News Sync to Mini Bot Repository
每日同步 AI 新聞摘要到 mini_bot repo
每週合併為單一檔案（檔名為該週週日日期）
"""

import os
import sys
import json
import shutil
import subprocess
from datetime import datetime, timedelta
from pathlib import Path
from typing import List, Dict

# 設定
CONFIG = {
    'source_folder': '/Users/the_mini_bot/.openclaw/workspace/cdp_project/data/',
    'repo_folder': '/Users/the_mini_bot/mini_bot_backup',
    'notes_folder': 'notes/ai_news',
    'weekly_folder': 'notes/ai_news/weekly',
    'github_token_env': 'GITHUB_TOKEN',
}


def get_sunday_of_week(date: datetime = None) -> str:
    """取得該週週日日期（YYYYMMDD 格式）"""
    if date is None:
        date = datetime.now()
    
    # 週日是一週的第一天
    days_since_sunday = date.weekday() + 1  # Monday=0, Sunday=6 → Sunday=7
    if days_since_sunday == 7:
        days_since_sunday = 0
    
    sunday = date - timedelta(days=days_since_sunday)
    return sunday.strftime('%Y%m%d')


def get_this_week_range() -> tuple:
    """取得本週週日-週六日期"""
    today = datetime.now()
    sunday = today - timedelta(days=today.weekday() + 1)
    if sunday > today:
        sunday -= timedelta(weeks=1)
    saturday = sunday + timedelta(days=6)
    return sunday, saturday


def find_ai_news_files(source_folder: str, start_date: str = None, end_date: str = None) -> List[Path]:
    """找出 AI 新聞 HTML 檔案"""
    folder = Path(source_folder)
    files = list(folder.glob('ai_news_*.html'))
    
    # 過濾日期範圍
    if start_date and end_date:
        files = [f for f in files if start_date <= f.stem.split('_')[1] <= end_date]
    
    return sorted(files)


def copy_daily_news(repo_folder: str, source_folder: str) -> int:
    """複製每日新聞到 repo"""
    repo_path = Path(repo_folder) / CONFIG['notes_folder']
    repo_path.mkdir(parents=True, exist_ok=True)
    
    # 找出最新的 AI news 檔案
    source_path = Path(source_folder)
    latest_file = max(source_path.glob('ai_news_*.html'), key=os.path.getmtime, default=None)
    
    if not latest_file:
        print("❌ 找不到 AI news 檔案")
        return 0
    
    # 複製到 repo
    dst = repo_path / latest_file.name
    shutil.copy2(latest_file, dst)
    print(f"✅ 已複製: {latest_file.name} → {dst}")
    return 1


def consolidate_weekly_news(repo_folder: str, source_folder: str, week_start: str = None) -> str:
    """合併本週所有新聞為單一檔案"""
    if week_start is None:
        week_start = get_sunday_of_week()
    
    # 取得本週日期範圍
    sunday_date = datetime.strptime(week_start, '%Y%m%d')
    start_date = week_start
    end_date = (sunday_date + timedelta(days=6)).strftime('%Y%m%d')
    
    # 找出本週所有檔案
    news_files = find_ai_news_files(source_folder, start_date, end_date)
    
    if not news_files:
        print(f"❌ 本週（{week_start}）沒有新聞檔案")
        return None
    
    # 建立週資料夾
    weekly_folder = Path(repo_folder) / CONFIG['weekly_folder']
    weekly_folder.mkdir(parents=True, exist_ok=True)
    
    # 合併內容
    combined_html = '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>AI News Weekly Summary</title>
    <style>
        body { font-family: -apple-system, BlinkMacSystemFont, sans-serif; padding: 20px; background: #1a1a2e; color: #fff; }
        .day { background: rgba(255,255,255,0.05); border-radius: 10px; padding: 15px; margin-bottom: 15px; }
        h1 { background: linear-gradient(90deg, #00d4ff, #7c3aed); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        .meta { color: #a0aec0; margin-bottom: 20px; }
        .article { padding: 8px 0; border-left: 2px solid #7c3aed; margin-left: 10px; }
        .title { font-size: 14px; }
    </style>
</head>
<body>
    <h1>🤖 AI 新聞每週摘要</h1>
    <div class="meta">📅 週期: {week_start} - {end_date} | 📰 {len(news_files)} 天</div>
'''.format(week_start=week_start, end_date=end_date)
    
    # 解析並合併每個檔案
    for file_path in news_files:
        date_str = file_path.stem.replace('ai_news_', '')[:8]
        date_formatted = datetime.strptime(date_str, '%Y%m%d').strftime('%Y-%m-%d')
        
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 提取 body 內容
        body_start = content.find('<body>')
        body_end = content.find('</body>')
        if body_start != -1 and body_end != -1:
            day_content = content[body_start+6:body_end]
            combined_html += f'<div class="day"><h2>📆 {date_formatted}</h2>{day_content}</div>\n'
    
    combined_html += '</body></html>'
    
    # 儲存合併檔案
    output_file = weekly_folder / f'ai_news_{week_start}.html'
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(combined_html)
    
    print(f"✅ 已合併: {output_file.name}（{len(news_files)} 天）")
    return str(output_file)


def git_commit_and_push(repo_folder: str, message: str = None) -> bool:
    """Git commit 並推送到 GitHub"""
    os.chdir(repo_folder)
    
    if not message:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M')
        message = f"chore: Update AI news - {timestamp}"
    
    # Git add
    subprocess.run(['git', 'add', CONFIG['notes_folder']], capture_output=True)
    
    # Git commit
    result = subprocess.run(['git', 'commit', '-m', message], capture_output=True)
    if result.returncode != 0:
        if 'nothing to commit' in result.stderr.decode():
            print("ℹ️ 沒有變更需要提交")
            return True
        print(f"❌ Commit 失敗: {result.stderr.decode()}")
        return False
    
    # Git push
    token = os.environ.get(CONFIG['github_token_env'])
    if not token:
        print("❌ GITHUB_TOKEN 未設定")
        return False
    
    push_url = f'https://anappleaday1984:{token}@github.com/anappleaday1984/mini_bot.git'
    result = subprocess.run(['git', 'push', push_url, 'main'], capture_output=True, timeout=30)
    
    if result.returncode == 0:
        print("✅ 已推送到 GitHub")
        return True
    else:
        print(f"❌ Push 失敗: {result.stderr.decode()[:200]}")
        return False


def sync_daily():
    """每日同步"""
    print("=" * 50)
    print("📡 每日 AI News 同步")
    print("=" * 50)
    
    copied = copy_daily_news(CONFIG['repo_folder'], CONFIG['source_folder'])
    
    if copied > 0:
        git_commit_and_push(CONFIG['repo_folder'], "chore: Add daily AI news")
    
    return copied > 0


def sync_weekly():
    """每週同步（合併）"""
    print("=" * 50)
    print("📅 每週 AI News 合併")
    print("=" * 50)
    
    week_start = get_sunday_of_week()
    output_file = consolidate_weekly_news(CONFIG['repo_folder'], CONFIG['source_folder'], week_start)
    
    if output_file:
        git_commit_and_push(CONFIG['repo_folder'], f"chore: Weekly AI news summary ({week_start})")
    
    return output_file is not None


def main():
    """主程式"""
    mode = sys.argv[1] if len(sys.argv) > 1 else 'daily'
    
    if mode == 'daily':
        success = sync_daily()
    elif mode == 'weekly':
        success = sync_weekly()
    elif mode == 'both':
        success = sync_daily()
        if success:
            success = sync_weekly()
    else:
        print(f"未知模式: {mode}")
        print("使用方式: python ai_news_sync.py [daily|weekly|both]")
        success = False
    
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()
