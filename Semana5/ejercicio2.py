"""
Ejercicio 2:
Dado un número entero positivo N, retornar la suma de los primeros N números.

Debe implementar:
- suma_ciclo(n)
- suma_recursiva(n)
"""

def suma_ciclo(n):
    """
    Retorna la suma de los primeros n números usando un ciclo.
    """
    suma = 0
    for i in range (1, n +1):
        suma += i
    return suma
print("La suma de los numeros de 1 al 8 es:", suma_ciclo(8))
        


def suma_recursiva(n):
    """
    Retorna la suma de los primeros n números usando recursividad.
    """
    if n == 1:
        return 1
    return n + suma_recursiva(n - 1)
print("La suma de los numeros de 1 al 8 es:", suma_recursiva(8))
