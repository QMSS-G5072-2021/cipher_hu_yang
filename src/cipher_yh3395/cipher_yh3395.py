def cipher(text, shift, encrypt=True):
     """
    Encrypt and decrypt letter text by using the Caesar cipher.

    Parameters
    ----------
    text : string
      A string only contains letters from alphabet
    shift : int
      A number that you wish to replace each original letter to the letter with that number of positions down the alphabet.
    encrypt: boolean
      A boolean value with true indicates encrypt the text and false indicates decrypt the text
    
    Returns
    -------
    string
      The encrypt or decrypt letter text.

    Examples
    --------
    >>> from cipher_yh3395 import cipher
    >>> cipher('abc', 1)
    'bcd'
    >>> cipher('bcd', 1, False)
    'abc
    """
        
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_text = ''
    for c in text:
        index = alphabet.find(c)
        if index == -1:
            new_text += c
        else:
            new_index = index + shift if encrypt == True else index - shift
            new_index %= len(alphabet)
            new_text += alphabet[new_index:new_index+1]
    return new_text

