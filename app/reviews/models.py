from django.db import models

from movies.models import Movie
from .validators import validate_grade


class Review(models.Model):
    grade = models.FloatField(validators=[validate_grade])
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)




