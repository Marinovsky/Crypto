
from math import gcd as bltin_gcd
import re

#///////////////////////////////////////////////////////////////
#//////////////////////FUNCIONES UTILES///////////////////
#////////////////////////////////////////////////////////////////

def rela_primes():
  lista = []
  for i in range(26): 
    if bltin_gcd(26, i) == 1:
      lista.append(i)
  return lista 



def inver_primes():
  lista_primes = rela_primes()
  lista_inver = []
  for i in lista_primes:
    for j in range(30):
      if (i*j)%26 == 1:
        lista_inver.append(j)
        break
  return lista_inver

 
## agregar ignorar lo que no sean letras y pasar las mayus a minus 

def unify(palabra):
  palabralist = []
  palabra = palabra.replace(" ", "")
  palabra = palabra.lower()
  regex = re.compile('[^a-z]')
  palabra = regex.sub('', palabra)
  for i in range(len(palabra)):
    palabralist.append(palabra[i])
  return palabralist
  

  
def convert (list):
  lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  count = 0
  for i in list:
    for j in range(len(lista)):
      if i == lista[j]:
        list[count]= j
        continue

    count = count + 1
  return list

  
def deconvert(list):
  lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  string = ""
  for i in range(len(list)):
    list[i] = lista[int(list[i])]
    string = string + list[i]
  return string
