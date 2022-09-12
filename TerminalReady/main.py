import random as ran
from Utilities import utilities


#///////////////////////////////////////////////////////////////
#//////////////////////METODOS DE CODIFICACION///////////////////
#////////////////////////////////////////////////////////////////

def encode_despla(palabrast):
  palabrals = utilities.unify(palabrast)
  
  for count_falla in range(4):
    if count_falla > 2:
      clave = ran.randint(1,26)
      print("Al usar todos los intentos, hemos elegido una clave por usted. La clave sera: {}.".format(clave))
      palabrals = utilities.convert(palabrals)
      for i in range(len(palabrals)):
        palabrals[i] = (palabrals[i] + clave)%26
      palabrast = utilities.deconvert(palabrals)
      print(palabrast)
      return palabrast
    print("ingrese una clave entre 1 y 26. \n numero de intento: {}, tiene 3 intentos.".format(count_falla+1))
    clave = int(input())
    if 1 <= clave <= 26:
        palabrals = utilities.convert(palabrals)
        for i in range(len(palabrals)):
          palabrals[i] = (palabrals[i] + clave)%26
        palabrast = utilities.deconvert(palabrals)
        print(palabrast)
        return palabrast
    else:
      print("clave ilegal")
  

def encode_mult(palabrast):
  
  palabrals = utilities.unify(palabrast)
  claves_validas = utilities.rela_primes()
  for count_falla in range(4):
    if count_falla > 2:
      clave = claves_validas[ran.randint(1,len(claves_validas))]
      print("Al usar todos los intentos, hemos elegido una clave por usted. La clave sera: {}.".format(clave))
      palabrals = utilities.convert(palabrals)
      for i in range(len(palabrals)):
        palabrals[i] = (palabrals[i] * clave)%26
      palabrast = utilities.deconvert(palabrals)
      print(palabrast)
      return palabrast
    print("ingrese una clave que pertenezca a la lista {}. \nNumero de intento: {}, tiene 3 intentos.".format(claves_validas, count_falla+1))
    clave = int(input())
    if clave in claves_validas:
        palabrals = utilities.convert(palabrals)
        for i in range(len(palabrals)):
          palabrals[i] = (palabrals[i] * clave)%26
        palabrast = utilities.deconvert(palabrals)
        print(palabrast)
        return palabrast
    else:
      print("clave ilegal")


def encode_sust(palabrast):
  dic = {'a':"", 'b':"", 'c':"", 'd':"", 'e':"", 'f':"", 'g':"", 'h':"", 'i':"", 'j':"", 'k':"", 'l':"",'m':"", 'n':"", 'o':"", 'p':"", 'q':"", 'r':"", 's':"", 't':"", 'u':"", 'v':"", 'w':"", 'x':"", 'y':"", 'z':""}
  lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  palabrals = utilities.unify(palabrast)
  count_falla = 0
  count = 0
  flag = True
  print("Necesitamos crear la clave. Para esto pedimos que asigne letras para cada una en el abecedario, sin repetir. ")
  while flag == True:
    print("Numero de intento: {}, tiene 3 intentos.".format(count_falla+1))
    clave = input()
    if clave not in dic.values():
      if len(clave) > 1:
        print("clave ilegal")
        count_falla = count_falla +1
      else:
        dic[lista[count]] = clave
        print(dic)
        count = count + 1
    else:
      print("clave ilegal")
      count_falla = count_falla +1 
      
    if count_falla == 3:
      listaran = lista[:]
      ran.shuffle(listaran)
      print(listaran)
      print(lista)
      for item in listaran:
        if item not in dic.values():
          dic[lista[count]] = item
          count = count + 1
        print("el contador va en ", count)
        print(dic)
        if count == 26:
          break
         
    if dic["z"] != "":
      flag = False
     
  string = ""
  for i in range(len(palabrals)):
    palabrals[i] = dic[palabrals[i]]
    string = string + palabrals[i]
  print(string)
  return string


def encode_afin(palabrast):
  palabrals = utilities.unify(palabrast)
  claves_validas = utilities.rela_primes()
  for count_falla in range(4):
    if count_falla > 2:
      a = claves_validas[ran.randint(1,len(claves_validas))]
      b = ran.randint(1,25)
      print("Al usar todos los intentos, hemos elegido una clave por usted. La clave sera: 'a' = {} y 'b' ={}.".format(a,b))
      palabrals = utilities.convert(palabrals)
      for i in range(len(palabrals)):
        palabrals[i] = (((palabrals[i] * a)%26)+b)%26
      palabrast = utilities.deconvert(palabrals)
      print(palabrast)
      return palabrast
    print("Ingrese 'a' y 'b' que seran la pareja que funcionara como clave.\n Elija 'a' que pertenezca a la lista {}.\n Elija 'b' que sea un numero entre 1 y 25. \nNumero de intento: {}, tiene 3 intentos.".format(claves_validas, count_falla+1))
    print("Elija 'a'.")
    a = int(input())
    print("Elija 'b'.")
    b = int(input())
    if a in claves_validas:
      if 1 <= b <= 25:
        palabrals = utilities.convert(palabrals)
        for i in range(len(palabrals)):
          palabrals[i] = (((palabrals[i] * a)%26)+b)%26
        palabrast = utilities.deconvert(palabrals)
        print(palabrast)
        return palabrast
      else:
        print("clave ilegal")
    else:
      print("clave ilegal")
  return


def encode_permu(string):
  
  palabrals = utilities.unify(string)
  
  while True:
    print("Ingrese el tamaño de los bloques a permutar, considere que este tamaño debe ser menor o igual al tamaño de la palabra a encriptar.")
    m = int(input())
    if 1 <= m <=len(palabrals):
      break
    print("Tamaño invalido.")
  while True:
    print("Ingrese la cantidad de lugares a permutar, considere que esta cantidad debe ser menor al tamaño de los bloques.")
    l = int(input())
    if 1<= l < m:
      break
    print("Cantidad invalida.")
  
  chunks = [palabrals[x:x+m] for x in range(0, len(palabrals), m)]
  final=[]

  for x in chunks:
    test = []
    for i in range(l):
      test.append(x[(len(x)-(l-i))%len(x)])
      if(i>=len(x)-1):
        break
    for i in range(len(x)-l):
      test.append(x[i])
    final.extend(test)

  final = utilities.convert(final)
  final = utilities.deconvert(final)
  print(final)
  return final
#///////////////////////////////////////////////////////////////
#//////////////////////METODOS DE DECODIFICACION ///////////////////
#////////////////////////////////////////////////////////////////
####mbwjebftnvzmjoeb
####xmhupmqegzmoaeufmxuzpm (12)
def decode_despla(string):
  count_fallas = 0
  while count_fallas < 3:
    print("ingrese la clave, esta debe ser un numero entre 1 y 25.\n Tiene 3 intentos, este es el intento numero {}".format(count_fallas+1))
    key = int(input())
    if 1<= key<=26:
      lista = utilities.unify(string)
      lista = utilities.convert(lista)
      for j in range(len(lista)):
        lista[j] = (lista[j]-key)%26
      string = utilities.deconvert(lista)
      print(string)
      return string
    count_fallas = count_fallas + 1
  print("Al usar los 3 intentos, la aproximacion sera por fuerza bruta, las posibilidades son las siguientes:")
  for i in range(25):
    lista = utilities.unify(string)
    lista = utilities.convert(lista)
    for j in range(len(lista)):
      lista[j] = (lista[j]+1)%26
    string = utilities.deconvert(lista)
    print(string)
  return string
    
#lavidaesmuylinda
#sqbasqmnalmsnajaralfajafasnwfkjbaf (11) 
######### existe algo raro con el 11, arreglar
##qeaxgoxabaxxagngojgsgnoahg (21)
def decode_mult(string):
  inver_validas = utilities.inver_primes()
  keys = utilities.rela_primes()
  count_fallas = 0
  while count_fallas < 3:
    print("ingrese la clave, esta debe ser un numero que pertenece a la siguiente lista {}.\n Tiene 3 intentos, este es el intento numero {}".format(keys,count_fallas+1))
    key = int(input())
    if key in keys:
      lista = utilities.unify(string)
      lista = utilities.convert(lista)
      for i in range(len(keys)):
        if keys[i] == key:
          key = inver_validas[i]
      for j in range(len(lista)):  
        lista[j] = int((lista[j]*key)%26)
      string = utilities.deconvert(lista)
      print(string)
      return string
    count_fallas = count_fallas + 1
  print("Al usar los 3 intentos, la aproximacion sera por fuerza bruta, las posibilidades son las siguientes:")
  for i in inver_validas:
    lista = utilities.unify(string)
    lista = utilities.convert(lista)
    for j in range(len(lista)):
      lista[j] = int((lista[j]*i)%26)
    res = utilities.deconvert(lista)
    print(res)
  return res


  
  

## la vida es hermosa
##tulypuwqrwjaoqu (7,20)
##xuvijuogdobcmgu (5,20)
def decode_afin(string):
  alf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
  lista = utilities.unify(string)
  claves_validas = utilities.rela_primes()
  inversas_validas = utilities.inver_primes()
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
          palabrals = utilities.convert(lista)
          for i in range(len(palabrals)):
            palabrals[i] = (((palabrals[i] - b)%26)*ai)%26
          palabrast = utilities.deconvert(palabrals)
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
        lista = utilities.unify(string)
        ares = ((signoa*abs(a))*c)%26
        bres = (ei-(e * ares)%26)%26
        print("estos son a = {} y b = {}".format(ares,bres))
        palabrals = utilities.convert(lista)
        for i in range(len(claves_validas)):
          if claves_validas[i] == abs(ares):
            ares = inversas_validas[i]
            break
        for i in range(len(palabrals)):
          palabrals[i] = ((palabrals[i] - bres)*ares)%26
        palabrast = utilities.deconvert(palabrals)
        print(palabrast)
        return palabrast

def permufiesta(palabra,m,l):
  #Este metodo es para no tener que escribir lo mismo dos veces en decode_permu
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
  
  final = utilities.convert(final)
  final = utilities.deconvert(final)
  print(final)
  return final
  
def decode_permu(string):
  palabra = utilities.unify(string)
  print("Tiene usted el tamaño de los bloques? (Y/n)")
  res = input()
  
  if res == 'Y':
    print("Ingrese el tamaño de los bloques: ")
    m = int(input())
    print("Ingrese la cantidad de lugares a permutar: ")
    l = int(input())
    return permufiesta(palabra,m,l)

  else:
    print("Se decriptará a fuerza bruta imprimiendo así todas los posibles resultados para que el usuario elija así la que más le convenga.")
    final = []
    for i in range(1,len(palabra)+1):
      print("m = '{}'".format(i))
      final.append(permufiesta(palabra,i))
    return final
    
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