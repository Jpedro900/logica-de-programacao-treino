from desafios.desafio_003 import count_evens

def test_count_evens():
    assert count_evens([1,2,3,4]) == 2
    assert count_evens([]) == 0
    assert count_evens([2,2,2]) == 3
    assert count_evens([1,3,5]) == 0
    assert count_evens([-2,0,7]) == 2
