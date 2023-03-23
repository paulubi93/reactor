#Tutorial de Python: https://www.youtube.com/watch?v=HGOBQPFzWKo&ab_channel=freeCodeCamp.org

'''

#Lists: ordered, mutable, allows duplicate elements

mylist = ["banana", "cherry", "apple"]
print(mylist)

mylist2 = [5, "apple", "apple"]
print(mylist2)

item = mylist[-1] #imprime el ultimo elemento 
print(item)

for i in mylist:
    print(i)

 #ver si un elemento esta dentro de una lista 
if "banana" in mylist:
    print("yes")
else:
    print("no")

#numero de elementos en la lista
print(len(mylist2))

#anadir elementos a la lista 
mylist2.append("lemon")
print(mylist2)

#anadir un elemento en una posicion especifica 
mylist2.insert(2,"blueberry")
print(mylist2)

#quitar elementos 
item = mylist2.pop()
print(item)
print(mylist2)

#quitar elemento especifico 
item = mylist2.remove("blueberry")
print(mylist2)

#limpiar lista: mylist.clear()

#revertir una lista 
mylist2.reverse()
print(mylist2)

#ordenar una lista 
mylist3=[1,2,4,3,6,2]
item = mylist3.sort()
print(mylist3)

#desordenar lista como estaba al inicio: 
mylist3=[1,2,4,3,6,2]
new_list = sorted(mylist3)
print(mylist3)
print(new_list)

#crear una lista con el mismo elemento varias veces 
mylist4= [0]*5
print(mylist4)

#sumar listas: se adjunta una luego de la otra 
new_list=mylist3 + mylist4
print(new_list)

#cortar una lista con un intervalo determinado 
a=mylist3[1:3]
print(a)

#elegir solo los elementos de una lista de inicio a fin cada 2 elementos 
a=mylist3[::2]
print(a)

#copiar listas: si modificamos las copias, tambien modificaremos el original
list_copy=mylist
print(list_copy)
#para evitar el problema antes mencionado utilizamos 
list_copy=mylist.copy()
#o tambien 
list_copy=list(mylist)
#o tambien 
list_copy=mylist[:]

#comprension de listas: crear una lista a partir de otra existente incluyendo operaciones: 
# vamos a crear una lista de los cuadrados de los elementos de otra lista  
mylist3=[1,2,4,3,6,2]
mylist3_sq= [i*i for i in mylist3]
print(mylist3_sq)

'''

'''

#tuplas: ordered, immutable, allows duplicate elements

mytuple=("Max", 28, "Quito")
print(mytuple)
#Obs: una tupla de un elemento no se reconoce como tupla, para salvaguardar esto se pone una ',' al final 
mytuple=("Max",)
print(type(mytuple))

#crear tupla utilizando funcion 'tupla': creamos una tupla a partir de una lista 
mytuple=tuple(["Max", 28, "Quito"])

#acceder a un elemento
item = mytuple[0]
item1 = mytuple[-1]

#reemplazar un elemento 
#mytuple[0]="Paul" #ERROR: una tupla es immutable, no se pueden cambiar sus elementos, contrario a la lista

#iterar la tupla 
for i in mytuple:
    print(i)

#ver si un elemento esta en una tupla 
if "Quito" in mytuple:
    print("yes")
else: 
    print("no")

#contar el numero de veces que se repite un elemento 
mytuple = ('p', 'p', 'a', 'b', 'c', 'p')
print(mytuple.count('p'))

#encontrar la posicion de un element
print(mytuple.index('c'))

#convertir una tupla en una lista y viceversa
my_list = list(mytuple)
print(my_list)

#al reves
mytuple=tuple(my_list)
print(mytuple)

#slicing: acceder a partes de la tupla 
a = ('1','2','3','5','6','7')
b=a[2:5]
print(b)
#argumento de slicing con paso
c=a[::3]
print(c)

#slicing para revertir la tupla 
d=a[::-1]
print(d)

#desempaquetar una tupla 
mytuple="Max", 28, "Quito"
name, age, city = mytuple #cardinalidad de ambos lados debe ser igual
print(name)
print(age)
print(city)

#forma facil considerando todos los elementos, se respeta la cardinalidad 
a = ('1','2','3','5','6','7')
a1, *a2, a3 = a #la '*' es muy importante para hacer respetar la cardinalidad de ambos lados por el numero de variables
#a la izquierda
print(a1)
print(a2)
print(a3)

#comparar tuplas y listas: las listas tienen mas peso en espacio y mas tiempo en crearse que las tuplas por ser mutables 
import sys 
my_list= [0, 1, 2, "hello", True]
my_tuple = (0, 1, 2, "hello", True)
print(sys.getsizeof(my_list), "bytes")
print(sys.getsizeof(my_tuple), "bytes")

#tiempo que se demora en crear un millon de veces una lista y una tupla
import timeit
print (timeit.timeit(stmt="[0, 1, 2, 3, 4, 5]", number=1000000))
print(timeit.timeit(stmt="(0, 1, 2, 3, 4, 5)", number=1000000))

'''

'''

#Dictionary: collection data type, key-value pairs, unordered, mutable

#creacion
mydict={
    "name": "Max",
    "age": 28,
    "city": "Quito"
}
print(mydict)

#otra forma
mydict2=dict(name= "Mary", age= 50, city="Ibarra")
print(mydict2)

#acceder a los valores
value = mydict["name"]

#diccionario es immutable: anadir, sustituir, eliminar 
mydict["email"]="xyz.com"
mydict["email"]="cool.xyz.com"
del mydict["email"] #eliminar email
# mydict.pop("email") 
mydict.popitem()#elimina el ultimo elemento 

#verificar si esta un elemento
if "name" in mydict:
    print(mydict["name"])
else:
    print("no")

#o tambien 
try:
    print(mydict["name"])
except:
    print("error")

#lazo for en diccionarios 
for key in mydict:
    print(key)

#o tambien se puede retornar una lista con todas las keys o los valores
for key in mydict.keys():
    print(key)

for value in mydict.values():
    print(value)

# los dos a la vez
for key, value in mydict.items():
    print(key, value)

#copiar un diccionario 
mydict_copy = mydict # es el mismo que el original pero tambien inflinge cambios en el original 
mydict_copy["email"] = "xyz.com"
print(mydict_copy)
print(mydict)

#para evitar cambios en el original 
mydict_copy=mydict.copy()

# o tambien 
mydict_copy = dict(mydict)

#fusionar diccionarios: update method 
mydict={
    "name": "Max",
    "age": 28,
    "email": "xyz.com"
}
mydict2=dict(name= "Mary", age= 50, city="Ibarra")

mydict_merge=mydict.update(mydict2) #sustituye los valores presentes en el dic inicial y aumenta los que no hay en el inicial
print(mydict)

#tipos de 'key': numeros o tuplas
my_dict={3: 9, 6: 36, 9: 81}
print(my_dict)

value = my_dict[3] #Obs: se tiene que utilizar la 'key' directamente y no el valor de la posicion, caso contrario obtenemos error
print(value)

# con tuplas 
my_tuple=(8,7)
my_dict = {my_tuple: 15}
print(my_dict)
#no se puede utilizar listas: my_tuple=[8,7] puesto que es mutable 

'''

'''

#Conjuntos: unordered, mutable, no duplicates 
myset = {1, 2, 3}
print(myset)
#En el caso de repetirse elementos dentro del conjunto, estos se imprimen solamente 1 vez

#crear con una lista y funcion set()
myset = set([1, 2, 3]) 

#o si incluimos un string, va a incluir cada letra de forma independiente 
myset = set("Hello")
print(myset)
#obtenemos letras no ordenadas por la propiedad de conjuntos 

#empty set 
myset = {} #esto es un diccionario 
myset = set() #esto es correcto 

#es immutable, podemos: anadir, remover, descartar, limpiar, pop 
myset.add(1)
myset.remove(1) #bota error si el elemento no se encuentra en el conjunto
myset.discard(1) #no bota error en el anterior caso
myset.clear()#vacia el conjunto 
# myset.pop() #remueve un valor al azar y tambien lo imprime 

#iterar sobre el conjunto 
for i in myset:
    print(i)

#ver si un elemento pertenece al conjunto 
if 1 in myset:
    print("yes")

#union e interseccion de conjuntos
odds = {1, 3, 5, 7, 9}
evens = {0, 2, 4, 6, 8}
primes = {2, 3, 5, 7}

union_set = odds.union(evens) # no toma en cuenta la duplicacion de elementos 
print(union_set)
intersec_set=odds.intersection(evens)
print(intersec_set)

#resta entre dos conjuntos 
setA = {1, 2, 3, 4, 5, 6, 7, 8, 9}
setB = {1, 2, 3, 10, 11, 12}

dif_set = setA.difference(setB)
print(dif_set)

#diferencia simetrica: retorna un conjunto con elementos no comunes entre dos conjuntos 
sim_set = setA.symmetric_difference(setB)
print(sim_set)

#actualizar conjuntos: anade los elementos de B a A sin contar los duplicados
setA.update(setB)
print(setA)

#actualizar con interseccion: mantiene solo los elementos presentes en ambos conjuntos 
setA.intersection_update(setB)
print(setA)

#actualizar con diferencia: remueve los elementos del A presentes en el B
setA.difference_update(setB)
print(setA)

#actualizar con diferencia simetrica: mantiene los elementos presentes en A y B pero no los elementos en ambos 
setA.symmetric_difference_update(setB)
print(setA)

#subconjuntos 
setA = {1, 2, 3, 4, 5, 6}
setB = {1, 2, 3}

print(setA.issubset(setB))#Falso
print(setA.issuperset(setB))#True
print(setA.isdisjoint(setB))#False

#copia de conjuntos: mismas observaciones con respecto a los anteriores casos 
setB = setA #copia y tambien influye cambios en el original 
setB = setA.copy()
setB = set(setA)

#conjunto frozen: conjunto immutable (no sirven ni los metodos de update)
a = frozenset([1, 2, 3, 4])
print(a)
a.add(2)#Error 

'''

'''

#Strings: ordered, immutable, text representation 
#Para su creacion podemos utilizar "" o ''
my_string = 'I\'m Ecuadorian'

#Multilineas: utilizamos """ """
my_string = """
Hello 
world"""
print(my_string)

#acceder a caracteres o substrings: 
my_string = "Hello" 
char = my_string[0]
print(char)

#slicing 
substring = my_string[1:3] 

#intervalo de caracteres paso igual a 2 
substring=my_string[::2]

#invertir palabra 
substring=my_string[::-1]
print(substring)

#concatenar strings 
name ="Paul" 
sentence = my_string +" "+ name 
print(sentence)

#iteracion sobre el string 
for i in name:
    print(i)

#ver si un caracter se encuentra en un string 
if "el" in my_string:
    print("yes")
else:
    print("no")

#eliminar espacios en blanco con 'strip'
my_string = '          Hello          '
my_string = my_string.strip()
print(my_string)

#Convertir caracteres en mayusculas o minusculas, si empieza o termina con una letra en particular, encontra el indice de una letra
name = "Paul"
print(name.upper())
print(name.lower())
print(name.startswith('P'))
print(name.endswith('P'))
print(name.find('u')) #si no encuentra dicho caracter regresa '-1'

#reemplazar palabras o caracteres 
print(name.replace('Paul', 'Bryan')) #Obs: regresa un nuevo string por lo que no afecta al original 

#convertir string en list y viceversa
my_string = 'Como estas?'
my_list = my_string.split() # el argumento dentro de .split() es el espacio
print(my_list)

my_string = ' '.join(my_list)
print(my_string)

#otro caso respecto al anterior ejemplo
my_list = ['a']*500
from timeit import default_timer as timer 

#caso pesado para crear strings a partir de una lista 
start=timer()
my_string = ''
for i in my_list:
    my_string +=i #esto rellena el string con los elementos de la lista. Es una operacion pesada 
stop = timer()
print(stop-start)

#caso rapido para crear strings a partir de una lista 
start=timer()
my_string = ''.join(my_list) #este caso es mas rapido 
stop = timer()
print(stop-start)

#formatear strings: % o format(), f-strings

#1) 
var = "Paul" 
my_string = "The variable is %s" % var #%s reemplazado por var
var = 3
my_string = "The variable is %d" % var #%d representa valor decimal
var = 3.16
my_string = "The variable is %.2f" % var #%f representa float, .2 representa 2 decimales
print(my_string)

#2) 
var = "Paul" 
my_string = "The variable is {}".format(var) 
#o tambien funciona con valores numericos y varias variables a la vez
var = 3.1416 
var1 = 4
my_string = "The variable is {:.2f} and {}".format(var,var1) # 'f' representa float, .2 representa 2 decimales
print(my_string)

#3) forma mas utilizada
var = 3.1416 
var1 = 4
my_string = f"The variable is {var*2} and {var1}" # forma mas utilizada. Se pueden utilizar operaciones matematicas 
print(my_string)

'''

'''

#Collections: counter, namedtuple, OrderedDict, defaultDict, deque

#1) Counter: es un contenedor que almacena los elementos como keys de diccionarios y sus repeticiones como valores de diccioarios 
from collections import Counter
a = 'aaaaabbbbccc'
my_counter = Counter(a)
print(my_counter)
# resultado: Counter({'a': 5, 'b': 4, 'c': 3})
print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())
print(my_counter.most_common())#devuelve una lista de duplas ordenadas del mas comun al menos  
print(my_counter.most_common(1)[0][0])#acceder al elemento mas repetido
print(list(my_counter.elements()))

#2) namedtuple: crea una clase con un nombre especifico y con campos tambien especificos 
from collections import namedtuple
point = namedtuple('point', 'x, y') 
pt = point(1,-4)
print(pt)
#resultado: point(x=1, y=-4)
print(pt.x, pt.y)
#resultado: 1 -4

#3)OrderedDict: diccionario con orden, no immutable 
from collections import OrderedDict
ordered_dict = OrderedDict()
# tambien se utiliza ordered_dict = {} en las nuevas versiones de Python
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
print(ordered_dict)

#4)defaultDict: diccionario con la unica diferencia que se asigna un valor de default (0) cuando una 'key' no tiene un valor asignado
# con un diccionario comun este tipo de errores botan un mensaje  
from collections import defaultdict
d = defaultdict(int)
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4
print(d['e']) # resulltado = 0 (valor de default)

#5)deque: es una cola de con dos extremos. Se utiliza para meter o sacar valores de ambos extremos 
from collections import deque
d = deque()
d.append(1)
d.append(2)
d.append(3)
d.appendleft(5) #naturalmente se anaden a la derecha 
print(d)

d.popleft()
print(d)

d.extendleft([7,8,9]) #entran en forma de pila (primero 7 y el mas extremo vendria a ser el 9)
print(d)

d.rotate(1) #rota los elementos hacia la derecha 1 posicion. Para rotar hacia la izquierda consideramos valores negativos
print(d)

'''

'''

# itertools: product, permutations, combinations, accumulate, groupby, and infinite iterators 
#los iteradores son tipos de datos que se utilizan en los lazos for: listas 

#1) product: calcula el producto cartesiano de listas
from itertools import product
a = [1, 2]
b = [4, 5]
prod = product(a,b) 
print(list(prod))

#2) permutations: retorna todas las permutaciones posibles del input
from itertools import permutations
a = [1, 2, 3]
perm=permutations(a) # se puede especificar la longitud de la permutacion con un segundo argumento 
print(list(perm))

#3) combinations: retorna todas las posibles combinaciones del input, con longitud especifica
from itertools import combinations, combinations_with_replacement
a = [1, 2, 3]
comb=combinations(a,2)
print(list(comb)) #no hay repeticiones. Si deseamos, podemos importar 'combinations_with_replacement'

comb_w=combinations_with_replacement(a,2)
print(list(comb_w)) 

#4) accumulate: retorna sumas acumuladas entre los elementos de la lista (anterior mas actual) o cualquier otra funcion binaria 
from itertools import accumulate
import operator #para la multiplicacion
a = [1, 2, 3]
acc = accumulate(a)
print(list(acc))

acc_mul = accumulate(a,func=operator.mul) #multiplica el anterior con el actual en cada posicion
print(list(acc_mul))

#5) groupby: retorna keys y las agrupa de forma iterativa con los valores 
from itertools import groupby   
def smaller_than_3(x):
    return x<3

a = [1,2,3,4]
group1 = groupby(a,key = smaller_than_3)
for key,value in group1:
    print(key,list(value))

#6) groupby con funciones lambda: son funciones de una linea que pueden tener un input 
from itertools import groupby   
#en este caso, eseta funcion ya no es util 
def smaller_than_3(x):
    return x<3

a = [1,2,3,4]
group1 = groupby(a,key = lambda x: x < 3) # la funcion lambda resume la funcion antes codificada 
for key,value in group1:
    print(key,list(value))

#otro ejemplo de groupby : una lista que incluye diferentes diccionarios 
persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25},
            {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}]

#queremos agrupar a las personas por su edad 
group1 = groupby(persons, key = lambda x: x['age']) # la funcion lambda resume la funcion antes codificada 
for key,value in group1:
    print(key,list(value)) 

#iteradores infinitos: 
from itertools import count, cycle, repeat

#count: funcion que empieza a contar hasta el infinito desde un valor de partida    
for i in count(10):
    print(i)
    if i == 15:
        break

#cycle: imprime infinitas veces una lista 
a = [1,2,3,4]
for i in cycle(a):
    print(i)
    if i == 2:
        break

#repeat: repite infinitas veces un numero en especifico
for i in repeat(1,10): #como segundo argumento se puede incluir el numero de veces que se quiere repetir el numero
    print(i)

'''

'''

#Lambda functions

add10 = lambda x: x + 10 #esto crea una funcion con un argumento y suma 10 al argumento y retorna el resultado.
# la variable asignada se convierte en una funcion de variable x 
print(add10(5))
# es lo mismo que crear la funcion 
def add10_func(x):
    return x + 10

#funcion mult con varios argumentos 
mult = lambda x,y: x*y
print(mult(2,0))

#son funciones que se utilizan una sola vez en el codigo o como argumento para otras funciones mas complejas 

#funciones de arreglo 

#sorted 
points2D = [(1, 3), (15, 1), (5, -1), (10, 4)]
points2D_sorted = sorted(points2D) 
print(points2D)
print(points2D_sorted) #ordena de menor a mayor segun el primer argumento 

#se puede especificar un metodo de orden: ordenemos segun el segundo argumento 
points2D_sorted = sorted(points2D, key=lambda x: x[1]) 
print(points2D)
print(points2D_sorted)

#o en lugar de utilizar funcion lambda: 
def sort_by_y(x):
    return x[1]
points2D_sorted = sorted(points2D, key=sort_by_y) 
print(points2D)
print(points2D_sorted)

#map function: transforma cada elemento con una funcion: map(func, seq)
a = [1,2,3,4,5]
b = map(lambda x:x*2, a)
print(list(b)) #se multiplica cada elemento por 2 

#list comprehension: lo mismo pero optimizado 
c=[x*2 for x in a] 
print(c)

#filter function: es una funcion que devuelve boleanos, devuelve los valores Verdaderos como respuesta: filter(func, seq)
#queremos filtrar los numeros pares de una secuencia 
a = [1,2,3,4,5,6]
b = filter(lambda x:x%2==0, a)
print(list(b)) 

#list comprehension: lo mismo pero optimizado 
c=[x for x in a if x%2==0] 
print(c)

#reduce function: aplica repetidamente la funcion y devuelve un solo valor: filter(func, seq)
#calcular el producto de todos los elementos de una lista 
from functools import reduce
a = [1,2,3,4,5,6]
b = reduce(lambda x,y:x*y, a)
print(b) 

'''

'''

#Errors and exceptions: sustituye el mensaje de error por sintaxis 

#1) errores de sintaxis
#a=5 
#print(a)) #error por un parantesis extra 

#2) errores de tipo
#a=5+'10' #operando no soportado int + string

#3)import error 
# import somemodule not exist

#4) name error 
#a=5
#b=c #variable no definida 

#5) file not found error 
# f = open('somefile.txt') #file not found 

#6)value error: ocurre cuando la funcion recibe una variable no adecuada
# a = [1,2,3] 
# a.remove(4) #x no esta en la lista 

#7) index error: cuando se accede al indice de una sucesion o de una lista  
# a = [1,2,3]
# a[4] list index out of range 

#8) key error 
# my_dict = {'name': 'Max'}
# my_dict['age'] #key error 

#incluir excepciones 
x = -5 
if x < 0:
    raise Exception('x should be positive')

#assert statement 
x = -5 
assert (x >= 0), 'x is not positive' # se incluye un argumento falso y devuelve un error de acersion

#try and except 
try: 
    a = 5/0
except:  
    print('error')

# o tambien se puede modificar el tipo de excepcion 
try: 
    a = 5/0
except Exception as e: 
    print(e)

 # tambien se puede incluir la sentencia 'ZeroDivisionError' o 'TypeError'
try: 
    a = 5/0
except ZeroDivisionError as e: 
    print(e)
except TypeError as e:
    print(e)
else:
    print("Everything is fine")
finally: #usado para operacion de limpieza 
    print('cleaning up')

#Definir nuestras propias excepciones 
class ValueTooHighError(Exception): 
    pass      #manera correcta de definir una excepcion. 'pass' se encarga de no dejar el vacio en el cuerpo

class ValueTooSmallError(Exception): 
    def __init__(self, message, value):
        self.message = message
        self.value = value 

def test_value():
    if x > 100:
        raise ValueTooHighError('value is too high')
    if x < 5:
        raise ValueTooSmallError('value is too small', x)

try:
    test_value(200)
except ValueTooHighError as e:
    print(e)
except ValueTooSmallError as e:
    print(e.message, e.value )

'''

'''
# Logging 
import logging 

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s-%(name)s-%(levelname)s-%(message)s'
                    ,datefmt='%m/%d/%Y %H:%M:%S')
import helper # esto para cambiar el nombre del logger. Hace referencia al archivo 'helper.py'

#tenemos 5 diferentes niveles de "log", muestran la severidad del evento 
logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')
#los dos primeros no se imprimen, esto es porquen por default, solo mensajes de 'warning' o mas altos se 
#imprimen. Si queremos cambiar esto ejecutamos logging.basicConfig antes del 'import logging'

#%(asctime)s: imprime el tiempo en el que se muestra el mensaje 
#%(name)s: nombre del logger, en este caso 'root'
#%(levelname)s: imprime el nombre del nivel de advertencia 
#%(message)s: imprime el mensaje 
#datefmt='%m/%d/%Y %H:%M:%S: formato del tiempo

#Obs: por buena practica, el logger no se debe considerar 'root', entonces para cambiarlo: 
#1) crearmos un nuevo archivo 'helper.py' y escribimos: 
#    import logging 
#    logger = logging.getLogger(__name__) # en este caso __name__ seria 'helper'
#    logger.info ('hello from demo')

#2) en el documento de trabajo escribimos: import helper

#3) corremos el programa sin considerar otros comandos luego de esta linea, y obtenemos: 
# 03/20/2023 14:54:48-helper-INFO-hello from demo


#log handlers: encargados de entregar el debido mensaje (por mail o archivo incluso) de los loggers
import logging 
logger = logging.getLogger(__name__) #establecer nombre del modulo

#create handler 
stream_h = logging.StreamHandler()
file_h = logging.FileHandler('file.log') #nos crea un archivo 'file.log' con el mensaje de error 

#set up level and format 
stream_h.setLevel(logging.WARNING) #recordar que el se muestran mensajes de warning para arriba 
file_h.setLevel(logging.ERROR)

formatter = logging.Formatter('%(name)s-%(levelname)s-%(message)s')
stream_h.setFormatter(formatter)
file_h.setFormatter(formatter)

#anadir handler al logger 
logger.addHandler(stream_h)
logger.addHandler(file_h)

logger.warning('this is a warning')
logger.error('this is an error')

#otros tipos de config methods 
#Para esto creamos un archivo 'logging.conf' o 'logging.ini' (ver archivo para ver codigo)
import logging
import logging.config
from os import path

#no funciona esto
logging.config.fileConfig('logging.conf')

#tampoco funciona 
#log_file_path = path.join(path.dirname(path.abspath(__file__)), 'logging.conf')
#logging.config.fileConfig(log_file_path)


#creamos el logger 

logger = logging.getLogger('simpleExample')
logger.debug('this is a debug message')    

#capturing stack traces: muy util para troubleshooting issues
import logging

#Ejm: creemos un codigo que de una excepcion 
try: 
    a = [1,2,3]
    val = a[4] #error normal: IndexError: list index out of range
except IndexError as err:
    logging.error(err, exc_info=True)

# error modificado: ERROR:root:list index out of range
# si aumentamos el stack trace (el resumen del error y la raiz del archivo), es decir, 
# logging.error(err, , exc_info=True), obtenemos: 
#Traceback (most recent call last):
#  File "c:/Users/paug9/Desktop/Reactor/Python/Tutoriales/demo2.py", line 871, in <module>
#    val = a[4] #error normal: IndexError: list index out of range
#IndexError: list index out of range

#caso general, si no especificamos el tipo de error 
import traceback 

try: 
    a = [1,2,3]
    val = a[4] #error normal: IndexError: list index out of range
except IndexError as err:
    logging.error('the error is %s', traceback.format_exc())


#Rotating filehandlers: en el caso que tengamos muchos log messages y queremos ver el track issue de los 
#eventos mas recicentes 
import logging
from logging.handlers import RotatingFileHandler

logger = logging.getLogger(__name__) #creamos el logger
logger.setLevel(logging.INFO) # establecemos el nivel 

#roll over after 2KB, aand keep backup logs app.log.1, app.log.2, etc. 
handler = RotatingFileHandler('app.log', maxBytes=2000, backupCount=5) #especificamos el tipo de Handler
# creamos un archivo 'app.log', el almacenamiento maximo por cada archivo .log, y la cantidad maxima de archivos 
logger.addHandler(handler) #anadimos nuestro Handler al logger 

for _ in range(10000): #el '_' significa que no ponemos importancia a esa variable (puesto que no vamos a utilizarla)
    logger.info('Hello world')

#acabamos de crear 6 archivos .log con el mensaje establecido 


#Rotating filehandlers with time: crea un log basado en el tiempo consumido 

import logging
import time
from logging.handlers import TimedRotatingFileHandler

logger = logging.getLogger(__name__) #creamos el logger
logger.setLevel(logging.INFO) # establecemos el nivel 

handler = TimedRotatingFileHandler('timed_test.log', when='s', interval=5, backupCount=5)
#se definio el nombre del .log, tiempo que debe consumirse ('s' para segundos, 'm' para minutos, 'h' para horas, 
# 'd' para dias, 'midnight', w0 (para lunes), w1 (para martes), etc), cada 5 segundos se realiza la rotacion, con
# 5 archivos 
logger.addHandler(handler)

for _ in range(6): 
    logger.info('Hello world')
    time.sleep(5)

#van a crearse los documentos .log cada 5 segundos hasta 

#Obs: se puede utilizar logger con json (ver en github python-json-logger)


'''

'''

#JSON: JavaScript Object Notation. Utilizada para intercambio de datos en aplicaciones web
#Utilizaremos el archivo 'example.json'

#codificacion o serializacion: de Python a JSON
#Convert Python objects (in this case 'person') into a JSON string with the 'json.dumps()' method.
import json

person = {"name": "John", "age": 30, "city": "New York", "hasChildren": False, "titles": ["engineer", "programmer"]}

# convert into JSON:
person_json = json.dumps(person) # esta funcion nos permite transformar a strings tipo JSON

# use different formatting style: utilizamos indent para darle un buen formato, podemos cambiar 
#los separadores cambian: los ':' por '=', la ',' por ';' 
#Obs: se recomienda utilizar los separadores por default
#'sort_keys=True' ordena alfabeticamente las keys
person_json2 = json.dumps(person, indent=4, separators=("; ", "= "), sort_keys=True)

#podemos convertir el resultado en un archivo con el siguiente codigo:
#with open ('person.json', 'w') as file:
#    json.dump(person, file, indent=4)

# the result is a JSON string:
print(person_json) #es un objeto tipo JSON puesto que los booleanos estan con minuscula (notacion JSON)
print(person_json2) # el objeto tipo JSON con arreglos y modificaciones


#decodificacion o deserializacion: convertir un objeto JSON a Python 
person = json.loads(person_json2)
print(person) #obtenemos un objeto Python (un diccionario) puesto que los booleanos estan con mayuscula

#para decodificar un archivo .json:
#with open ('person.json', 'r') as file:
#     person = json.load(file)
#     print(person)


# ahora consideremos el caso en que tenemos una clase cualquiera (ya no un diccionario):
import json 
# a priori, las clases no son serializables, por ende hay que considerar una funcion decodificadora custom:
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

user = User('Max', 27)

#funcion decodificadora custom
def enconde_user(o):
    if isinstance(o, User): #verifica si un objeto es parte de una clase o subclase 
        return {'name':o.name, 'age':o.age,o.__class__.__name__: True} # devolvemos los elementos de la clase mas
        # el nombre de la clase (su valor no importa por lo que se rellena con True)
    else:
        return TypeError('Object of type User is not JSON serializable')

#convertir en formato JSON (debemos especificar el uso de nuestra funcion especial mediante el 'default')
userJSON = json.dumps(user, default=enconde_user)
print(userJSON)

#otro metodo para implementar un decodificador custom ya incluido
import json
from json import JSONEncoder

class UserEncoder(JSONEncoder):
    def default(self, o): #hace lo mismo que la funcion 'enconde_user' anterior
        if isinstance(o, User):
            return {'name':o.name, 'age':o.age,o.__class__.__name__: True}
        return JSONEncoder.default(self, o)

#ahora, en lugar del 'default' consideramos un argumento 'cls' de clase con el UserEncoder y ya no el 'enconde_user)'
userJSON = json.dumps(user, cls=UserEncoder) 
print(userJSON)

#tercera opcion: utilizar el 'UserEncoder' directamente
import json
from json import JSONEncoder

userJSON = UserEncoder().encode(user)
print(userJSON)

#ahora realizamos la decodificacion de JSON a Python con una clase particular 
# en este caso funciona directamente pero nos devuelve un diccionario en lugar de una clase
import json

#para obtener una clase necesitamos una funcion custom decodificadora
def decode_user(dct):
    if User.__name__ in dct: #utilizamos el nombre de la clase para identificar 
        return User(name=dct['name'], age=dct['age'])
    return dct

#utilizamos la funcion custom decodificadora para obtener una clase 
user = json.loads(userJSON, object_hook=decode_user)
print(user)
# al ser una clase podemos acceder a sus elementos: 
print(user.name)
print(user.age)

'''

'''

#Random Numbers
#Vamos a ver distintos modulos para generar numeros aleatorios 

#1) Random module: genera valores "aleatorios" (son reproductibles = facilmente obtenibles a partir de una semilla) 
# con varias distibuciones  
import random 

#1.1) random(): valor aleatorio (float) de 0 a 1 
a = random.random()
print(a) 

#1.2) uniform(): valor aleatorio (float) dentro de un intervalo especifico 
a = random.uniform(1,10)
print(a) 

#1.3) randint(): valor aleatorio (entero) dentro de un intervalo especifico, incluye extremos intervalo
a = random.randint(1,10)
print(a) 

#1.4) randrange(): valor aleatorio (entero) dentro de un intervalo especifico, no incluye extremos intervalo
a = random.randint(1,10)
print(a) 

#1.5) normalvariate(): distribucion normal con media 0 y desviacion estandarf 1
a = random.normalvariate(0,1)
print(a) 

#2) sucesiones: 
import random 

mylist = list("ABCDEFGH")
print(mylist)

#2.1) choice(): escoge al azar un elemento de una lista 
a = random.choice(mylist)
print(a)

#2.2) sample(): escoge una muestra (en este caso 3 elementos) al azar (sin repeticion) de una lista 
a = random.sample(mylist, 3)
print(a)

#2.3) choices(): escoge una muestra (en este caso 3 elementos) al azar (con repeticion) de una lista  
a = random.choices(mylist, k=3)
print(a)

#2.4) random.shuffle(): mezclar los elementos de una lista 
random.shuffle(mylist)
print(mylist)


#como cambiar la semilla (seed) de los valores aleatorios
import random 

random.seed(1) #todos los valores aleatorios generados a partir de esta semilla van a ser iguales 
# es decir, si generamos valores aleatorios 2 veces a partir de una distribucion, vamos a obtener 
# en ambos casos los mismos valores  
print(random.random())
print(random.randint(1,10))

#Obs: al ser valores reproducibles, facilmente obtenibles a partir de una semilla, no son optimos 
# para utilizar en seguridad. Para este caso utilizamos el siguiente modulo 

#3) secrets module: se utiliza para generar contrasenas o mensajes secretos
import secrets
#estos si generan verdaderos valores aleatorios por lo que su tiempo de proceso es mayor 

#3.1) randbelow(): genera un valor aleatorio (entero) de 0 a 10 con extremos no incluidos
a = secrets.randbelow(10)
print(a)

#3.2)randbits(): genera un valor aleatorio (entero) con un numero especifico de bits
a = secrets.randbits(k=10)
print(a)

#3.3)choice(): escoge una muestra (en este caso 3 elementos) al azar (no reproducible) (con repeticion) de una lista 
mylist = list("ABCDEFGH")
a = secrets.choice(mylist)
print(a)

#4) numpy module: 
import numpy as np

#4.1) array with random floats 
a = np.random.rand(3,3) #arreglo de 3X3
print(a)

#4.2) array with random integers  
a = np.random.randint(0,10, 3) #arreglo de 3X3 de valores enteros entre 0 y 10
print(a)

#4.3) si queremos tuplas 
a = np.random.randint(0,10, (3,4)) #matriz 3x4
print(a)

#4.4) random shuffle
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)
np.random.shuffle(arr) #mezcla las filas manteniendo sus valores iniciales 
print(arr)

#funcion seed de numpy (muy distinto al anterior visto)
np.random.seed(1)
print(np.random.rand(3,3))
np.random.seed(1)
print(np.random.rand(3,3))

'''

'''

#Decorators: herramientas diferentes a una funcion, con syntax igual al de una funcion y llamandala con @nombre.
#Usualmente extienden el funcionamiento de una funcion en la cual se aplica, explicitamente modificandola.
#En pocas palabras, ayuda a dar una nueva funcionalidad a una funcion ya existente  

#1)function decorator:
def start_decorator(func):
    def wrapper():
        print('start')
        func()
        print('end')
    return wrapper

#aplicamos el decorador a esta funcion
def print_name():
    print('Alex')

print_name()

#para aplicar el decorador: le asignamos a la funcion dentro del decorador  
print_name = start_decorator(print_name)
print_name()

#otra forma para aplicar el decorador de manera facil  
@start_decorator 
def print_name():
    print('Alex')

print_name()


#2) si nuestra funcion tiene argumentos: 
@start_decorator 
def add5(x):
    return x + 5
#add5(10)
#ERROR: TypeError: wrapper() takes 0 positional arguments but 1 was given

#Necesitamos tener el mismo argumento dentro de la funcion del decorador que en la funcion en 
#donde se le aplica el decorador
#Para arreglar este error, aplicamos las variables *args, **kwargs dentro de la funcion del decorador
#estos permiten utilizar libremente el numero que sea de variables o argumentos 
import functools

def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        #podemos hacer algo antes de que se ejecute la funcion principal
        print('start')
        result = func(*args, **kwargs) #asignamos una variable a func() para evitar un resultado NONE
        #podemos hacer algo despues de que se ejecute la funcion principal
        print('end')
        return result  #para evitar el resultado NONE
    return wrapper

@my_decorator 
def add5(x):
    return x + 5

result = add5(10)
print(result)

#se tiene una ambiguedad por parte de Python al querer identificar la funcion add5 puesto que la identifica 
#como la funcion que se utiliza dentro del decorador (wrapper())

print(help(add5))
print(add5.__name__)

#Help on function wrapper in module __main__:
#wrapper(*args, **kwargs)
#None
#wrapper

#Para arreglar este problema anadimos el modulo 'functools' y antes de la funcion dentro del decorador
#aplicamos un in-built decorator llamado 'functools.wraps(func)', este se encarga de preservar la informacion 
#de la funcion principal fuera del decorador 

#3) si el decorador toma directamente los argumentos 

import functools

def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):    
            for _ in range(num_times):
                result = func(*args,**kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=3) #repite 3 veces la funcion principal. Es un decorador con argumento 
def greet(name):
    print(f'Hello {name}')
greet('Alex')

#4) decoradores anidados: utilizamos los decoradores @debug y @start_decorator
import functools

def start_decorator(func):
    
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        print('start')
        result = func(*args,**kwargs)
        print('end')
        return result
    return wrapper

def debug(func):
    @functools.wraps(func)
    def wrapper(*args,**kwargs):
        args_repr = [repr(a) for a in args] #extraemos los *args 
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()] #extraemos los *kargs 
        signature = ",".join(args_repr + kwargs_repr) #extrae el nombre 
        print(f"Calling {func.__name__}({signature})") #imprime la info de esta funcion 
        result = func(*args,**kwargs) #ejecuta la funcion principal 
        print(f"Calling {func.__name__!r}returned {result!r}") #imprime la info del valor de retorno 
        return result
    return wrapper 

#los decoradores se ejecutan en el orden en el que estan enlistados 
#se ejecuta @debug y dentro de este se ejecuta @start_decorator y dentro de este se ejecuta la funcion say_hello(name):
@debug
@start_decorator
def say_hello(name):
    greeting = f'Hello {name}'
    print(greeting)
    return greeting

say_hello('Alex')

#resultado:
# Calling say_hello('Alex')
# start
# Hello Alex
# end
# Calling 'say_hello'returned 'Hello Alex'

#5)class decorators: son utilizadas cuando deseamos tener un estado actualizado.
#en el siguiente ejemplo queremos saber cuantas veces se ejecuta la funcion principal
class CountCalls:

    def __init__(self, func):
        self.func = func
        self._num_calls = 0 #creamos un estado que cuenta el numero de ves que se ejecuta la funcion

    def __call__(self,*args,**kwargs): #este me permite ejecutar un objeto de la clase inicial como una funcion 
        #print('Hi there')
        #queremos actualizar el estado 
        self._num_calls += 1
        print(f'This is executed {self._num_calls} times')
        return self.func(*args,**kwargs)
#cc=CountCalls(None) #se ejecuta como una funcion la clase inicial 
#cc()

@CountCalls
def say_hello():
    print('Hello')

say_hello() #This is executed 1 times
say_hello() #This is executed 2 times

'''

'''

#Generadores: son funciones que devuelven un objeto que itera. Generan los elementos una sola vez y bajo pedido, y por ende
#son mas eficientes que el resto de funciones cuando se tiene que trabajar con muchos datos 

#ejemplo: Notar que los "generadores" utilizan el comando 'yield' en lugar del 'return', y tambien permiten el uso
#de varios 'yields'
def mygenerator():
    yield 1 
    yield 2
    yield 3

#objeto generador
g = mygenerator()
print(g)

#se puede hacer loop
#for i in g:
#    print(i)

#o utilizar el comando 'next' para obtener un valor a la vez
value = next(g)
print(value)# Resultado = 1

value = next(g)
print(value)# Resultado = 2

value = next(g)
print(value)# Resultado = 3

#value = next(g)
#print(value)# Resultado = StopIteration (ya no se tiene otra sentencia 'yield')

#1) se los puede utilizar como inputs para otras funciones 
def mygenerator():
    yield 2 
    yield 1
    yield 3

g = mygenerator()
print(sum(g))

#o se puede utilizar la funcion 'sorted' para ordenar los yields
def mygenerator():
    yield 2 
    yield 1
    yield 3
g = mygenerator()

print(sorted(g))

#2)ejecucion de una funcion generadora 
def countdown(num):
    print('Starting')
    while num>0:
        yield num
        num -=1

cd = countdown(4) #hasta aqui nada se imprime 

value = next(cd)
print(value) #Resultado = 4
value = next(cd)
print(value) #Resultado = 3

#3) eficiencia de los generadores: creemos una sucesion que tenga como entrada un valor entero e imprima todos los valores desde el 0 hasta dicho valor
import sys
# 3.1) sin utilizar generador
def first(n):
    nums = [] #todos los numeros se van a almacenar en esta lista, esto consume mucha memoria
    num=0
    while num<n:
        nums.append(num)
        num +=1
    return nums

print(sys.getsizeof(first(100)))#resultado= 452 bytes
print(sum(first(10)))

#utilizando generador

def firstn_generator(n):
    # ya no necesitamos la lista nums = []
    num=0
    while num<n:
        yield num
        num +=1

print(sys.getsizeof(firstn_generator(100))) #resultado= 56 bytes
print(sum(firstn_generator(100)))      

#Obs: no hay que esperar que todos los elementos se terminen de generar para poder usarlos 

#otro ejemplo: sucesion de Fibonacci
def Fibonacci(limit):
    # 0 1 1 2 3 5 8 13...
    a,b = 0, 1
    while a < limit:
        yield a 
        a, b = b, a+b

fib=Fibonacci(30)
for i in fib:
    print(i)

#4) Generador para expresiones 
import sys
#caso generador de expresiones: utiliza '()' en lugar de '[]'
mygenerator = (i for i in range(1000) if i % 2 == 0) #coloca todos los valores pares en nuestro generador de 0 a 10 sin tomar en cuenta limite superior
#for i in mygenerator:
#   print(i)
#tambien se le puede transformar en una lista
#print(list(mygenerator))
print(sys.getsizeof(mygenerator))#resultado = 56

#caso tipico: 
mylist = [i for i in range(1000) if i % 2 == 0]
print(sys.getsizeof(mylist)) #resultado = 2132

'''

'''

#Threading & Multiprocessing

#Con estas opciones podemos correr codigos en paralelo y aumentar la velocidad de procesamiento

#Process: es una instancia del programa (e.g. interpretador de Python, FireFox).
#   Toma ventaja de los multiples CPUs y nucleos 
#   Separa automaticamante el espacio de memoria
#   procesos independientes
#   procesos son interrumpibles 
#   Empezar un proceso es mas lento que empezar un thread
#   Consume mas memoria  
#   un proceso puede contener varios threads


#Thread: es una entidad dentro de un proceso que puede ser programada (tambien conocida como proceso ligero)
#   todos los threads dentro de un proceso comparten el mismo espacio de memoria 
#   solo se puede ejecutar un thread a la vez 
#   no se puede interrumpir 
# muy utilizados para input/output tasks

#GIL: Global Interpreter Lock
#   es un seguro que permite ejecutar solamente un thread a la vez en Python 

#1) creacion de procesos 
from multiprocessing import Process
import os
import time

def square_numbers():
    for i in range(100):
        i*i
        time.sleep(0.1)

processes = [] #aqui vamos a almacenar todos los procesos 
num_processes = os.cpu_count() #generamos un proceso para cada nucleo de la computadora (child processes)

#creamos los procesos 
for i in range(num_processes):
    p = Process(target=square_numbers) #dentro de los argumentos de esta funcion, si nuestra funcion especificada necesita argumentos, los 
    processes.append(p)                                   #llamamos mediante 'args='

#inicio de procesos 
for p in processes:
    p.start()

#juntar los procesos: esperamos a que todos los procesos termine y con esto bloqueamos el thread principal 
for p in processes:
    p.join()

#esto se imprime solamente cuando los procesos terminan
print('end main')

#Cada nucleo trabaja en cada proceso

#2) multithreading 
from threading import Thread  
import os
import time

def square_numbers():
    for i in range(100):
        i*i
        time.sleep(0.1)

if __name__=="__main__":
    threads = []
    num_threads = 10 #(child threads)

#creacion de threads 
for i in range(num_threads):
    t = Thread(target=square_numbers)  
    threads.append(t)                                 

#inicio de procesos 
for t in threads:
    t.start()

#juntamos los threads
for t in threads:
    t.join() #en este caso el thread principal se bloquea hasta que la tarea este completa

#esto se imprime solamente cuando los threads terminan
print('end main')

#un solo nucleo genera 11 threads (el principal mas 10 child threads creados)

'''

'''

#3) compartir datos entre threads: esto se logra puesto que los threads comparten el mismo espacio de memoria 

from threading import Thread, Lock
import time

database_value = 0 #esto va a simular una base de datos (variable global)

def increase(lock):
    global database_value
    #queremos almacenar en una archivo local
    lock.acquire() #bloquea el estado y previene el cambio de thread (explicado abajo)
    local_copy = database_value
    #procesamiento
    local_copy +=1
    time.sleep(0.1) #simulamos un tiempo de procesesamiento 
    #queremos escribir nuestro nuevo valor en la base de datos 
    database_value = local_copy
    lock.release()

if __name__=="__main__":
    lock = Lock()
    print('start value', database_value)
    thread1 = Thread(target=increase, args=(lock,)) #se necesita la coma dentro de (lock,) para que Python sepa que es una tupla
    thread2 = Thread(target=increase, args=(lock,))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print('end value', database_value)

# Resultado: start value 0 end value 1. Tenemos dos threads y en realidad deberiamos tener "end value 2". No es asi, puesto que, al momento en que la ejecuccion 
#llega al comando 'time.sleep(0.1)' la maquina inteligentemente cambia al otro thread que va a ocuparse de este comando, pero inicia tambien su valor con 0
#ya que la anterior ejecuccion nunca llego al comando de reemplazo (database_value = local_copy)

#Obs: una 'race condition' ocurre cuando 2 o mas threads desean modificar una misma variable global al mismo tiempo

#3.1) para prevenir este error de cambio de thread: 
#from threading import Lock 
# y a continuacion creamos un Lock dentro del if antes de la creacion de los threads. Luego, agreagamos como variable este lock dentro de la funcion increase,
#agregamos la variable lock dentro del comando de creacion de cada thread 'Thread(target=increase, args=(lock,))'. Finalemente iniciamos y finalizamos el uso de
#lock con las sentencias 'lock.acquire()' y 'lock.release()'

#Resultado: start value 0 end value 2.

#Otra opcion para aplicar el lock en el comando impuesto a los threads (en lugar de 'lock.acquire()' y 'lock.release()'): 
#    with lock:
#        local_copy = database_value
#        local_copy +=1
#        time.sleep(0.1) 
#        database_value = local_copy 

#4) colas en Python: muy utilizado en Multithreading & Multiprocessing

from queue import Queue

#4.1) trabajo de una cola: es una extraccion de datos lineal que maneja el principio FIFO

if __name__=="__main__":
    q = Queue()
    #llenamos la cola
    q.put(1)
    q.put(2)
    q.put(3)

    #obtener primer elemento de la cola
    first = q.get()
    print(first)

    q.empty()

    #en ambiente de threading 
    q.task_done()
    q.join() #bloquea la cola hasta que todos los elementos dentro se hayan procesado


#ejemplo practico 

from threading import Thread, Lock, current_thread
from queue import Queue

def worker(q): #loop infinito
    while True:
        value = q.get() # al inicio el proceso se bloquea puesto que no hay elementos en la cola q
        #processing...
        print(f'in {current_thread().name} got {value}')
        q.task_done()

if __name__=="__main__":
    q = Queue()
    num_threads = 10 

    for i in range(num_threads):
        thread = Thread(target=worker, args=(q,))
        thread.daemon = True #simula un thread de trasfondo al main y hace que finalice el loop infinito
        thread.start()

    for i in range(1, 21): #ingresamos 20 elementos a las colas 
        q.put(i)
    
    q.join()

    print("End main")

#el resultado arroja un orden no secuencial pero no es importante 

'''

'''

#5) Multiprocessing
#Recordemos que los procesos no comparten el mismo espacio de memoria, por tanto no comparten datos publicos. Vamos a ver objetos especiales 
#que permiten compartir datos entre procesos 

#5.1)Share memory objects: podemos utilizar objetos para un solo valor o para un arreglo 

#a) para un solo valor: 'from multiprocessing import Value'

from multiprocessing import Process, Value, Array, Lock 
import time 

def add_100(number, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire() #fija el proceso que entra en esta funcion y se asegura que termine sin que otro proceso interrumpa 
        number.value += 1
        lock.release() #termina el lock de proceso
        #recordar que tambien se utiliza lo siguiente en lugar de lock.acquire() y lock.release()
        #with lock:
        #number.value += 1       

if __name__ == "__main__":
    
    lock = Lock()
    shared_number = Value('i', 0) # debemos dar un tipo de dato ('i' denota entero) y un valor de estado inicial (en este caso 0)
    print('Value at beginning:', shared_number.value) # share_number.value = 0

    #creacion procesos que modifiquen este numero inicial 
    p1 = Process(target=add_100, args=(shared_number,lock))
    p2 = Process(target=add_100, args=(shared_number,lock))

    #inicio procesos 
    p1.start()
    p2.start()

    #join procesos
    p1.join()
    p2.join()

    print('Number at the end is: ', shared_number.value)

# Obs: Notemos que el programa arroja valores distintos cada vez que se ejecuta. Esto se debe a una 'race condition', es decir 2 o mas procesos 
# intentan modificar el mismo dato (shared_value) al mismo tiempo, por lo que algunas operaciones dentro de la funcion add_100 se pierden. 
# Para prevenir esto utilizamos el 'lock'    


#b) para un array: 'from multiprocessing import Array'


from multiprocessing import Process, Value, Array, Lock 
import time 

def add_100(numbers, lock):
    for i in range(100):
        time.sleep(0.01)
        for i in range(len(numbers)):
            with lock:
                numbers[i] += 1

        
    #creacion procesos que modifiquen este numero inicial 
if __name__ == "__main__":
    
    lock = Lock()
    shared_array = Array('d',[0.0, 100.0, 200.0]) # debemos dar un tipo de dato ('i' denota entero) y un valor de estado inicial (en este caso 0)
    print('array at beginning is:', shared_array[:]) # share_number.value = 0

    #creacion procesos que modifiquen este numero inicial 
    p1 = Process(target=add_100, args=(shared_array,lock))
    p2 = Process(target=add_100, args=(shared_array,lock))

    #inicio procesos 
    p1.start()
    p2.start()

    #join procesos
    p1.join()
    p2.join()

    print('array at the end is: ', shared_array[:])  

'''

#5.2) utilizando colas en multiprocessing: podemos correr dos funciones distintas al mismo tiempo 

from multiprocessing import Process, Value, Array, Lock 
from multiprocessing import Queue
import time 

def square(numbers, queue):
    for i in numbers:
        queue.put(i*i)

def make_negative(numbers, queue):
    for i in numbers:
        queue.put(-1*i)
        
if __name__ == "__main__":
    
    numbers = range(1,6)
    q = Queue()

    #creacion procesos que modifiquen este numero inicial 
    p1 = Process(target=square, args=(numbers,q))
    p2 = Process(target=make_negative, args=(numbers,q))

    #inicio procesos 
    p1.start()
    p2.start()

    #join procesos
    p1.join()
    p2.join()

    #no hay funcion de join para queues, pero se puede hacer lo siguiente
    while not q.empty():
        print(q.get())
    #esto se envargara de tratar el proceso dentro de la cola y luego vaciar la cola 



#5.3) Process Pool: puede ser utilizado para manejar varios procesos     

from multiprocessing import Pool
from multiprocessing import Queue
import time 

def cube(number):
    return number*number*number
        
if __name__ == "__main__":
    
    numbers = range(20)
    pool = Pool()

    #metodos utilizados en 'Pool': map, apply, join, close
    result = pool.map(cube, numbers) #la funcion 'cube' se va a ejecutar en paralelo por todos los procesadores disponibles
    #si queremos que solo una funcion se ejecute:
    #pool.apply(cube, numbers[0])

    pool.close()
    pool.join()
    print(result)

#El 'Pool' automaticamente llama al numero maximo de procesadores y crea diferentes procesos para procesar la funcion en paralelo
