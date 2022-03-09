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

    def retrieve(self, request, pk=None):
        queryset = Movie.objects.all()
        movie = get_object_or_404(queryset, pk=pk)
        serializer = MovieSerializer(movie)
        data = serializer.data
        reviews = Review.objects.filter(id=movie.id)
        data["mean_review"] = calculate_mean_review(reviews)
        return Response(data)
