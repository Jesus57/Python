"""
Ejercicio 07
Escribir un programa que tome una cantidad "m" de valores ingresados por el
usuario, a cada uno le calcule el factorial e imprima el resultado junto con
el número de orden correspondiente.
"""
leyendo = int(input("Introduzca el numero de factoriales que quieras sacar"))
factorial = 1
for j in range(2,leyendo):
    factorial *= j
print(leyendo, factorial)