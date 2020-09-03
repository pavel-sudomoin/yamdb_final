import factory
from django.contrib.auth import get_user_model

from users.models import UsersRoles

User = get_user_model()
factory.Faker._DEFAULT_LOCALE = 'ru_RU'


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    username = factory.Sequence(lambda n: 'user%s' % n)
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
    bio = factory.Faker('text')
    role = factory.Iterator(UsersRoles.values)
