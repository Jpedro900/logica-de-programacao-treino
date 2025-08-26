from desafios.desafio_007 import remove_vowels

def test_remove_vowels():
    assert remove_vowels("abcde") == "bcd"
    assert remove_vowels("PYTHON") == "PYTHN"
    assert remove_vowels("") == ""
    assert remove_vowels("Programacao") == "Prgrmc"
