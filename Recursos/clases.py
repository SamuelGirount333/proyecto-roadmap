### Clases de python ###

# Definicion 

class MyEmptyperson:
    pass

print(MyEmptyperson)
print(type(MyEmptyperson))

print('--'*50)

# Clase con constructor 
"""
Al hacer uso del def __init__(self) estamos directamente un constructor de clase 
se puede llegar a pensar de que seria una funcion pero teniendo en cuenta que se 
esta definiendo dentro de una clase y se esta haciendo uso de (__init__) damos por 
sentado que es un lugar donde podemos almacenar los atributos de clase que estamos definiendo 

# self (Atributos de la clase)

se refiere a las propiedades del objeto al cual estamos definiendo en nuesta clase 
en este caso concreto el objeto es persona 


"""

class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

my_person = Person('samuel','gomez')
print(f"{my_person.name} {my_person.surname}")