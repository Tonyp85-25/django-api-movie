import pytest
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


