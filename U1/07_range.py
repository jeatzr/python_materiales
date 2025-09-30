rango_numeros = range(11)
rango_numeros_2 = range (6,20)
rango_numeros_3 = range (20,6,-2)

lista_n1, lista_n2, lista_n3 = list(rango_numeros), list(rango_numeros_2), list(rango_numeros_3)

print (rango_numeros,rango_numeros_2, rango_numeros_3)

print (lista_n1, lista_n2, lista_n3)

for n in rango_numeros:
  print(f"{n} * 6 = {n * 6} ")
