from desafios.desafio_004 import reverse_str

def test_reverse_str():
    assert reverse_str("abc") == "cba"
    assert reverse_str("a") == "a"
    assert reverse_str("") == ""
    assert reverse_str("python") == "nohtyp"
