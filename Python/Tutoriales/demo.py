#Demo tutorial (https://www.youtube.com/watch?v=rfscVS0vtbw&t=7285s&ab_channel=freeCodeCamp.org)

'''

# calculadora utilizando if
num1 = float(input("Enter the first number: "))
op = input("Enter operator (+,-,*,/): ")
num2 = float(input("Enter the second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("Invalid operator.")

'''

'''

#Diccionarios (creacion de Key Value Pairs)
# queremos transformar Jan -> January o Mar -> March 
monthConversion = {
    "Jan": "January",#Jan es la Key y January es el value. Las Keys deben ser unicas dentro del diccionario 
    "Feb": "February",
    "Mar": "March",# tambien podemos utilizar valores numericos como Keys
    "Abr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Nov": "November",
    "Dec": "December",
}
#Para acceder al diccionario 
print(monthConversion["Feb"])
#Otra forma 
print(monthConversion.get("Aug"))
#Ganancia de utilizar '.get' es que, si introducimos un valor erroneo, nos regresa "None", es decir nos regresa un valor de Default:
print(monthConversion.get("AUV"))
# Podemos utilizar este valor de Default de la siguiente manera:
print(monthConversion.get("LA","Not a valid key"))

'''
'''

#Lazos while: nos deja ejecutar codigos varias veces 
i=1 
while i <= 10: 
    print(i, "is less or equal to 10")
    i+=1
print("i is greater than 10")

'''
'''
#Construir un juego de adivinanzas con while loops con tres intentos 
secret_word = "Taco"
guess = ""
guess_count=0
guess_limit=3
out_of_guesses=False


while secret_word!=guess and out_of_guesses==False:
    if guess_count<guess_limit:
        guess=input("Enter the secret word: ")
        guess_count+=1
    else:
        out_of_guesses=True

if out_of_guesses:
    print("Out of guesses. You lose!")
else:
    print("Correct!")
'''

'''

#for loop
# Primer caso
friends=["Paul", "Teresa", "Bryan", "Carlos"]
for friend in friends:
    print(friend)

# Variacion del primer caso con 'range' y 'len'
for friend in range(len(friends)):
    print(friends[friend])

#Segundo caso
for letter in "Ecuador":
    print(letter)

#Tercer caso
for index in range(3, 10):
    print(index)

#Solo imprimir primer caso como correcto 
for index in range(5):
    if index==0:
        print("first iteration")
    else:
        print("not first")

'''

'''

#funcion exponencial 
def exp_function(base_num,power_num):
    result = 1
    for index in range(power_num):
        result=result*base_num
    return result

print(exp_function(2,8))

#codigo abreviado 
print(2**8)

'''

'''

#2D lists and nested loops: listas dentro de listas y lazos anidados

#lista dentro de lista 
number_grid =[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]
print(number_grid[3][0])

#lazo anidado de for
for row in number_grid:
    for col in row:
        print(col)

#Construir un traductor: cambiar todas las vocales por 'g' o 'G'
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou": # tambien puede ser if letter.lower() in "aeiou":
           # if letter.isupper():
                translation=translation+"G" #PUEDE REEMPLAZAR UNA MAYUSCULA POR UNA g MINUSCULA (por ende, incluimos el if precedente)
            else:
                translation=translation+"g"
        else:
            translation=translation+letter
    return translation

print(translate(input("Enter a phrase: "))) 

'''

'''
#Sentencias Try/Except: Aceptacion o no de un codigo en especifico 

#En este caso estamos obligando al programa a introducir un numero, caso contrario nos bota un error de codigo. 
#Utilizando Try/Except, podemos personalizar el error que nos bota el programa. Por ende podemos proteger nuestro programa
try:
    number=int(input("Enter a number: "))
    print(number)
except:
    print("Invalid input")

#Otro ejemplo 
try:
    value=10/0 #el programa bota un error de calculo 
except ZeroDivisionError as err: #se puede especificar el tipo de error aumentando el codigo 'as err' y cambiando el print
    print(err)
except ValueError:
    print("Invalid input")
#En este caso, el error proviene por algo ilogico y no por algo invalido, por lo que es necesario especificar el tipo de error. 
#Para el ejemplo anterior utilizamos 'except ZeroDivisionError' y 'except ValueError'. Asi, podemos especificar el tipo de 
#excepciones que manejamos


'''

'''
#abrir/cerrar documentos 
trans_file=open("translator.txt","r")
print(trans_file.readable()) #booleano para ver si podemos leer o no el documento 
print(trans_file.read())#ver contenido del documento
print(trans_file.readline())#ver primera linea. Si juntamos otra vez esta sentencia de manera seguida obtenemos las 2 primeras lineas
print(trans_file.readlines())#muestra todas las lineas del documento en formato de lista 

for translator in trans_file.readlines():#lazo for que permite obtener uno a uno los elementos generados por 'trans_file.readlines()'
   print(translator) 
trans_file.close()
'''
'''
#escribir y anadir texto en archivos
trans_file=open("translator.txt","a")#'a' es 'append' = anadir al final del texto 
#si el archivo indicado no existe, y ademas se utiliza 'w', Python creara un nuevo archivo con este nombre 
#anadiendo el texto indicado 
trans_file.write("Perro -> Pgrrg")#anade este texto a continuacion del texto ya escrito y cada vez que corremos el codigo
trans_file.write("\nTren -> Trgn")#'\n' anade el texto en una nuevca linea 
trans_file.close()
'''

'''

#Modules: conecta archivos externos para utilizar su codigo en un archivo actual 
#vamos a utilizar el archivo 'useful_tools.py': vamos a importar las variables y funciones de este archivo 
import useful_tools
print(useful_tools.roll_dice(10))

#existe una lista de todos los modulos disponibles en Python (Python module index), entonces para importar archivos .py externos se utiliza 'external modules' en PyCharm
# o se utiliza el package manager 'pip': 'pip install python-docx' utilizando el command prompt o la terminal de WIN

'''

'''
#clases y objetos 

#Clases: sirven para crear nuestro propio tipo de data 
#Vamos a crear un tipo de dato 'student' (objeto) a partir de la clase dentro del archivo 'student.py' que contiene varios 
#atributos (name, major, grade, is_on_probation)
from student import student #el primer 'student' es el archivo, el segundo es la clase 
student1=student("Jim", "Math", 16, False)
student2=student("Bryan", "Physics", 20, True)
print(student1.grade)
print(student2.is_on_probation)
'''

'''
#Ejercicio: examen de opcion multiple 
from preguntas_examen import preguntas_examen

question_prompts = [
"What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
"What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
"What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

#representar las preguntas presentes en el examen: Vamos a crear una clase 'preguntas' 
#para almacenar las preguntas y las respuestas 

questions =[ #creamos un array de preguntas
    preguntas_examen(question_prompts[0], "a"),
    preguntas_examen(question_prompts[1], "c"),
    preguntas_examen(question_prompts[2], "b"),
]

def correr_examen(questions):
    score=0 #contador para respuestas correctas 
    for question in questions: #loop para presentar cada pregunta 
        answer=input(question.pregunta) #variable donde se almacena la respuesta
        if answer == question.respuesta: #ver si la respuesta es correcta 
            score +=1
    print("Obtuvo " + str(score) + "/" + str(len(questions)) + " respuestas correctas")

correr_examen(questions)
'''
'''
#Funciones clases: poner funciones dentro de clases

#Vamos a utilizar el archivo 'student.py' para incluir dentro de esta clase una funcion para determinar 
#si un estudiante tiene honores o no

from student import student #el primer 'student' es el archivo, el segundo es la clase 
student1=student("Jim", "Math", 16, False)
student2=student("Bryan", "Physics", 20, True)

print(student2.honores())
'''

#Inheritance (herencia): Crear una segunda clase que herede todos los atributos de una clase primaria
#Utilizaremos el archivo 'chef.py' y la heredaremos hacia el archivo 'ChineseChef.py'
from Tutoriales.Chef import Chef
#Clase herencia 
from Tutoriales.ChineseChef import ChineseChef

myChef = Chef()
myChef.make_chicken()

#Ahora vamos a crear otra clase para otro tipo de Chef mas especializado ('ChineseChef.py'):
myChineseChef = ChineseChef()
myChineseChef.make_fried_rice()
myChineseChef.make_special_dish()
myChef.make_special_dish()