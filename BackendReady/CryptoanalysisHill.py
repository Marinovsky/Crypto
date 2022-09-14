import numpy as np
from Utils import utils
from Hill import DecryptText

def GuessKey(x, y, n):
    """
    Description
    -----------
    Given square matrices x and y where the x i-th row it's
    supposed to be mapped to the y i-th row using the key we
    are looking for, it tries to return that key, at least if
    the x matrix is invertible modulus n

    Parameters
    ----------
    x : 2-dimensional array or np.array ei. [[1,2], [5, 6]]
        The matrix where the rows are the values for which is
        supposed to be known its product after apply the key
    y : 2-dimensional array or np.array ie. [[4,5],[11, 9]]
        The matrix where the i-th row is the result after
        multiply x by the key
    n : int
        The modulus to use in all the operations
    
    Returns
    -------
    If the x matrix is invertible modulus n, it will return the
    key which is the product of x^-1*y. Otherwise, it will return
    -1
    """
    m = len(x)
    inverse = utils.ComputeInverseKey(n, x)
    if inverse != -1:
        key = np.dot(inverse, y)
        mod = m*[m*[n]]
        key = np.mod(key, mod)
        return key
    else:
        return -1

def GuessText(x, y, encryptedText):
    """
    Description
    -----------
    Tries to decrypt the encrypted text using the plain-text pairs
    x and y where the x i-th row it's supposed to be mapped to the
    y i-th row using the key we are looking for, it tries to return
    that key, at least if the x matrix is invertible modulus n

    Parameters
    ----------
    x : 2-dimensional array or np.array ei. [[1,2], [5, 6]]
        The matrix where the rows are the values for which is
        supposed to be known its product after apply the key
    y : 2-dimensional array or np.array ie. [[4,5],[11, 9]]
        The matrix where the i-th row is the result after
        multiply x by the key
    encryptedText : string
        The text to decrypt
    
    Returns
    -------
    string : The a potential decryption of the encrypted text
    """
    key = GuessKey(x, y, 26)
    inverseKey = utils.ComputeInverseKey(26, key)
    return DecryptText(inverseKey, encryptedText)