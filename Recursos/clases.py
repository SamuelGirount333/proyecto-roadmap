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
    def __init__(self, name, surname, alias="Sin alias"):
        self.full_name = f"{name} {surname} ({alias})"  # Propiedad pública
        self.__name = name  # Propiedad privada

    def get_name(self):
        return self.__name

    def walk(self):
        print(f"{self.full_name} está caminando")


my_person = Person("samuel;", "Gomez")
print(my_person.full_name)
print(my_person.get_name())
my_person.walk()

my_other_person = Person("Samuel", "Gomez", "Sam-Sam")
print(my_other_person.full_name)
my_other_person.walk()
my_other_person.full_name = "Hugo Hernan Hernadez Henao "
print(my_other_person.full_name)

my_other_person.full_name = 666
print(my_other_person.full_name)