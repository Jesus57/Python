"""
Ejercicio 02
Escribir un programa que le pregunte al usuario una cantidad de euros, una
tasa de interés y un número de años y muestre como resultado el monto final a
obtener. La fórmula a utilizar es (interés compuesto):
Cf = Ci * (1 + i/100) ^ n
Donde Ci es el capital inicial, i es la tasa de interés y n es el número de
años a calcular.
"""

ci = float(input("Digame su capital inicial en €"))
i = float(input("Ahora digame la tasa de interés"))
n = float(input("Ahora los años"))
print(ci *(1+i/100)**n)