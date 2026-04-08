"""
Ejercicio 1: Dado un número entero positivo N, retornar una lista con los números desde 1 hasta N.

Debe implementar dos funciones:
1. Una usando iteración (for o while)
2. Una usando recursividad
"""

def contar_ciclo(n):
    resultado =[]
    for i in range (1, n+1):
        resultado.append(i)
    return resultado
print(contar_ciclo(5))

def contar_recursivo(n):
    """
    Retorna una lista con los números desde 1 hasta n usando recursividad.
    """
    if n == 1:
        return [1]
    lista_previa = contar_recursivo(n - 1)
    lista_previa.append(n)
    return lista_previa
print(contar_recursivo(8))