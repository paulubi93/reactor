class student:
    def __init__(self, name, major, grade, is_on_probation): #funcion inicializadora (constructor) necesaria siempre que se crea una clase
        self.name=name 
        self.major=major
        self.grade=grade
        self.is_on_probation=is_on_probation

#self.name, self.major,... son atributos que se le dan a la clase 'student'. El 'self' nos ayuda a transformar 'valores'
#en 'atributos' de la clase, esto nos permite utilizarlos externamente en otros archivos 

#Para la parte de funciones clases 
#Definimos una funcion que permita ver si el estudiante tiene honores 
    def honores(self):
        if self.grade >=17:
            return True
        else:
             return False