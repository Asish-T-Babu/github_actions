#!/bin/sh

# Exit on error
set -e

echo "Creating migration..."

alembic revision --autogenerate -m "migration"

echo "Running migrations..."

alembic upgrade head

echo "Starting FastAPI..."

exec uvicorn app.main:app --host 0.0.0.0 --port 8000