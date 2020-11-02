web: gunicorn wsgi:app --log-file -
init: pytho manage.py db init
migrate: python manage.py db migrate
upgrade: python manage.py db upgrade