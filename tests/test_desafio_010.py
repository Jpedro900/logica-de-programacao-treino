from desafios.desafio_010 import is_anagram

def test_is_anagram():
    assert is_anagram("amor", "roma") is True
    assert is_anagram("Amor", "Roma") is True
    assert is_anagram("python", "typhon") is True
    assert is_anagram("banana", "ananab") is True
    assert is_anagram("abc", "abcc") is False
    assert is_anagram("oi", "oi ") is True  # ignora espaço
