from fibonacci import fibonacci

def test_fibonacci_sequence():
    assert fibonacci(0) == []
    assert fibonacci(1) == [1]
    assert fibonacci(2) == [1, 2]
    assert fibonacci(5) == [1, 2, 3, 5, 8]
    assert fibonacci(10) == [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]