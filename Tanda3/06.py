"""
Ejercicio 06
Utilizando la función randrange del módulo random, escribir un programa que
obtenga un número aleatorio secreto, y luego permita al usuario ingresar
números y le indique sin son menores o mayores que el número a adivinar,
hasta que el usuario ingrese el número correcto.
"""
from random import randrange

n = randrange(10)
while True:
    adivina = int(input("Juegatela: "))
    if adivina == n:
        print("¡¡ Ole !!")
        break
    elif adivina < n:
        print("Nop, más alto")
    else:
        print("Nop, más bajo")