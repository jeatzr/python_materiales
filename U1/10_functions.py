def saludo(nombre="Usuario"):
  """Esta función devuelve una cadena de saludo 'hola, nombre'"""
  return f"Hola, {nombre}"

print(saludo("Juanito"))
print(saludo())

def fib(n):    # escribir la serie de fibonacci por debajo de n
    """Print a Fibonacci series less than n."""
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a+b
    print()

# Llamamos la función
fib(10000)

def sumar(*numeros):
    total = sum(numeros)
    print(f"La suma es {total}")

sumar(2)
sumar(4, 3, 4)
sumar(1, 2, 3, 4, 5, 5, 5, 5, 35)

def mostrar_info(**info):
    for clave, valor in info.items():
        print(f"{clave}: {valor}")

mostrar_info(nombre="Ana", edad=25, ciudad="Madrid", estudios="FP")