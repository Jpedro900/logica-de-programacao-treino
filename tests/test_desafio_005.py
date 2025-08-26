from desafios.desafio_005 import is_palindrome

def test_is_palindrome():
    assert is_palindrome("ana") is True
    assert is_palindrome("abc") is False
    assert is_palindrome("") is True
    assert is_palindrome("a") is True
    assert is_palindrome("radar") is True
    assert is_palindrome("python") is False
