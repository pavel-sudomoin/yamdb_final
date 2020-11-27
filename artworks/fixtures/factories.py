import factory
from slugify import slugify

from artworks.models import Category, Genre, Title

factory.Faker._DEFAULT_LOCALE = 'ru_RU'


class CategoriesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('bs')
    slug = factory.LazyAttribute(lambda o: slugify(o.name))


class GenresFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Genre

    name = factory.Faker('job')
    slug = factory.LazyAttribute(lambda o: slugify(o.name))


class TitleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Title

    name = factory.Sequence(lambda n: 'Artwork #%s' % n)
    year = factory.Iterator((2000, 2001, 2010, 2020))
    description = factory.Faker('text')
    category = factory.Iterator(Category.objects.all())

    @factory.post_generation
    def genre(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of users were passed in, use them
            for genre in extracted:
                self.genre.add(genre)
