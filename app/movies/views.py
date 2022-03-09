from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from reviews.utils import calculate_mean_review
from reviews.models import Review
from rest_framework.response import Response

from movies.models import Movie
from movies.serializers import MovieSerializer


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


# Create your views here.
