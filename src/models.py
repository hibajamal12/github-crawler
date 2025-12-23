from sqlalchemy import Column, Integer, String, BigInteger, DateTime, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Repository(Base):
    __tablename__ = 'repositories'

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    github_id = Column(BigInteger, unique=True, nullable=False, index=True)
    name = Column(String(255), nullable=False)
    full_name = Column(String(255), nullable=False, index=True)
    owner_login = Column(String(255), nullable=False)
    stargazers_count = Column(Integer, default=0)
    last_crawled = Column(DateTime, default=datetime.utcnow, index=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)
    archived = Column(Boolean, default=False)
    language = Column(String(100))
    forks_count = Column(Integer, default=0)
    open_issues_count = Column(Integer, default=0)
    size_kb = Column(Integer, default=0)
    
    def __repr__(self):
        return f"<Repository {self.full_name}: {self.stargazers_count} stars>"

class CrawlMetadata(Base):
    __tablename__ = 'crawl_metadata'
    
    id = Column(Integer, primary_key=True)
    total_repos_crawled = Column(Integer, default=0)
    last_crawl_start = Column(DateTime, default=datetime.utcnow)
    last_crawl_end = Column(DateTime)
    rate_limit_remaining = Column(Integer)
    rate_limit_reset = Column(DateTime)