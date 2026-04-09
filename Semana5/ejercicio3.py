"""
Ejercicio 3:
Dado un número entero positivo N, calcular su factorial.

Debe implementar una versión iterativa y una recursiva.
"""

def factorial_ciclo(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado = resultado * i
    return resultado
print("El factorial de 5 es:", factorial_ciclo(5))


def factorial_recursivo(n):
    if (n==1):
        return 1
    resultado = factorial_recursivo(n-1)*n
    return resultado
print("El factorial de 5 es:", factorial_recursivo(5))