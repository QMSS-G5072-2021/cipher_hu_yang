from cipher_yh3395.src.cipher_yh3395 import cipher_yh3395

def test_cipher_negshift():
    example = 'Lisa'
    expected = 'KhrZ'
    actual = cipher('Lisa',-1)
    assert actual == expected