import pytest

# @pytest.mark.smoke
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi", "Test failed because strings do not match"

def test_secondProgram():
    a = 4
    b = 6
    assert a+2 == 6, "Test failed because expression do not match"

def test_thirdProgram():
    a = 5
    b = 6
    assert a+1 == 6, "Test failed because expression do not match"

