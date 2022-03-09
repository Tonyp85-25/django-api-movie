from rest_framework import serializers


def validate_grade(review):
    """Checks if a grade is between 0 and 5"""
    if review.grade < 0 or review.grade > 5:
        raise serializers.ValidationError("grade must be between 0 and 5.")
