#Ejercicio 1)
lista = []
for i in range(1,104):
  if i % 4 == 0:
   lista.append(i)
print(f"Multiplos de 4 de 1 a 100: {lista}")

#Ejercicio 2)
lista_2 = ["Musica",8,"Deporte","Mates",True]
print(lista_2[3])
print(f"Indexing con numeros negativos: {lista_2[-2]}")

#Ejercicio 3)
lista_3 = []
print("La siguiente lista esta vacia", lista_3)
for x in range(1):
  lista_3.append("Viernes")
  lista_3.append("Soda")
  lista_3.append("Comida")
print("Lista con palabras agregadas: ",lista_3)

#Ejercicio 4)
animales = ["perro", "gato", "conejo", "pez"] 
print(animales)
animales[1] = "loro"
animales[-1] = "oso"
print(f"Animales con palabras reemplazadas ", animales)

#Ejercicio 5)
print("El comando remove() en una lista elimina elementos pero no por indices, sino por valor. Entonces al escribir el codigo")
print("numeros.remove(max(numeros)) buscara en la lista numeros el maximo de ellos y lo eliminará.")

#Ejercicio 6)
lista_4 = []
for i in range(10,35,5):
  lista_4.append(i)
print(lista_4[:2])

#Ejercicio 7)
autos = ["sedan", "polo", "suran", "gol"]
print(autos)
autos[1], autos[2] = "celta", "corsa"
print(autos)

#Ejercicio 8)
dobles = []
for i in range(1):
  dobles.append(5*2)
  dobles.append(10*2)
  dobles.append(15*2)
print(dobles)

#Ejercicio 9)
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]] 
compras[2].append("jugo")
compras[1][1] = "tallarines"
compras[0].remove("pan")
print(f"Lista resultante: ",compras)

#Ejercicio 10)
lista_anidada = [15,True, [25.5,57.9,30.6],False]
print(lista_anidada)