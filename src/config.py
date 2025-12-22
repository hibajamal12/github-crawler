import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    GITHUB_TOKEN = os.getenv('GITHUB_TOKEN', '')
    GITHUB_GRAPHQL_URL = "https://api.github.com/graphql"
    
    RATE_LIMIT_POINTS = 5000  
    RATE_LIMIT_WINDOW = 3600  

    DATABASE_URL = os.getenv('DATABASE_URL', 
                            'postgresql://postgres:postgres@localhost:5432/github_crawler')
   
    BATCH_SIZE = 100  
    TOTAL_REPOS = int(os.getenv('TOTAL_REPOS', 100000))
    MAX_RETRIES = 3
    RETRY_DELAY = 5  
    REQUEST_TIMEOUT = 30  

    SAVE_INTERVAL = 1000 