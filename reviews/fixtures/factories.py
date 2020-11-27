import factory
from django.contrib.auth import get_user_model
import random

from artworks.models import Title
from reviews.models import Comment, Review

User = get_user_model()
factory.Faker._DEFAULT_LOCALE = 'ru_RU'


class CommentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Comment

    text = factory.Faker('text', max_nb_chars=350)
    author = factory.Iterator(User.objects.all())


class ReviewFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Review

    text = factory.Faker('text', max_nb_chars=550)
    author = factory.Iterator(User.objects.all())
    comments = factory.RelatedFactoryList(
        CommentFactory, 'review', size=random.randint(5, 35)
    )
    title = factory.Iterator(Title.objects.all())
    score = factory.Iterator(range(1, 11))
