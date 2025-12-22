-- Create repositories table
CREATE TABLE IF NOT EXISTS repositories (
    id BIGSERIAL PRIMARY KEY,
    github_id BIGINT UNIQUE NOT NULL,
    name VARCHAR(255) NOT NULL,
    full_name VARCHAR(255) NOT NULL,
    owner_login VARCHAR(255) NOT NULL,
    stargazers_count INTEGER DEFAULT 0,
    last_crawled TIMESTAMP DEFAULT NOW(),
    created_at TIMESTAMP,
    updated_at TIMESTAMP,
    archived BOOLEAN DEFAULT FALSE,
    language VARCHAR(100),
    forks_count INTEGER DEFAULT 0,
    open_issues_count INTEGER DEFAULT 0,
    size_kb INTEGER DEFAULT 0
);

-- Create indexes
CREATE INDEX IF NOT EXISTS idx_repos_github_id ON repositories(github_id);
CREATE INDEX IF NOT EXISTS idx_repos_last_crawled ON repositories(last_crawled);
CREATE INDEX IF NOT EXISTS idx_repos_stars ON repositories(stargazers_count DESC);
CREATE INDEX IF NOT EXISTS idx_repos_full_name ON repositories(full_name);

-- Create metadata table for future expansion
CREATE TABLE IF NOT EXISTS crawl_metadata (
    id SERIAL PRIMARY KEY,
    total_repos_crawled INTEGER DEFAULT 0,
    last_crawl_start TIMESTAMP DEFAULT NOW(),
    last_crawl_end TIMESTAMP,
    rate_limit_remaining INTEGER,
    rate_limit_reset TIMESTAMP
);