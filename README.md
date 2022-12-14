# Blueprint for app with Docker, Flask and ORM (SQLAlchemy + Flask-Admin)

## Create database

```docker-compose exec web python manage.py create_db```

## Start psql cli

```docker-compose exec db psql --username=hello_flask --dbname=hello_flask_dev```

# setup

https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/

