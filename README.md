# Example Django application with Celery

## Running the app

- `$ git clone <this repo>`
- `$ pip install -r requirements.txt`
- `$ ./manage.py migrate`

Start the server

- `$ ./manage.py runserver`

Start the worker

- `$ celery worker --app=health_celery --statedb=django`

Start flower

- `$ flower -A health_celery --port=5555`
