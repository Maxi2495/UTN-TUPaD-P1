#Ejercicio 1)
def imprimir_hola_mundo():
    print("Hola Mundo!")
    
#Ejercicio 2)    
def saludar_usuario(nombre):
 return print(f"Hola {nombre}, estamos muy contentos de saludarte")

#Ejercicio 3

def informacion_personal(nombre, apellido, edad, residencia):
 print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")
 
 #Ejercicio 4
 
def calcular_area_circulo(radio):
  import math
  area = math.pi * (radio**2)
  return print(f"El area de un circulo de radio {radio} es {round(area,2)}")

def calcular_perimetro_circulo(radio):
  import math
  perimetro = 2 * math.pi * (radio)
  return print(f"El perimetro de un circulo de radio {radio} es {round(perimetro,2)}")

#Ejercicio 5

def segundos_a_horas(segundos):
 conversor_a_horas = segundos / 3600 #3600 segundos --> 1 hora
 return print(f"La cantidad de segundos ingresada equivale a {round(conversor_a_horas,2)} horas")

#Ejercicio 6

def tabla_multiplicar(numero):
  
  while numero < 1 or numero > 10:
   numero = int(input("Error! el numero debe estar en el rango de 1 a 10. Intente otra vez "))
  for i in range(1,11):
   print(f"{i} x {numero} = {i*numero}")
   
#Ejercicio 7

def operaciones_basicas(a,b):
  suma = a + b
  resta = a - b
  division = a / b
  multiplicacion = a * b
  print(f"{a} + {b} = {suma}")
  print(f"{a} - {b} = {resta}")
  print(f"{a} * {b} = {multiplicacion}")
  print(f"{a} / {b} = {round(division,2)}")
  
  #Ejercicio 8
  
def calcular_imc(peso,altura):

  #Empiezo con una validacion de valores tanto para peso como altura
  while peso < 3 or peso > 200: #Elegi estos valores de peso suponiendo los limites de peso de que podria llegar un ser humano pero sin datos certeros 
   peso = float(input("Error! Por favor ingrese un peso posible en KG "))
  while altura < 0 or altura > 2.50:
   altura = float(input("Error! Por favor ingrese una altura posible en metros "))

  imc = peso / (altura ** 2)

  print(f"El indice de masa corporal suyo es: {round(imc,2)}")
  
  #Ejercicio 9
  
def celsius_a_fahrenheit(celsius):
  farenheit = (celsius * (9/5)) + 32
  print(round(farenheit,2) , "F")
  
  #Ejercicio 10 
  
def calcular_promedio(a,b,c):
  promedio = (a+b+c)/3
  print(f"El promedio de los numeros ingresados es: {round(promedio,2)}")


#Programa principal
imprimir_hola_mundo()
saludar_usuario("Manuel Belgrano")
informacion_personal("Maximiliano", "Niemiec", 30, "Cordoba")
calcular_perimetro_circulo(5)
calcular_area_circulo(5)
segundos_a_horas(9600)
tabla_multiplicar(233)
operaciones_basicas(10,7)

#Datos necesarios del ejercicio 8 
peso = float(input("Por favor ingrese su peso en KG "))
altura = float(input("Por favor ingrese su altura en metros "))

calcular_imc(peso,altura)

#Datos necesarios del ejercicio 9
temperatura = float(input("Por favor ingrese una temperatura en grados Celsius "))

celsius_a_fahrenheit(temperatura)

#Datos necesarios del ejercicio 10

numero1 = int(input("Por favor ingrese un primer numero "))
numero2 = int(input("Por favor ingrese un segundo numero "))
numero3 = int(input("Por favor ingrese un tercer numero "))

calcular_promedio(numero1, numero2, numero3)

