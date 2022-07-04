import os

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

workers = os.environ.get('GUNICORN_WORKERS', default=4)
bind = os.environ.get('GUNICORN_BIND_ADDRESS', default='127.0.0.1:8000')
wsgi_app = os.environ.get('GUNICORN_WSGI_APP', default='config.wsgi:application')
loglevel = os.environ.get('GUNICORN_LOGLEVEL', default='info')
reload = True if os.environ.get('DEBUG') else False
name = 'movies_name'
threads = os.environ.get('GUNICORN_THREADS', default=2)
max_requests = os.environ.get('GUNICORN_MAX_REQUESTS', default=1000)
max_requests_jitter = os.environ.get('GUNICORN_MAX_REQUESTS_JITTER', default=100)
timeout = os.environ.get('GUNICORN_TIMEOUT', default=30)
