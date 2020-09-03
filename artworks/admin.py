from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Category, Genre, Title


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')
    search_fields = ('name', 'slug')
    list_filter = ('name',)
    empty_value_display = _('-empty-',)
    ordering = ('pk',)


class GenreAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'slug')
    search_fields = ('name', 'slug')
    list_filter = ('name',)
    empty_value_display = _('-empty-',)
    ordering = ('pk',)


class TitleAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'description', 'category', 'show_genres')
    search_fields = ('name', 'year', 'description')
    list_filter = ('year', 'genre', 'category')
    empty_value_display = _('-empty-',)
    ordering = ('name',)

    def show_genres(self, obj):
        return ", ".join([g.name for g in obj.genre.all()])

admin.site.register(Category, CategoryAdmin)
admin.site.register(Genre, GenreAdmin)
admin.site.register(Title, TitleAdmin)
