while True:
    try:
        edad = int(input("Introduce tu edad: "))
        break
    except ValueError:
        print("⚠️ Eso no es un número entero, inténtalo de nuevo.")

print(f"Tu edad es {edad}")