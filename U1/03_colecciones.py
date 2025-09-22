lista = [1, 2, 3]
tupla = (1, 2, 3)
diccionario = {"nombre": "Ana", 
               "edad": 30,
               "ciudad": "Madrid",
               "es_estudiante": False,
               "notas": [8.5, 9.0, 7.5]}  # Diccionario con varios tipos de valores 

conjunto = {1, 2, 3}

print("Lista:", lista)
print("Tupla:", tupla)
print("Diccionario:", diccionario)
print("Conjunto:", conjunto)  

print(diccionario["nombre"])  # Acceder al valor asociado a la clave "nombre"

lista.append(4)  # Agregar un elemento a la lista
print("Lista después de agregar un elemento:", lista)