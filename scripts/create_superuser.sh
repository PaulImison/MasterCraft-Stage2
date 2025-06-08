#!/bin/bash

# Usage: ./scripts/create_superuser.sh

# Load .env
source .env

# Export DATABASE_URL for Django
export DATABASE_URL=$PRODUCTION_DATABASE_URL

# Run migrations
echo "Running migrations on production database..."
python manage.py migrate

# Create superuser
echo "Creating superuser on production database..."
python manage.py createsuperuser

echo "✅ Done! You can now log in to your production /admin site."
