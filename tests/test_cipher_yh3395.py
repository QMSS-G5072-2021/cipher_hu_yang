from cipher_yh3395.cipher_yh3395 import cipher

def test_cipher_negshift():
    example = 'Lisa'
    expected = 'KhrZ'
    actual = cipher('Lisa',-1)
    assert actual == expected