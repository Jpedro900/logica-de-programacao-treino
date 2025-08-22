from desafios.desafio_002 import max_three

def test_max_three():
    assert max_three(1, 2, 3) == 3
    assert max_three(5, 5, 2) == 5
    assert max_three(-7, -1, -3) == -1
    assert max_three(9, 9, 9) == 9

