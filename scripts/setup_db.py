#!/usr/bin/env python3
# scripts/setup_db.py - SIMPLIFIED VERSION
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.database import DatabaseManager
from src.models import Base

def main():
    print("🗄️ Setting up database...")
    
    try:
        # Initialize database connection
        db = DatabaseManager()
        
        # Create tables
        db.create_tables()
        
        print("✅ Database setup completed successfully!")
        
        # Verify by counting tables
        from sqlalchemy import inspect
        inspector = inspect(db.engine)
        tables = inspector.get_table_names()
        print(f"📊 Created tables: {', '.join(tables)}")
        
    except Exception as e:
        print(f"❌ Error during database setup: {e}")
        sys.exit(1)
    finally:
        if 'db' in locals():
            db.close()

if __name__ == "__main__":
    main()