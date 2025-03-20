#Cadenas de caracteres 
'''
Manipular cadenas de caracteres en python:

en python podemos crear cadenas de caracters declarando una variable mediante 
palbra = 'this is strings in python'

manipular cadenas en python juega un papel fundamental en la mayoria de las tareas de procesamiento de 
texto.
'''

# primera cadena 
mensaje = 'Hola mundo'
print(mensaje)


# Operadores de cadenas
"""
Una cadena de caracteres en un objeto que consiste precisamente en una serie de signos o caracteres.
Python sabe como tratar un numero de representacion poderosas y de proposito general incluidas las cadenas 
de caracteres es utilizar  operadores de cadenas de caracteres (strings). Una forma de manipular las cadenas
de caracteres. Dichos operadores se presentan como simbolos que asociamos con las matematicas, como +, -, *, / 
y el =. estos signos  realizan acciones similares a sus contrapartes matematicas cuando se usan en las cadenas
de caracteres, aunque no iguales.
"""
print('--'* 50)

#Concatenar
mensaje1 = 'Hola' + ' ' +  'Mundo'
print(mensaje1)

# Multiplicar 
''''
Si quieres varias copias de una cadena de caracteres el operador de multiplicacion(*)
en este ejemplo, la cadena de caracteres lleva contenido 'Hola' tres veces, mientras que la
cadena de caracteres mensaje 2b tiene el contenido "Mundo" 
'''

mensaje2 = 'Hola' * 3
mensaje2b = "Mundo"
print(mensaje2 + mensaje2b)

# Añadir

'''
¿Qué pasa si quieres añadir material de manera sucesiva al final de una cadena de caracteres? 
El operador especial para ello es compuesto (+=).
'''

mensaje3 = 'Hola'
mensaje3 += ' '
mensaje3 += 'Mundo'
print(mensaje3)

# Metodos de cadenas 
'''
En adición a los operadores, Python trae preinstalado docenas de métodos que 
te permiten hacer cosas con las cadenas de caracteres. 
Solos o en combinación, los métodos pueden hacer casi todo lo que te imagines 
con las cadenas de caracteres. 
Puedes usar como referencia la lista de métodos de cadenas de caracteres (String Methods) 
en el sitio web de Python, que incluye información de cómo utilizar correctamente cada uno.
Para asegurar que tengas una comprensión básica de métodos para cadenas de caracteres, 
lo que sigue es una breve descripción de los utilizados más comúnmente.
'''
# Cadenas de caracteres en Python
"""
Las cadenas en Python son secuencias inmutables de caracteres.
Se pueden definir con comillas simples, dobles o triples.
"""

# Creación de cadenas
cadena1 = 'Hola, mundo!'
cadena2 = "Python es genial"
cadena3 = '''Texto con varias líneas'''
cadena4 = """Otra forma de escribir cadenas multilínea"""
print(cadena1, cadena2, cadena3, cadena4)

# Métodos de modificación
texto = " hola mundo "
print(texto.upper())  # " HOLA MUNDO "
print(texto.lower())  # " hola mundo "
print(texto.capitalize())  # " Hola mundo "
print(texto.title())  # " Hola Mundo "
print(texto.strip())  # "hola mundo"
print(texto.replace("mundo", "Python"))  # " hola Python "
print("-".join(["Python", "es", "genial"]))  # "Python-es-genial"

# Métodos de búsqueda
texto = "Python es increíble"
print(texto.startswith("Python"))  # True
print(texto.endswith("increíble"))  # True
print(texto.find("es"))  # 7
print(texto.count("e"))  # 3
print("12345".isdigit())  # True
print("Python".isalpha())  # True
print("Python123".isalnum())  # True

# Indexación y segmentación
texto = "Python"
print(texto[0])  # 'P'
print(texto[-1])  # 'n'
print(texto[1:4])  # 'yth'
print(texto[::-1])  # 'nohtyP'

# Concatenación y repetición
nombre = "Juan"
apellido = "Pérez"
print(nombre + " " + apellido)  # "Juan Pérez"
print(nombre * 3)  # "JuanJuanJuan"

# Interpolación de cadenas
nombre = "Ana"
edad = 25
print("Mi nombre es {} y tengo {} años".format(nombre, edad))
print(f"Mi nombre es {nombre} y tengo {edad} años")
print("Mi nombre es %s y tengo %d años" % (nombre, edad))
print("mis cambios  del repo github")
"""
Extra
"""
def check(word1: str, word2: str):

    # Palíndromos
    print(f"¿{word1} es un palíndromo?: {word1 == word1[::-1]}")
    print(f"¿{word2} es un palíndromo?: {word2 == word2[::-1]}")

    # Anagramas
    print(f"¿{word1} es anagrama de {word2}?: {sorted(word1) == sorted(word2)}")

    # Isogramas

    def isogram(word: str) -> bool:

        word_dict = dict()
        for character in word:
            word_dict[character] = word_dict.get(character, 0) + 1

        isogram = True
        values = list(word_dict.values())
        isogram_len = values[0]
        for word_count in values:
            if word_count != isogram_len:
                isogram = False
                break

        return isogram

    print(f"¿{word1} es un isograma?: {isogram(word1)}")
    print(f"¿{word2} es un isograma?: {isogram(word2)}")


check("radar", "pythonpythonpythonpython")
print('esto es una prueba de guardado de los cambios')
print('esto es una prueba de guardado de los cambios2')
print('esto es una prueba de guardado de los cambios3')