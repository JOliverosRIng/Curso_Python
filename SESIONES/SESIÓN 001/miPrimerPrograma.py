#Impresión
print ("Hola Mundo")

# Variables
## String
a = "Hola ¿Cómo estás?"

## Enteros
b = 8

## Float (Decimales)
c = 3.1416

# Imprimir variables
print (a + "Mi nombre es Janeth y tengo " + str(b) + " opciones para programar en Python. Y " + str(c) + " es mi número favorito.")

## Para facilitar la impresión de variables
print("Hola, {} tengo {} de programar y mi número favorito es el {}".format(a,b,c))

## Cambio de variable
b = 15
print("Hola, {} tengo {} de programar y mi número favorito es el {}".format(a,b,c))

## Cambio de variable
print("Hola, {} tengo {} de programar y mi número favorito es el {}".format(a,21,c))

## Otros ejemplos de impresión

nombre = "Janeth"
apellido = "Oliveros"

mensaje = f"Hola, mi nombre es {nombre} {apellido}"

print(mensaje)

# OPERADORES (Operaciones matemáticas básicas)
## Suma, resta, multiplicación, división y módulo

### Números que jugaran
a = 6
b = 19
c = 33

### Operaciones

suma = a + b
resta = b - c
multiplicacion = a * c
division = b / c
modulo = a % b

print("Los resultados de las operaciones son:")
print(f"SUMA: {suma}")
print(f"RESTA: {resta}")
print(f"MULTIPLICACIÓN: {multiplicacion}")
print(f"DIVISIÓN: {division}")
print(f"MÓDULO: {modulo}")

# Decisiones
if a > b :
     print(f"{a} es mayor que {b}")
else:
     print(f"{a} no es mayor que {b}")
