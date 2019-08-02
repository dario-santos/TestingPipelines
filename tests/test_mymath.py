import pytest
from MyCode.mymath import Sub


def test_sub():
     assert Sub(5, 3) == 2

def test_raises_exception_on_non_string_arguments():
     with pytest.raises(TypeError):
          Sub('2', '1')