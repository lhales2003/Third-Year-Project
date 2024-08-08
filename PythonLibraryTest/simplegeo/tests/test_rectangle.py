from simplegeo import rectangle

def test_rectangle_area():
    result = rectangle.rectangle_area(5, 6)
    expected_result = 30
    assert result == expected_result

def test_rectangle_perimeter():
    result = rectangle.rectangle_perimeter(3, 4)
    expected_result = 14
    assert result == expected_result