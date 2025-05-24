#1)
def factorial(num):
  if num == 1:
    return 1
  else:
    return num * factorial(num-1)
  
def factoriales():
  numeros = int(input("Ingrese un numero. Se calculara el factorial de todos los numeros entre 1 y ese "))
  print( f"El factorial de {numeros} y los numeros entre 1 y el son: ")
  for i in range(1,numeros+1):
     print(factorial(i))
     


#2)
def fibonacci(pos):
  if pos == 0:
    return 0
  elif pos == 1:
    return 1
  else:
    return fibonacci(pos-1) + fibonacci(pos-2)

#3)

def potencia_recursiva(numero, exponente):
  if exponente == 0:
    return 1
  else:
    return numero * potencia_recursiva(numero, exponente-1)
  
#4)

def decimal_a_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

#5)

def es_palindromo(palabra):
  palabra = palabra.lower()
  palabra = palabra.strip()

  if len(palabra) <= 1:
   return True
  elif palabra[0] != palabra[-1]:
    return print("Es falso")
  return  es_palindromo(palabra[1:-1])

#6)

def suma_digitos(x):
    if x < 10:
        return x
    else:
        return (x % 10) + suma_digitos(x // 10)
      
#7) 

def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)
      
#8)

def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        if numero % 10 == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)

#----------------------------------------------------------------------------------------------------------
factoriales()
print(f"Fibonacci: {fibonacci(5)}")
print("potencia recursiva " ,potencia_recursiva(2, 5))
print("decimal a binario " , decimal_a_binario(5))
print("es palindromo ",es_palindromo("neuquen"))
print("suma digitos ", suma_digitos(5))
print("contar bloques ", contar_bloques(4))
print("contar digitos ", contar_digito(1231231231323212132132,3))


