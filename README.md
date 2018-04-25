# Example Django Application with Celery

## Running The App

- `$ git clone <this repo>`
- `$ pip install -r requirements.txt`
- `$ ./manage.py migrate`

Start the server

- `$ ./manage.py runserver`

Start the worker

- `$ celery worker --app=health_celery --statedb=django`

Start flower

- `$ flower -A health_celery --port=5555`

## Celery Behavior

When starting Celery, the default is to listen to all Queues.

```
$ celery worker --app=health_celery --statedb=django --loglevel=INFO

celery@Anthonys-MBP v4.1.0 (latentcall)

Darwin-17.5.0-x86_64-i386-64bit 2018-04-25 22:08:52

[config]
.> app:         health_celery:0x106c77610
.> transport:   redis://localhost:6379/0
.> results:
.> concurrency: 4 (prefork)
.> task events: OFF (enable -E to monitor tasks in this worker)

[queues]
.> backoffice       exchange=backoffice(direct) key=default
.> blackbird        exchange=blackbird(direct) key=default
.> caching          exchange=caching(direct) key=default
.> default          exchange=default(direct) key=default
.> pathways         exchange=pathways(direct) key=default
.> refresh          exchange=refresh(direct) key=default
.> reports          exchange=reports(direct) key=default
.> snapshots        exchange=snapshots(direct) key=default

[tasks]
  . health_celery.account.jobs.space_task
  . health_celery.account.jobs.time_task
  . health_celery.pathways.jobs.space_task
  . health_celery.pathways.jobs.time_task
  . health_celery.reports.jobs.space_task
  . health_celery.reports.jobs.time_task

```

You can specify individual Queues to listen to by using `--queues`. The following will only listen to the queues: default and reports.

```
$ celery worker --app=health_celery --statedb=django --loglevel=INFO --queues=reports,default
```

If any tasks are queued in, say, the `pathways` queue, they will not be ran until a worker is started that will listen on that queue. At which point the backlogged items will start to process. This is exactly what I was able to do locally. I started Celery to only listen to queues `reports` and `default`. Starting jobs in these queues worked. Started jobs in `pathways` sent the job to redis but celery did not pick it up. After I restarted celery to listen on the `pathways` queue, the backlogged jobs started running. 

## Extras Included

- [Django Celery Results](https://github.com/celery/django-celery-results) - This extension enables you to store Celery task results using the Django ORM. It defines a single model (django_celery_results.models.TaskResult) used to store task results, and you can query this database table like any other Django model.
- [Flower](http://flower.readthedocs.io/en/latest/) - Flower is a web based tool for monitoring and administrating Celery clusters

