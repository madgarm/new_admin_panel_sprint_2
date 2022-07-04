from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_URL = '/staticfiles/'
STATIC_ROOT = BASE_DIR / 'staticfiles'
MEDIA_URL = '/mediafiles/'
MEDIA_ROOT = BASE_DIR / 'mediafiles'
