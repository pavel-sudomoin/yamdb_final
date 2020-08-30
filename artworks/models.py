from django.contrib.auth import get_user_model
from django.db import models

from .snippets.unique_slugify import unique_slugify


User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            unique_slugify(self, self.name)
        super(Category, self).save(*args, **kwargs)


class Genre(models.Model):
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            unique_slugify(self, self.name)
        super(Genre, self).save(*args, **kwargs)


class Title(models.Model):
    name = models.CharField(max_length=200)
    year = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    genre = models.ManyToManyField(
        Genre,
        related_name="titles",
        blank=True
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        related_name="titles",
        blank=True, null=True
    )

    class Meta:
        ordering = ['id']
