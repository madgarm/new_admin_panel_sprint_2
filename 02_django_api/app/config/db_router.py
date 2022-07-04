from typing import Type

from django.db.models import Model
from movies.models import FilmWork, Genre, GenreFilmWork, Person, PersonFilmWork

ROUTED_MODELS = [Genre, Person, PersonFilmWork, GenreFilmWork, FilmWork]


class DBRouter:
    default = 'default'
    content = 'content'

    def db_for_read(self, model: Type[Model], **hints):
        if model in ROUTED_MODELS:
            return self.content
        return self.default

    def db_for_write(self, model: Type[Model], **hints):
        if model in ROUTED_MODELS:
            return self.content
        return self.default
