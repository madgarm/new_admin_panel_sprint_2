from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import Q
from django.http import HttpResponseNotFound, JsonResponse
from django.views.generic import DetailView
from django.views.generic.list import BaseListView
from movies.models import FilmWork


class MoviesApiMixin:
    model = FilmWork
    http_method_names = ['get']

    def get_queryset(self):
        return (
            self.model.objects.annotate(genres=ArrayAgg('genre__name', distinct=True))
            .annotate(
                actors=ArrayAgg(
                    'personfilmwork__person__full_name', filter=Q(personfilmwork__role='actor'), distinct=True
                )
            )
            .annotate(
                directors=ArrayAgg(
                    'personfilmwork__person__full_name', filter=Q(personfilmwork__role='director'), distinct=True
                )
            )
            .annotate(
                writers=ArrayAgg(
                    'personfilmwork__person__full_name', filter=Q(personfilmwork__role='writer'), distinct=True
                )
            )
        )

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)


class MoviesListApi(MoviesApiMixin, BaseListView):
    model = FilmWork
    http_method_names = ['get']
    paginate_by = 50

    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .values(
                'id',
                'title',
                'description',
                'creation_date',
                'rating',
                'type',
                'genres',
                'actors',
                'directors',
                'writers',
            )
        )

    def get_context_data(self, *, object_list=None, **kwargs):
        queryset = self.get_queryset()
        paginator, page, queryset, is_paginated = self.paginate_queryset(queryset, self.paginate_by)

        context = {
            'count': paginator.count,
            'total_pages': paginator.num_pages,
            'prev': page.previous_page_number() if page.has_previous() else None,
            'next': page.next_page_number() if page.has_next() else None,
            'results': list(queryset),
        }
        return context


class MoviesDetailApi(MoviesApiMixin, DetailView):
    def get_queryset(self):
        queryset = super().get_queryset().filter(id=self.kwargs[self.pk_url_kwarg])
        if queryset is None:
            raise HttpResponseNotFound
        return queryset

    def get_context_data(self, **kwargs):
        context = self.get_queryset().values(
            'id', 'title', 'description', 'creation_date', 'rating', 'type', 'genres', 'actors', 'directors', 'writers'
        )
        return context[0]
