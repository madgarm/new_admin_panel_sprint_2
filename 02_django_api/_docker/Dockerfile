FROM python:3.10-slim-buster

WORKDIR /opt/app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    DJANGO_SETTINGS_MODULE='config.settings' \
    POETRY_VERSION=1.1.13 \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_CACHE_DIR='/var/cache/pypoetry' \
    POETRY_HOME='/test'

RUN groupadd -g 1000 -r web \
    && useradd -d /opt/app -g web -l -r -u 1000 web \
    && chown web:web -R /opt/app \
    && mkdir -p /opt/app/staticfiles/ /opt/app/mediafiles/ \
    && chown web:web /opt/app/staticfiles/ /opt/app/mediafiles/

RUN pip install --upgrade pip && pip install --upgrade --ignore-installed setuptools && pip install poetry==$POETRY_VERSION

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-dev

COPY ./app .

RUN chown -R web:web /opt/app

USER web

EXPOSE 8000
