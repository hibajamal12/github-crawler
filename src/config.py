import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # GitHub API Configuration
    GITHUB_TOKEN = os.getenv('GITHUB_TOKEN', '')
    GITHUB_GRAPHQL_URL = "https://api.github.com/graphql"
    
    # Rate Limiting
    RATE_LIMIT_POINTS = 5000  # Authenticated requests per hour
    RATE_LIMIT_WINDOW = 3600  # seconds
    
    # Database
    DATABASE_URL = os.getenv('DATABASE_URL', 
                            'postgresql://postgres:postgres@localhost:5432/github_crawler')
    
    # Crawling Configuration
    BATCH_SIZE = 100  # GitHub GraphQL max per query
    TOTAL_REPOS = int(os.getenv('TOTAL_REPOS', 100000))
    MAX_RETRIES = 3
    RETRY_DELAY = 5  # seconds between retries
    REQUEST_TIMEOUT = 30  # seconds
    
    # Progress tracking
    SAVE_INTERVAL = 1000  # Save to DB every N repos