import random

feet_in_mile = 5280
meters_in_kilometer = 1000
beatles = ["John Lennon", "Paul Mcartney", "George Harrison", "Ringo Star"]

def get_file_ext(filename): #nos da la extension de un archivo
    return filename[filename.index(".") + 1:]

def roll_dice(num):#bota un valor aleatorio entero, 'num' es el numero maximo que se considera  
    return random.randint(1, num)

