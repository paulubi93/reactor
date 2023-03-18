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

# Logging 

#Hola 