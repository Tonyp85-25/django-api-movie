import factory
import pytest

from .serializers import ReviewSerializer
from .utils import calculate_mean_review, ReviewFactory
from .validators import validate_grade
from rest_framework.serializers import ValidationError
# Create your tests here.

@pytest.fixture
def right_grade():
    yield range(6)

@pytest.fixture
def wrong_grade():
    return [-1, 6, 7, -5, 15]

class TestValidateGrade:

    @pytest.mark.unit
    def test_validate_grade_right(self, right_grade):
        grades = [validate_grade(x) for  x in right_grade]
        assert grades == list(right_grade)

    @pytest.mark.unit
    def test_validate_grade_false(self,wrong_grade):
     
        with pytest.raises(ValidationError,match="grade must be between 0 and 5.") as val_err:
           errs = [validate_grade(x) for x in wrong_grade]


class MockReview:
    grade =3

@pytest.fixture()
def reviews():
    reviews =[MockReview for x in range(3)]
    return reviews


class TestCalculateMeanReview:

    def test_calculation(self,reviews):
      result = calculate_mean_review(reviews)
      assert result == 3

class TestReviewSerializer:

    @pytest.mark.unit
    def test_serialize_model(self):
        review = ReviewFactory.build()
        serializer = ReviewSerializer(review)

        assert serializer.data

    @pytest.mark.unit
    def test_serialized_data(self):
        valid_serialized_data = factory.build(
            dict,
            FACTORY_CLASS=ReviewFactory
        )

        serializer = ReviewSerializer(data=valid_serialized_data)

        assert serializer.is_valid()
        # assert serializer.errors == {}