##1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 
#(incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
for i in range(101):
  print (i)
  
#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de 
#dígitos que contiene. 

num = input("Por favor ingrese un numero entero: ")
print(f"Este numero tiene {len(num)} digitos")

#3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores 
#dados por el usuario, excluyendo esos dos valores.

num3 = int(input("Ingrese un numero entero "))
num4 = int(input("Ingrese otro numero entero diferente "))
sumatoria2 = 0
print(f"A continuacion se mostrara la sumatoria de los numeros comprendidos entre {num3} y {num4}")
for j in range(num3+1,num4):
  sumatoria2 += j
print(sumatoria2)

#4) Elabora un programa que permita al usuario ingresar números enteros y los sume en 
#secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese 
#un 0. 

num2 = int(input("Por favor ingrese numeros enteros y se mostrara la suma de los mismos. Para finalizar, ingrese el 0 "))
sumatoria = 0
while num2 != 0:
  sumatoria += num2
  num2 = int(input("Ingrese otro numero "))
print(f"La sumatoria total es igual a {sumatoria}")

#5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el 
#programa debe mostrar cuántos intentos fueron necesarios para acertar el número.
import random
num_aleatorio = random.randint(0,9)
print("A continuacion ingrese numeros entre 0 y 9 para descubrir cual es el numero secreto! ")
intentos = 0
num5 = int(input("Ingresar numero --> "))
while num5 != num_aleatorio:
  print("Incorrecto! intente nuevamente ")
  num5 = int(input("Ingresar --> "))
  intentos += 1
print(f"Exito! el numero secreto era {num_aleatorio}. Lo descubriste en {intentos} intentos!")

#6)Desarrolla un programa que imprima en pantalla todos los números pares comprendidos 
#entre 0 y 100, en orden decreciente. 
for a in range(100,-2,-2):
 print(a)
 
 #7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un 
#número entero positivo indicado por el usuario. 
num6 = int(input("Por favor ingrese un numero entero "))
sumatoria3 = 0
print(f"A continuacion se mostraran los numeros comprendidos entre 0 y {num6} (el numero que usted ingreso)")
for b in range(0,num6):
  sumatoria3 += b
print(f"La sumatoria final es {sumatoria3}")

#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el 
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son 
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad 
#menor, pero debe estar preparado para procesar 100 números con un solo cambio). 
numeros_pares = 0
numeros_impares = 0
numeros_neg = 0
numeros_pos = 0
for c in range(100):
  num7 = int(input("Ingrese un numero "))
  if num7 % 2 == 0:
    numeros_pares += 1
  else:
    numeros_impares +=1
  if num7 > 0:
    numeros_pos +=1
  else:
    numeros_neg += 1
print(f"Usted ingreso {numeros_pares} numeros pares, {numeros_impares} numeros impares, {numeros_neg} numeros negativos y {numeros_pos} numeros positivos")

#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la 
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe 
#poder procesar 100 números cambiando solo un valor).
print("Ingrese 100 numeros enteros y se le calculara el promedio a esos valores")
sum_ej9 = 0
for i in range(100):
  sum_ej9 += int(input("Ingrese un numero --> "))
promedio = sum_ej9/10
print(f"El promedio es {promedio}")

#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el 
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

ej10 = input("Por favor ingrese un numero. Se le devolvera el inverso del mismo: ")
ej10_invertido = ""
for i in ej10[::-1]: #Con esto recorro el str numero de atras hacia adelante
  ej10_invertido += i
print(f"El numero invertido es {ej10_invertido}")