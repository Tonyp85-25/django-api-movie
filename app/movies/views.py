from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from reviews.utils import calculate_mean_review
from reviews.models import Review
from rest_framework.response import Response
from rest_framework.decorators import action

from movies.models import Movie
from movies.serializers import MovieSerializer
from tasks.celery import sleep_task
from reviews.serializers import ReviewPartialSerializer

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

    @action(detail=True,methods=['post'])
    def review(self, request, pk=None):
        queryset = Movie.objects.all()
        movie = get_object_or_404(queryset, pk=pk)
        serializer = ReviewPartialSerializer(data=request.data)
        if serializer.is_valid():
            review = Review.objects.create(grade=serializer.validated_data['grade'],movie= movie )
            sleep_task()
            review.save()
            return Response({'status':'review added'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)



