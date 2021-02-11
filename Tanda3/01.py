"""
Ejercicio 01
Escribir funciones que resuelvan los siguientes problemas:
Dado un número entero n, indicar si es o no par.
"""

n = int(input("Decime un numero: "))


def par(n):
    if n%2==0:
        return True
    else:
        return False


def esPrimo(n):
    primo = True
    if not (n % 2):
        for i in (3, n/2, 2):
            if n % i == 0:
                primo = False
                break
        return primo