from rest_framework import viewsets
from reviews.serializers import ReviewSerializer

from reviews.models import Review


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
