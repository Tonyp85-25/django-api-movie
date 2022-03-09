from rest_framework import serializers

from movies.serializers import MovieSerializer
from reviews.validators import validate_grade
from tasks.celery import sleep_task
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    movie = serializers.StringRelatedField()

    class Meta:
        model = Review
        fields = ["grade", "movie"]

    def create(self, validated_data):
        movie_data = validated_data.pop("movie")
        review = Review.objects.create(**validated_data)
        validate_grade(review)
        sleep_task()
        return review
