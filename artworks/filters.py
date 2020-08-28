import django_filters

from .models import Category, Genre, Title


class TitleFilter(django_filters.FilterSet):
    genre = django_filters.ModelChoiceFilter(
        field_name="genre__slug",
        to_field_name='slug',
        queryset=Genre.objects.all()
    )

    category = django_filters.ModelChoiceFilter(
        field_name="category__slug",
        to_field_name='slug',
        queryset=Category.objects.all()
    )

    class Meta:
        model = Title
        fields = ('genre','category','name','year')
