import random as ran
from math import gcd as bltin_gcd
import re





#///////////////////////////////////////////////////////////////
#//////////////////////FUNCIONES GENERALES///////////////////
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
  print(palabra)
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



#///////////////////////////////////////////////////////////////
#//////////////////////METODOS DE CODIFICACION///////////////////
#////////////////////////////////////////////////////////////////

####LIMPIO
def encode_despla(palabrast,key,count_falla):
  palabrals = unify(palabrast)
  if count_falla > 2:
    key = ran.randint(1,26)
    palabrals = convert(palabrals)
    for i in range(len(palabrals)):
      palabrals[i] = (palabrals[i] + key)%26
    palabrast = deconvert(palabrals)
    print(palabrast)
    return palabrast
  if 1 <= key <= 26:
      palabrals = convert(palabrals)
      for i in range(len(palabrals)):
        palabrals[i] = (palabrals[i] + key)%26
      palabrast = deconvert(palabrals)
      print(palabrast)
      return palabrast
  else:
    return -1
  

####LIMPIO
def encode_mult(palabrast,key,count_falla):
  palabrals = unify(palabrast)
  claves_validas = rela_primes()
  if count_falla > 2:
    key = claves_validas[ran.randint(1,len(claves_validas))]
    palabrals = convert(palabrals)
    for i in range(len(palabrals)):
      palabrals[i] = (palabrals[i] * key)%26
    palabrast = deconvert(palabrals)
    return palabrast
  if key in claves_validas:
      palabrals = convert(palabrals)
      for i in range(len(palabrals)):
        palabrals[i] = (palabrals[i] * key)%26
      palabrast = deconvert(palabrals)
      return palabrast
  else:
    return -1

###### toca pensarlo mucho mejor, la idea es que la codificacion entre
###### completa, las 26 keys.
def encode_sust(palabrast,key,count_falla):
  dic = {'a':"", 'b':"", 'c':"", 'd':"", 'e':"", 'f':"", 'g':"", 'h':"", 'i':"", 'j':"", 'k':"", 'l':"",'m':"", 'n':"", 'o':"", 'p':"", 'q':"", 'r':"", 's':"", 't':"", 'u':"", 'v':"", 'w':"", 'x':"", 'y':"", 'z':""}
  lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  palabrals = unify(palabrast)
  count = 0
  if count_falla > 2:
    listaran = lista[:]
    ran.shuffle(listaran)
    for item in listaran:
      if item not in dic.values():
        dic[lista[count]] = item
  for item in key:
    if item not in lista:
      return -1
    else:
      if item not in dic.values():
        dic[lista[count]] = item
        count = count + 1
      else:
        return -1  
  string = ""
  for i in range(len(palabrals)):
    palabrals[i] = dic[palabrals[i]]
    string = string + palabrals[i]
  return string


####LIMPIO
def encode_afin(palabrast, a, b, count_falla):
  palabrals = unify(palabrast)
  claves_validas = rela_primes()
  if count_falla > 2:
    a = claves_validas[ran.randint(1,len(claves_validas))]
    b = ran.randint(1,25)
    palabrals = convert(palabrals)
    for i in range(len(palabrals)):
      palabrals[i] = (((palabrals[i] * a)%26)+b)%26
    palabrast = deconvert(palabrals)
    return palabrast
  if a in claves_validas:
    if 1 <= b <= 25:
      palabrals = convert(palabrals)
      for i in range(len(palabrals)):
        palabrals[i] = (((palabrals[i] * a)%26)+b)%26
      palabrast = deconvert(palabrals)
      return palabrast
    else:
      return -1 
  else:
    return -1

####LIMPIO
def encode_permu(string, tama, key, count_falla):
  palabrals = unify(string)
  while True:
    if 1 <= tama <=len(palabrals):
      break
    return -1
  while True:
    if 1<= key < tama:
      break
    return -1
  chunks = [palabrals[x:x+tama] for x in range(0, len(palabrals), tama)]
  final=[]
  for x in chunks:
    test = []
    for i in range(key):
      test.append(x[(len(x)-(key-i))%len(x)])
      if(i>=len(x)-1):
        break
    for i in range(len(x)-key):
      test.append(x[i])
    final.extend(test)
  final = convert(final)
  final = deconvert(final)
  return final
#///////////////////////////////////////////////////////////////
#//////////////////////METODOS DE DECODIFICACION///////////////////
#////////////////////////////////////////////////////////////////
#### LIMPIO
####mbwjebftnvzmjoeb
####xmhupmqegzmoaeufmxuzpm (12)
def decode_despla(string, key, count_fallas):
  if 1<= key<=26:
    lista = unify(string)
    lista = convert(lista)
    for j in range(len(lista)):
      lista[j] = (lista[j]-key)%26
    string = deconvert(lista)
    print(string)
    return string
  for i in range(25):
    lista = unify(string)
    lista = convert(lista)
    for j in range(len(lista)):
      lista[j] = (lista[j]+1)%26
    string = deconvert(lista)
  return string



##### LIMPIO
#lavidaesmuylinda
#sqbasqmnalmsnajaralfajafasnwfkjbaf (11) 
######### existe algo raro con el 11, arreglar
##qeaxgoxabaxxagngojgsgnoahg (21)
def decode_mult(string, key, count_fallas):
  inver_validas = inver_primes()
  keys = rela_primes()
  if key in keys:
    lista = unify(string)
    lista = convert(lista)
    for i in range(len(keys)):
      if keys[i] == key:
        key = inver_validas[i]
    for j in range(len(lista)):  
      lista[j] = int((lista[j]*key)%26)
    string = deconvert(lista)
    return string
  for i in inver_validas:
    lista = unify(string)
    lista = convert(lista)
    for j in range(len(lista)):
      lista[j] = int((lista[j]*i)%26)
    res = deconvert(lista)
  return res

#LIMPIO
def decode_sust(palabrast,key,count_falla):
  dic = {'a':"", 'b':"", 'c':"", 'd':"", 'e':"", 'f':"", 'g':"", 'h':"", 'i':"", 'j':"", 'k':"", 'l':"",'m':"", 'n':"", 'o':"", 'p':"", 'q':"", 'r':"", 's':"", 't':"", 'u':"", 'v':"", 'w':"", 'x':"", 'y':"", 'z':""}
  lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  palabrals = unify(palabrast)
  count = 0
  if count_falla > 2:
    listaran = lista[:]
    ran.shuffle(listaran)
    for item in listaran:
      if item not in dic.values():
        dic[lista[count]] = item
  for item in key:
    if item not in lista:
      return -1
    else:
      if item not in dic.values():
        dic[lista[count]] = item
        count = count + 1
      else:
        return -1  
  string = ""
  for i in range(len(palabrals)):
    palabrals[i] = dic[palabrals[i]]
    string = string + palabrals[i]
  return string
  
  
#####  PENSAR MEJOR COMO GENERAR ESTO EN UNA SOLA
## la vida es hermosa
##tulypuwqrwjaoqu (7,20)
##xuvijuogdobcmgu (5,20)
def decode_afin(string):
  alf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  lista = unify(string)
  claves_validas = rela_primes()
  inversas_validas = inver_primes()
  print("tiene usted la clave? (Y/n)")
  res = input()
  if res == "Y":
    flag = True
    while flag == True:
      print("ingrese 'a': ")
      a = int(input())
      for i in range(len(claves_validas)):
        if claves_validas[i] == a:
          ai = inversas_validas[i]
      print("ingrese 'b': ")
      b = int(input())
      if a in claves_validas:
        if 1 <= b <= 25:
          palabrals = convert(lista)
          for i in range(len(palabrals)):
            palabrals[i] = (((palabrals[i] - b)%26)*ai)%26
          palabrast = deconvert(palabrals)
          print(palabrast)
          return palabrast
        else:
          print("ingrese nuevamente la clave")
      else:
        print("ingrese nuevamente la clave")
    
  else:
    dic={}
    for item in lista:
      if item not in dic.keys():
        dic[item] = 1
      else:
        dic[item] = dic[item]+1
    dic = dict(sorted(dic.items(), key=lambda item: item[1], reverse = True))
    print("Se ha realizado el siguiente conteo, basado en esto, como desea mapear?")
    print(dic)
    flag = True
    while flag == True:
      print("Como primera letra, cual letra desea mapear. (sugerimos las letras con mayor frecuencias en el alfabeto ingles 'e','t','a','o','n')")
      e = input()
      print("Cual letra cree que mapea a '{}'?".format(e))
      ei = input()
      print("Como segunda letra, cual letra desea mapear. (sugerimos las letras con mayor frecuencias en el alfabeto ingles 'e','t','a','o','n')")
      t = input()
      print("Cual letra cree que mapea a '{}'?".format(t))
      ti = input()
      for i in range(len(alf)):
        if alf[i] == e:
          e = i
        if alf[i] == ei:
          ei = i 
        if alf[i] == t:
          t = i
        if alf[i] == ti:
          ti = i
      a = e - t
      c = ei - ti
      signoa = a/abs(a)
      signoc = c/abs(c)
      print(e,ei,t,ti,a,c,signoa,signoc)
      if abs(a) not in claves_validas:
        print("intentelo nuevamente")
      else:
        for i in range(len(claves_validas)):
          if claves_validas[i] == abs(a):
            a = inversas_validas[i]
        lista = unify(string)
        ares = ((signoa*abs(a))*c)%26
        bres = (ei-(e * ares)%26)%26
        print("estos son a = {} y b = {}".format(ares,bres))
        palabrals = convert(lista)
        for i in range(len(claves_validas)):
          if claves_validas[i] == abs(ares):
            ares = inversas_validas[i]
            break
        for i in range(len(palabrals)):
          palabrals[i] = ((palabrals[i] - bres)*ares)%26
        palabrast = deconvert(palabrals)
        print(palabrast)
        return palabrast


#### LIMPIO
#Este metodo es para no tener que escribir lo mismo dos veces en decode_permu
def permufiesta(palabra,m,l):
  chunks = [palabra[x:x+m] for x in range(0, len(palabra), m)]
  final=[]
  for x in chunks:
    test = []
    for i in range(l,len(x)):
      test.append(x[i])
    for i in range(l):
      test.append(x[i])
      if(i>=len(x)-1):
        break
    final.extend(test)
  final = convert(final)
  final = deconvert(final)
  return final

#### LIMPIO
def decode_permu(string, tama, key, count_falla):
  palabra = unify(string)
  if count_falla > 2:
    final = []
    for i in range(1,len(palabra)+1):
      final.append(permufiesta(palabra,i))
    return final
  if 1 <= tama <= len(palabra):
    if 1 <= key < tama:
      return permufiesta(palabra,tama,key)
    else:
      return -1
  else:
    return -1
    
#////////////////////////////////////////////////////////////////
#//////////////////////CUERPO PRINCIPAL///////////////////
#////////////////////////////////////////////////////////////////

    
print("elija entre las siguietnes opciones:\nEncriptar: 1 \nDesencriptar: 2")
opcion = int(input())
if opcion == 1:
  while True:
    print("cual es la palabra que desea encriptar? (al menos un caracter, todo en minuscula")
    palabra = input()
    if len(palabra) > 1:
      break
  print("Cual metodo de encriptacion desea?\nDesplazamiento: 1\nMultiplicacion: 2\nSustitucion: 3\nAfin: 4\nPermutación: 5")
  opcion = int(input())
  if opcion == 1:
    encode_despla(palabra)
  elif opcion == 2:
    encode_mult(palabra)
  elif opcion == 3:
    encode_sust(palabra)
  elif opcion == 4:
    encode_afin(palabra)
  else:
    encode_permu(palabra)
else:
  print("cual es la palabra que desea desencriptar?")
  palabra = input()
  print("cual cree que fue el metodo de encriptacion?\nDesplazamiento: 1\nMultiplicacion: 2\nAfin: 3\nPermutación: 4")
  opcion = int(input())
  if opcion == 1:
    decode_despla(palabra)
  elif opcion == 2:
    decode_mult(palabra)
  elif opcion == 3:
    decode_afin(palabra)
  else:
    decode_permu(palabra)