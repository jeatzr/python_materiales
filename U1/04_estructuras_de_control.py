edad = 18

if edad >= 18:
  print("Puedes entrar")
else:
  print("No puedes entrar")

nombre = "Pepe"

if nombre == "Pepe":
  print("Hola Pepe")
elif nombre == "Manolo":
  print("Hola Manolo")
else:
  print("No eres ni Pepe ni Manolo, no puedes entrar")

# Bucles

for i in range(5):
  print(i)

print ("De 1 a 10:")
for i in range(1,11):
  print(i)

print("Números pares de 20 a 44 inclusive ambos")
for i in range(20,45):
  if (i%2 == 0 ):
    print(i)

for i in range(20,45,2):
  print(i)

lista = ["gato","perro","canario","caimán","oso polar"]

for pet in lista:
  print(pet)


