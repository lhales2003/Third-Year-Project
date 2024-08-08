import math

from simplegeo import circle

def test_circle_area():
    result = circle.circle_area(5)
    expected_result = math.pi * 25
    assert result == expected_result

def test_circle_circumference():
    result = circle.circle_circumference(4)
    expected_result = math.pi * 8
    assert result == expected_result