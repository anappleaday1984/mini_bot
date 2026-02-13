#!/usr/bin/env python3
"""
Markdown Notes Backup Tool
自動備份 Markdown 筆記到 GitHub
"""

import os
import sys
import json
import time
import logging
from datetime import datetime
from pathlib import Path

# 設定日誌
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('logs/backup.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class MarkdownBackupTool:
    def __init__(self, config_file='config.json'):
        self.config = self.load_config(config_file)
        self.notes_folder = Path(self.config['notes_folder'])
        self.repo_folder = Path(self.config.get('repo_folder', '.'))
        
    def load_config(self, config_file):
        """載入設定檔"""
        if os.path.exists(config_file):
            with open(config_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            # 預設設定
            return {
                'notes_folder': os.path.expanduser('~/Documents/MarkdownNotes'),
                'repo_folder': os.path.expanduser('~/mini_bot_backup'),
                'auto_commit': True,
                'auto_push': True,
                'schedule_time': '22:00'
            }
    
    def scan_notes(self):
        """掃描筆記資料夾"""
        notes = []
        if self.notes_folder.exists():
            for f in self.notes_folder.rglob('*.md'):
                notes.append({
                    'path': str(f),
                    'name': f.name,
                    'modified': os.path.getmtime(f),
                    'relative_path': str(f.relative_to(self.notes_folder))
                })
        return sorted(notes, key=lambda x: x['modified'], reverse=True)
    
    def copy_notes_to_repo(self, notes):
        """複製筆記到本地 Repo"""
        count = 0
        for note in notes:
            src = Path(note['path'])
            dst = self.repo_folder / 'notes' / note['relative_path']
            
            # 建立目標資料夾
            dst.parent.mkdir(parents=True, exist_ok=True)
            
            # 複製檔案
            if not dst.exists() or dst.stat().st_mtime < note['modified']:
                import shutil
                shutil.copy2(src, dst)
                logger.info(f"Copied: {note['name']}")
                count += 1
        
        logger.info(f"Total files copied: {count}")
        return count
    
    def git_commit(self, message=None):
        """Git Commit"""
        os.chdir(self.repo_folder)
        
        if not message:
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            message = f"Auto backup: {timestamp}"
        
        # Git add
        os.system('git add notes/')
        
        # Git commit
        result = os.system(f'git commit -m "{message}"')
        
        if result == 0:
            logger.info(f"Committed: {message}")
            return True
        else:
            logger.warning("Nothing to commit or commit failed")
            return False
    
    def git_push(self):
        """Git Push to GitHub"""
        os.chdir(self.repo_folder)
        result = os.system('git push origin main')
        
        if result == 0:
            logger.info("Pushed to GitHub successfully")
            return True
        else:
            logger.error("Failed to push to GitHub")
            return False
    
    def backup(self, message=None):
        """完整備份流程"""
        logger.info("=" * 50)
        logger.info("Starting backup...")
        
        # 1. 掃描筆記
        notes = self.scan_notes()
        logger.info(f"Found {len(notes)} notes")
        
        if not notes:
            logger.info("No notes to backup")
            return
        
        # 2. 複製到 Repo
        copied = self.copy_notes_to_repo(notes)
        
        # 3. Git Commit
        committed = False
        if self.config.get('auto_commit', True) and copied > 0:
            committed = self.git_commit(message)
        
        # 4. Git Push
        pushed = False
        if self.config.get('auto_push', True) and committed:
            pushed = self.git_push()
        
        logger.info("Backup completed!")
        logger.info(f"  - Notes scanned: {len(notes)}")
        logger.info(f"  - Files copied: {copied}")
        logger.info(f"  - Committed: {committed}")
        logger.info(f"  - Pushed: {pushed}")
        logger.info("=" * 50)


def main():
    """主程式入口"""
    tool = MarkdownBackupTool()
    
    # 檢查命令列參數
    if len(sys.argv) > 1:
        command = sys.argv[1]
        
        if command == 'backup':
            message = sys.argv[2] if len(sys.argv) > 2 else None
            tool.backup(message)
        elif command == 'scan':
            notes = tool.scan_notes()
            for n in notes:
                print(f"{n['name']} - {datetime.fromtimestamp(n['modified'])}")
        elif command == 'push':
            tool.git_push()
        else:
            print(f"Unknown command: {command}")
            print("Usage: python backup_tool.py [backup|scan|push]")
    else:
        # 預設執行備份
        tool.backup()


if __name__ == '__main__':
    main()
