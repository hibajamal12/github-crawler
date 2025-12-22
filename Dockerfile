FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    libpq-dev \
    curl \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir \
    --default-timeout=100 \
    --retries 5 \
    -i https://pypi.org/simple \
    -r requirements.txt

COPY src/ ./src/
COPY scripts/ ./scripts/

RUN useradd -m -u 1000 appuser && \
    chown -R appuser:appuser /app
USER appuser

CMD ["python", "src/crawler.py"]