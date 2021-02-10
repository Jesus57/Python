"""
Ejercicio 05
Escribir un programa que imprima todos los números pares entre dos números que
se le pidan al usuario
"""
inicial = int(input("Digame el valor inicial: "))
final = int(input("Digame el valor final: "))

for i in range(inicial,final):
    if i % 2==0:
        print(i)