import random

import factory

from .models import Review


def calculate_mean_review(reviews):
    """calculate the mean review for one movie"""
    mean = 0
    for review in reviews:
        mean += float(review.grade)
    return mean / len(reviews)

class MockMovie :

    def __init__(self,title):
        self.title = title

class ReviewFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Review
    grade = random.randint(0,5)
    movie = MockMovie(title='movie')
