#Aqui tenemos una clase heredada del archivo 'Chef.py'
from Chef import Chef

class ChineseChef(Chef):

    def make_fried_rice(self):
        print("The chef makes fried rice")

#se puede reescribir funciones definidas en la clase base 'Chef':
    def make_special_dish(self):
        print("The chef makes orange chicken")

    