import random

import factory

from .models import Review
from  movies.factory import MovieFactory


def calculate_mean_review(reviews):
    """calculate the mean review for one movie"""
    mean = 0
    for review in reviews:
        mean += float(review.grade)
    return mean / len(reviews)



class ReviewFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Review
    grade = random.randint(0,5)
    movie = MovieFactory.build()
