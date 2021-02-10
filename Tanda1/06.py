"""
Ejercicio 04
Utilice el programa anterior para generar una tabla de conversión de
temperaturas, desde 0º F hasta 120º F, de 10 en 10.
"""
def celsius(faren):
    return (faren-32)*5/9
print("Grados Fahrenheit     Grados Celsius")
print("=================     ==============")
for faren in range(0,121,10):
    print("       ", faren, "           ", celsius(faren))