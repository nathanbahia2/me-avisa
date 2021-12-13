worker: celery -A webScrapingProdutos worker --loglevel=info -Q celery & celery -A webScrapingProdutos beat --loglevel=info --scheduler django_celery_beat.schedulers:DatabaseScheduler
web: gunicorn webScrapingProdutos.wsgi --log-file -
release: python manage.py migrate