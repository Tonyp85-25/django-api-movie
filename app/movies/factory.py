import factory

from .models import Movie


class MovieFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Movie
    title = factory.faker.Faker('domain_name')
    description = factory.faker.Faker('sentence')