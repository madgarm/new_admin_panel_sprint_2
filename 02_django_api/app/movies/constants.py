from django.db import models


class FilmWorkType(models.TextChoices):
    MOVIE = 'movie', 'Фильм'
    TV_SHOW = 'tv_show', 'ТВ-шоу'


class PersonRoles(models.TextChoices):
    ACTOR = 'actor', 'Актёр'
    WRITER = 'writer', 'Писатель'
    DIRECTOR = 'director', 'Директор'
