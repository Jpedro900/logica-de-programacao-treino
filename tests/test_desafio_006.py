from desafios.desafio_006 import count_vowels

def test_count_vowels():
    assert count_vowels("abcde") == 2
    assert count_vowels("PYTHON") == 1
    assert count_vowels("") == 0
    assert count_vowels("Programacao") == 6
