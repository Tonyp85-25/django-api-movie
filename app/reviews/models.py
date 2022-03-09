from django.db import models

from movies.models import Movie


class Review(models.Model):
    grade = models.FloatField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
