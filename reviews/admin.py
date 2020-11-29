from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import Review, Comment


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date')
    list_filter = ('title', 'author', 'pub_date')
    date_hierarchy = 'pub_date'
    empty_value_display = _('-empty-',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('review', 'text', 'pub_date')
    list_filter = ('review', 'author', 'pub_date')
    date_hierarchy = 'pub_date'
    empty_value_display = _('-empty-',)
