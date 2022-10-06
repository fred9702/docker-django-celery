echo "Making migrations..."
python manage.py makemigrations

echo "Running migrations..."
python manage.py migrate

echo "Starting ddc app..."
python manage.py runserver 0.0.0.0:8000