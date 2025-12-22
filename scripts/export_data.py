#!/usr/bin/env python3
import sys
import os
import csv
import json
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.database import DatabaseManager
from src.models import Repository

def export_to_csv():
    """Export repositories to CSV"""
    db = DatabaseManager()
    
    try:
        # Create exports directory
        os.makedirs("exports", exist_ok=True)
        
        # Get all repositories
        repos = db.session.query(Repository).all()
        
        # CSV export
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        csv_filename = f"exports/repositories_{timestamp}.csv"
        
        with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = [
                'github_id', 'full_name', 'owner_login', 'stargazers_count',
                'language', 'forks_count', 'open_issues_count', 'size_kb',
                'created_at', 'updated_at', 'last_crawled', 'archived'
            ]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            writer.writeheader()
            for repo in repos:
                writer.writerow({
                    'github_id': repo.github_id,
                    'full_name': repo.full_name,
                    'owner_login': repo.owner_login,
                    'stargazers_count': repo.stargazers_count,
                    'language': repo.language,
                    'forks_count': repo.forks_count,
                    'open_issues_count': repo.open_issues_count,
                    'size_kb': repo.size_kb,
                    'created_at': repo.created_at.isoformat() if repo.created_at else '',
                    'updated_at': repo.updated_at.isoformat() if repo.updated_at else '',
                    'last_crawled': repo.last_crawled.isoformat() if repo.last_crawled else '',
                    'archived': repo.archived
                })
        
        print(f"✅ Exported {len(repos)} repositories to {csv_filename}")
        
        # JSON export (optional)
        json_filename = f"exports/repositories_{timestamp}.json"
        repos_data = [
            {
                'full_name': repo.full_name,
                'stars': repo.stargazers_count,
                'language': repo.language,
                'forks': repo.forks_count
            }
            for repo in repos[:1000]  # First 1000 for JSON
        ]
        
        with open(json_filename, 'w', encoding='utf-8') as jsonfile:
            json.dump(repos_data, jsonfile, indent=2, ensure_ascii=False)
        
        print(f"✅ Exported sample data to {json_filename}")
        
    except Exception as e:
        print(f"❌ Error exporting data: {e}")
        sys.exit(1)
    finally:
        db.close()

if __name__ == "__main__":
    export_to_csv()