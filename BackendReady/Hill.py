from PIL import Image
import requests
from PIL import ImageOps
from IPython.display import display
import urllib.request
import numpy as np
from Utils import utils

def EncryptImage(key, url, failures):
    """
    Description
    -----------
    Given m(the dimension of the key matrix), the key(matrix) and a
    url of the image, it encrypts the image of the url using the key.
    Finally, the encrypted image is displayed and then saved in
    'result.pgm' file. 
    
    If the key is not valid after three times, it
    uses a valid random key generated.

    Parameters
    ----------
    key : 2-dimensional list or np.array ie [[1, 2], [5, 6]]
        The mxm matrix to use as a key in the Hill cipher
    url : string
        The url of the image to encrypt
    failures : int
        Number of times the user has entered an invalid key
    
    Returns
    -------
    2-dimensional list : The key used to encrypt the image
    """
    m = len(key)
    if failures == 3:
        key = utils.GetRandomInvertibleMatrix(256, m)
    elif utils.IsValidMatrix(key):
        return -1
    elif utils.ComputeInverseKey(256, key) == -1:
        return -1
    
    response = requests.get(url)
    urllib.request.urlretrieve(url,"image.jpg")
    img = Image.open("image.jpg")
    encryptedImg = img.convert("L")

    # Resize image as needed, the image width must be a multiple
    # of m
    if encryptedImg.width % m != 0:
        diff = m - (encryptedImg.width % m)
        encryptedImg = ImageOps.expand(encryptedImg, border=(0,0, diff, 0), fill = 0)
    
    # Iterate over each row of the image height taking at each step
    # m pixels to transform them into a new m pixels
    for y in range(0, encryptedImg.height):
        rowPixels = []
        for x in range(0, encryptedImg.width):
            if x % m == 0 and x > 0:
                # Transform the m pixels making the dot product between them and the
                # key matrix
                newRowPixels = list(np.dot(rowPixels, key))
                newRowPixels = [(i % 256) for i in newRowPixels]
                for i in range(x - m, x):
                    encryptedImg.putpixel((i,y), int(newRowPixels[i - (x-m)]))
                rowPixels = []
            
            rowPixels.append(encryptedImg.getpixel((x,y)))
    
    # Show the image and save it in a .pgm file
    #encryptedImg.show()
    encryptedImg.save("result.pgm")
    return key

def DecryptImage(decryptKey, imgPath):
    """
    Description
    -----------
    Given m(the dimension of the key matrix), the  decrypt key(the 
    inverse modulus 256 of the matrix used to encrypt) and the path
    of the image it decrypts the image in the path using the key
    and then displays it

    Parameters
    ----------
    decryptKey : 2-dimensional list or np.array
        The inverse modulus 256 of the matrix used to encrypt
    imgPath : string
        The path of the image to decrypt in the local host
    """

    if utils.IsValidMatrix(decryptKey) == -1:
        return -1

    m = len(decryptKey)
    img = Image.open(imgPath)
    decryptedImg = img

    # Iterate over each row of the image height taking at each step
    # m pixels to transform them into a new m pixels
    for y in range(0, decryptedImg.height):
        rowPixels = []
        for x in range(0, decryptedImg.width):
            if x % m == 0 and x > 0:
                # Transform the m pixels making the dot product between them and the
                # key matrix
                newRowPixels = list(np.dot(rowPixels, decryptKey))
                newRowPixels = [(int(i) % 256) for i in newRowPixels]
                for i in range(x - m, x):
                    decryptedImg.putpixel((i,y), int(newRowPixels[i - (x-m)]) % 256)
                rowPixels = []
            
            rowPixels.append(decryptedImg.getpixel((x,y)))
    
    #decryptedImg.show()
    decryptedImg.save("out.png")

def EncryptText(key, text, failures):
    """
    Description
    -----------
    Given m(the dimension of the key matrix), the key(matrix)
    and the text, it encrypts the text using the key and then
    returns it.

    If the user enters an invalid key three times, the function
    use a valid random key generated

    Parameters
    ----------
    key : 2-dimensional list or np.array
        The mxm matrix to use as a key in the Hill cipher
    text : string
        The text to encrypt. If the text length is not a m multiple
        it will add 'f' characters as needed to make it a m multiple
    failures : int
        The number of times the user has entered an invalid key
    
    Returns
    -------
    string : Encrypted text
    2-dimensional list : The key used to encrypt the text
    """
    m = len(key)

    if failures == 3:
        key = utils.GetRandomInvertibleMatrix(26, m)
    elif utils.IsValidMatrix(key):
        return -1
    elif utils.ComputeInverseKey(26, key) == -1:
        return -1
    
    text = utils.preProcessText(text)
    encryptedText = ""

    # Resize the text as needed, the text length must be a multiple
    # of m
    if len(text) % m != 0:
        diff = m - (len(text) % m)
        text += diff*"f"
    
    # Iterate over the text taking at each step m characters to transform
    # them into a new m characters
    rowCharacters = []
    for x in range(0, len(text) + 1):
        if x % m == 0 and x > 0:
            # Transform the m characters codes making the dot product between
            # them and the key matrix
            newRowCharacters = list(np.dot(rowCharacters, key))
            newRowCharacters = [(i % 26) for i in newRowCharacters]
            for i in range(x - m, x):
                encryptedText += utils.GetLetter(int(newRowCharacters[i - (x-m)]))
            rowCharacters = []
        
        if(x != len(text)):
            rowCharacters.append(utils.GetCode(text[x]))
    
    # Return the encrypted text
    return encryptedText, key

def DecryptText(decryptKey, text):
    """
    Description
    -----------
    Given m(the dimension of the key matrix), the decrpyt key(matrix)
    and the encrypted text, it decrypts the text using the decrypt key
    and then returns it

    Parameters
    ----------
    key : 2-dimensional list or np.array
        The mxm matrix to use as a a decrypt key in the Hill cipher
    text : string
        The text to decrypt, it must be of length m
    """

    try:
        utils.IsValidMatrix(decryptKey)
    except:
        return -1

    m = len(decryptKey)
    decryptedText = ""
    
    # Iterate over the text taking at each step m characters to transform
    # them into a new m characters
    rowCharacters = []
    for x in range(0, len(text) + 1):
        if x % m == 0 and x > 0:
            # Transform the m characters codes making the dot product between
            # them and the key matrix
            newRowCharacters = list(np.dot(rowCharacters, decryptKey))
            newRowCharacters = [(i % 26) for i in newRowCharacters]
            for i in range(x - m, x):
                decryptedText += utils.GetLetter(int(newRowCharacters[i - (x-m)]))
            rowCharacters = []
        
        if(x != len(text)):
            rowCharacters.append(utils.GetCode(text[x]))
    
    # Return the encrypted text
    return decryptedText