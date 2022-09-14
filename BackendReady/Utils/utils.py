import random
import string
import numpy as np

def GetCode(c):
    """
    Description
    -----------
    Using the correspondence a <-> 0, b <-> 1, ... , z <-> 25
    we associate to each character its corresponding numeric
    value.

    This function returns the corresponding numeric value 
    associated with the given character, according to the
    scheme described above.
    """
    return ord(c) - 97

def GetLetter(n):
    """
    Description
    -----------
    Using the correspondence a <-> 0, b <-> 1, ... , z <-> 25
    we associate to each character its corresponding numeric
    value.

    This function returns the corresponding letter asociated
    with the given value, according to the scheme described 
    above.
    """
    return chr(n + 97)

def GetRandomInteger(n):
    """
    Description
    -----------
    This function returns a random integer from 1 to n inclusive
    """
    return random.randint(1, n)

def GetRandomString(n):
    """
    Description
    -----------
    This function returns a random string of length n in lower
    case with letters from a to z
    """
    # choose from all lowercase letter
    letters = string.ascii_lowercase
    randomString = ''.join(random.choice(letters) for i in range(n))
    return randomString

def preProcessText(text):
    """
    Description
    -----------
    This function returns the given text in lowercase without
    spaces and not english alphabet characters.
    """
    text = text.replace(' ', '')
    text = text.lower()
    processedText = ""
    for c in text:
        if ord(c) >= 97 and ord(c) <= 97 + 25:
            processedText += c
    return processedText

def IsValidMatrix(m):
    if len(m) != len(m[0]):
        return -1

def GetRandomInvertibleMatrix(n, m):
    """
    Description
    -----------
    Generate random invertible mxm matrix modulus n
    
    Parameters
    ----------
    n : int
        Modulus being used
    m : int
        Size of the square matrix to obtain
    """
    matrix = np.random.randint(1, 100, size=(m, m))
    while ComputeInverseKey(n, matrix) != -1:
        matrix = np.random.randint(1,100,size=(m, m))
    return matrix

def Round(l):
    """
    Description
    -----------
    Returns a new list where each element is rounded

    Parameters
    ----------
    l : list
        The list to apply the round function

    Returns
    -------
    A new list with each entry rounded
    """
    result = []
    for i in l:
        result.append(int(round(i)))
    return result

def adjoint_matrix(matrix):
    """
    Description
    -----------
    Tries to compute the adjoint matrix of the given
    matrix as long as its determinant is not zero. If
    the matrix is invertible, it returns its adjoint
    matrix

    Parameters
    ----------
    matrix : 2-dimensional list or np.array
        The matrix to find the adjoint matrix
    
    Returns
    -------
    A new two 2-dimensional list or np.array
    """
    try:
        determinant = np.linalg.det(matrix)
        if(determinant!=0):
            cofactor = None
            cofactor = np.linalg.inv(matrix).T * determinant
            # return cofactor matrix of the given matrix
            return cofactor.transpose()
        else:
            raise Exception("singular matrix")
    except Exception as e:
        print("could not find cofactor matrix due to",e)

def gcdExtended(a, b):
    """
    Description
    -----------
    From number theory we have ax + by = gcd(a, b). This function
    finds the value of x,y and the gcd, given a, b, and returns
    them

    Parameters
    ----------
    a: int
        First number to get the gcd
    b: int
        Second number to get the gcd
    
    Returns
    -------
    gcd : int
        The gcd(a,b)
    x : int
        The coefficient of a in the formula ax + by = gcd(a,b)
    y : int
        The coefficient of b in the formula ax + by = gcd(a,b)
    """
    # Base Case
    if a == 0 :
        return b,0,1
             
    gcd,x1,y1 = gcdExtended(b%a, a)
     
    # Update x and y using results of recursive
    # call
    x = y1 - (b//a) * x1
    y = x1
    
    return gcd,x,y

def ComputeInverseKey(n, key):
    """
    Description
    -----------
    Computes the inverse matrix of the mxm key matrix modulus n
    and then returns it.

    Parameters
    ----------
    n : int
        The modulus to find the inverse matrix
    key : 2-dimensional list or np.array
        The matrix to find the inverse modulus n
    
    Returns
    -------
    If the matrix is invertible modulus n returns the inverse. Otherwise
    it returns -1
    """
    try:
        IsValidMatrix(key)
    except:
        return -1
    
    m = len(key)
    mod = m*[m*[n]]

    # Compute Adjoint matrix of the key modulus n
    adjoint = adjoint_matrix(key)
    adjoint = np.mod(adjoint, mod)

    # Compute the inverse of the determinant of the key
    # modulus n
    det = round(np.linalg.det(key)) % n
    gcd, inverseDet, y = gcdExtended(det,n)

    # Check whether or not the given matrix is inversible
    # modulus n
    if gcd == 1:

        # Compute the inverse matrix of the key modulus n
        # In the same way, round the entries of the resulting
        # matrix
        inverse = np.dot(inverseDet, adjoint)
        inverse = np.mod(inverse, mod)
        inverse = [Round(x) for x in inverse]

        return inverse
    else:
        return -1