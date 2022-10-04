echo "Making migrations..."
python manage.py makemigration

echo "Applying migrations..."
python manage.py migrate

echo "Starting App..."
poetry run python manage.py runserver 