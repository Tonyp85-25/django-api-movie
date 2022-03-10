from rest_framework import serializers


def validate_grade(grade):
    """Checks if a grade is between 0 and 5"""
    if grade < 0 or grade > 5:
        raise serializers.ValidationError("grade must be between 0 and 5.")
    else :
        return grade
