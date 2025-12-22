from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from src.config import Config
from src.models import Base
import time

class DatabaseManager:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._init_database()
        return cls._instance
    
    def _init_database(self):
        """Initialize database connection with retry logic"""
        max_retries = 5
        retry_delay = 5
        
        for attempt in range(max_retries):
            try:
                self.engine = create_engine(
                    Config.DATABASE_URL,
                    pool_size=20,
                    max_overflow=10,
                    pool_pre_ping=True,
                    echo=False  # Set to True for SQL logging
                )
                
                # Test connection
                with self.engine.connect() as conn:
                    conn.execute("SELECT 1")
                
                print("✅ Database connection established successfully")
                break
                
            except Exception as e:
                if attempt < max_retries - 1:
                    print(f"⚠️ Database connection failed (attempt {attempt + 1}/{max_retries}): {e}")
                    time.sleep(retry_delay * (attempt + 1))
                else:
                    print(f"❌ Failed to connect to database after {max_retries} attempts")
                    raise
    
    @property
    def session(self):
        if not hasattr(self, '_session'):
            Session = scoped_session(sessionmaker(bind=self.engine))
            self._session = Session()
        return self._session
    
    def create_tables(self):
        """Create all tables"""
        Base.metadata.create_all(self.engine)
        print("✅ Database tables created")
    
    def close(self):
        """Close database connection"""
        if hasattr(self, '_session'):
            self._session.remove()
        if hasattr(self, 'engine'):
            self.engine.dispose()