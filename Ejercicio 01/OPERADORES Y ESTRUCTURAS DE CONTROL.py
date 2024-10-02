""""

#Operadores aritméticos

suma = 2 + 3
print(suma)
resta = 5 - 3
print(resta)
multiplicacion = 2 * 3
print(multiplicacion)
division = 10 / 2
print(division)

#Operadores comparación

numero1 = 1; numero2 = 2

print(numero1 == numero2)
print(numero1 != numero2)
print(numero1 > numero2)
print(numero1 < numero2)
print(numero1 >= numero2)
print(numero1 <= numero2)


#Operadores lógicos

print(True and True) # Nota: Devuelve True si ambos elementos son True
print(True or False) # Nota: Devuelve True si al menos un elemento es True
print(not True) # Nota Devuelve el contrario, True si es Falso y viceversa


#Operadores de Identidad

a = 20
b = 20

print(a is b) # Nota Devuelve True si hacen referencia a el mismo objeto

c = 10
d = 10

print(c is not d) # Nota Devuelve False si no hacen referencia a el mismo objeto


#Declaración if

name = "KAKAROT"

if name != "David":
    print("el nombre no es igual")
else:
    print("el nombre es igual")


#Declaración If-Else

name = "KAKAROT"

if name != "KAKAROT":
    print("el nombre no es KAKAROT")
elif name == "KAKAROT":
    print("el nombre es kakarot :=) ")
else:
    print("no concuerda con niguna opcion")


#Sentencia If anidada
x = 50
y = 100

if x > 100:
    if x > 100:
        print("x e y son mayores que 100 ")
    else:
        print("x no es mayor que 100 pero y si")
else:
    print("x no es mayor que 100")


#Bucle For

animes = ["DxD", "Grendizer", "Bleach"]
for anime in animes:
    print(anime)


#Bucle While

i = 0

while i < 5:
    print(i)
    i += 1

# Bloque Try-Except

try:
    x = 5 / 0
except ZeroDivisionError:
    print("Error: no se puede hacer una division entre cero")
"""

""" EXTRA (opcional):
    * Crea un programa que imprima por consola todos los números comprendidos
    * entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
"""

number = 10

while number < 56:
    if number % 2 == 0 and number != 16 and number % 3 != 0:
        print(number)
    number += 1 