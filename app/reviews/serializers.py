from rest_framework import serializers

from movies.serializers import MovieSerializer
from reviews.validators import validate_grade
from tasks.celery import sleep_task
from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieSerializer

    class Meta:
        model = Review
        fields = ["grade", "movie"]

    def create(self, validated_data):
        review = Review.objects.create(**validated_data)
        sleep_task()
        return review

    def validate_grade(self, value):
        return validate_grade(value)


class ReviewPartialSerializer(serializers.Serializer):
    grade = serializers.FloatField()

    def validate_grade(self, value):
        return validate_grade(value)
