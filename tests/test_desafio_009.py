from desafios.desafio_009 import fibonacci

def test_fibonacci():
    assert fibonacci(0) == []
    assert fibonacci(1) == [0]
    assert fibonacci(2) == [0, 1]
    assert fibonacci(6) == [0, 1, 1, 2, 3, 5]
