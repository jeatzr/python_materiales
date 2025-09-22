# numéricos
edad = 25          # entero 
altura = 1.75      # flotante
peso = 70.5        # flotante
temperatura = -5.0 # flotante negativo
pi = 3.14159      # flotante

# cadenas de texto
nombre = "Juan"               # cadena con comillas dobles
apellido = 'Pérez'            # cadena con comillas simples
mensaje = """Hola,
  ¿Cómo estás?

  hasta luego"""  # cadena con comillas triples

print("Nombre:", nombre)
print('Mensaje:', mensaje)

# booleanos
es_estudiante = True   # valor booleano verdadero
tiene_mascota = False  # valor booleano falso 

if es_estudiante:
    print(nombre, "es estudiante.") 
else:
    print(nombre, "no es estudiante.")

print(f"El número PI con dos decimales: {pi:.2f}")