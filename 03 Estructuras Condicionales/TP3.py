#1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
#deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.

edad = int(input("Ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad")
else:
    print("No es mayor de edad")

#2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá 
#mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el  mensaje “Desaprobado”. 

nota = float(input("Por favor ingrese la nota que obutvo: "))
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
    
#3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un 
#número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso 
#contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del 
#operador de módulo (%) en Python para evaluar si un número es par o impar.

num = int(input("Ingrese numeros pares: "))
while num % 2 != 0:   
    print("Por favor, ingrese un número par")
    num = int(input("Nuevo numero: "))
print("Ha ingresado un número par")

#4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las 
#siguientes categorías pertenece: 
#● Niño/a: menor de 12 años. 
#● Adolescente: mayor o igual que 12 años y menor que 18 años. 
#● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. 
#● Adulto/a: mayor o igual que 30 años.

edad2 = int(input("Por favor ingrese su edad: "))
if edad2 <= 12:
    print("Niño/a")
elif edad2 >= 12 and edad2 <= 18:
    print("Adolescente")
elif edad2 >= 18 and edad2 < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a mayor")
    
#5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres 
#(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en 
#pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por 
#pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso 
#de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal 
#como una lista o un string.

contraseña = input("Ingrese una contraseña de entre 8 y 14 caracteres")
largo_contraseña = len(contraseña)
if largo_contraseña >= 8 and largo_contraseña <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
    
#6) El paquete statistics de python contiene funciones que permiten tomar una lista de números 
#y calcular la moda, la mediana y la media de dichos números. Un ejemplo de su uso es el  siguiente: 
from statistics import median, mode, mean
import random
numeros_aleatorios = random.randint[(1,100 for i in range(50))]

#escribir un programa que tome la lista 
#numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si 
#hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla. 
#Definir la lista numeros_aleatorios de la siguiente forma:
numeros_aleatorios = [random.randint(1, 100) for i in range(50)] 
moda = mode(numeros_aleatorios)
print(f"La moda es: {moda}")
mediana = median(numeros_aleatorios)
print(f"La mediana es: {mediana}")
media = mean(numeros_aleatorios)
print(f"La media es: {media}")
if media > mediana and mediana > moda:
    print("Sesgo positivo")
elif media < mediana and mediana < moda:
    print("Sesgo negativo")
elif media == mediana and mediana == moda:
    print("Sin sesgo")
    
#7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado 
#termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por 
#pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla. 

frase = input("Por favor ingrese una frase o palabra ")
ultima_letra = frase[len(frase)-1:len(frase)] #Aca me quedo con la ultima letra de la frase
ultima_letra = ultima_letra.lower() #Aca transformo en minuscula la ultima letra para evaluar con el condicional de mas abajo
if ultima_letra in ("a","e","i","o","u"):
  print(frase + "!")
else:
  print(frase)
  
#8)Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 
#dependiendo de la opción que desee: 
#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
#El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
#usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
#lower() y title() de Python para convertir entre mayúsculas y minúsculas.
print("Ingrese su nombre y el numero 1,2 o 3 si usted quiere")
print("#1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.")
print("#2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.")
print("#3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.")
ej_8 = input("Nombre: ")
num_ej8 = int(input("Numero: "))
if num_ej8 == 1:
  print(ej_8.upper())
elif num_ej8 == 2:
  print(ej_8.lower())
else:
  print(ej_8.title())
  
#9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la 
#magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado 
#por pantalla: 
#● Menor que 3: "Muy leve" (imperceptible). 
#● Mayor o igual que 3  y menor que 4: "Leve" (ligeramente perceptible). 
#● Mayor o igual que 4  y menor que 5: "Moderado" (sentido por personas, pero 
#generalmente no causa daños). 
#● Mayor o igual que 5  y menor que 6: "Fuerte" (puede causar daños en estructuras 
#débiles). 
#● Mayor o igual que 6  y menor que 7: "Muy Fuerte" (puede causar daños significativos). 
#● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala). 

magnitud = int(input("Ingrese por favor la magnitud del terremoto: "))
if magnitud < 3:
  print("Muy leve (Imperceptible)")
elif magnitud >= 3 and magnitud < 4:
  print("Leve (ligeramente perceptible)")
elif magnitud >= 4 and magnitud < 5:
  print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud >= 5 and magnitud < 6:
  print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud >=6 and magnitud < 7:
  print("Muy Fuerte (puede causar daños significativos)")
else:
  print("Extremo (puede causar graves daños a gran escala)")
  
# 10)Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes 
#del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla 
#si el usuario se encuentra en otoño, invierno, primavera o verano.
hemisferio = input("Por favor ingrese en que hemisferio se encuentra (N/S)")
hemisferio = hemisferio.upper() #Hago mayuscula la letra para despues compararla
mes = input("Ingrese el mes en el cual se encuentra ")
mes = mes.title() #La primera en mayuscula
dia = int(input("Ingrese que dia es "))

#armo un diccionario con los meses asi a traves del par "clave:valor" llamo al mes en forma de "int"

dict_meses = {"Enero": 1,
              "Febrero": 2,
              "Marzo": 3,
              "Abril": 4,
              "Mayo": 5,
              "Junio": 6,
              "Julio": 7,
              "Agosto": 8,
              "Septiembre": 9,
              "Octubre": 10,
              "Noviembre": 11,
              "Diciembre": 12}

if hemisferio == "N":
 if (dict_meses[mes] == 3 and dia >= 21) or (3 < dict_meses[mes] < 6) or (dict_meses[mes] == 6 and dia <= 20):
     estacion = "Primavera"
 elif (dict_meses[mes] == 6 and dia >= 21) or (6 < dict_meses[mes] < 9) or (dict_meses[mes] == 9 and dia <= 22):
     estacion = "Verano"
 elif (dict_meses[mes] == 9 and dia >= 23) or (9 < dict_meses[mes] < 12) or (dict_meses[mes] == 12 and dia <= 20):
     estacion = "Otoño"
 else:
     estacion = "Invierno"
elif hemisferio == "S":
 if (dict_meses[mes] == 9 and dia >= 21) or (9 < dict_meses[mes] < 12) or (dict_meses[mes] == 12 and dia <= 20):
     estacion = "Primavera"
 elif (dict_meses[mes] == 12 and dia >= 21) or (1 <= dict_meses[mes] < 3) or (dict_meses[mes] == 3 and dia <= 20):
     estacion = "Verano"
 elif (dict_meses[mes] == 3 and dia >= 21) or (3 < dict_meses[mes] < 6) or (dict_meses[mes] == 6 and dia <= 20):
     estacion = "Otoño"
 else:
     estacion = "Invierno"
print(f"La estacion en la que usted se encuentra el {dia} de {mes} en el hemisferio {hemisferio} es {estacion}")