"""
Ejercicio 7:
Una persona registra cuánto dinero ahorra cada mes en una lista.
Cada valor representa el ahorro mensual.

Se requiere calcular el ahorro total acumulado.

Debe implementar:
1. Una solución con iteración
2. Una solución con recursividad
"""

def ahorro_total_ciclo(ahorros):
    """
    Retorna el ahorro total usando iteración.
    """
    total = 0
    for dinero in ahorros:
        total += dinero
    return total
print("El total acumulado de lo ahorros es de:", ahorro_total_ciclo([30, 40, 26, 30, 45]))


def ahorro_total_recursivo(ahorros):
    """
    Retorna el ahorro total usando recursividad.
    """
    if not ahorros:
        return 0
    dinero = ahorros [0]
    ahorros.pop(0)
    return dinero + ahorro_total_recursivo(ahorros)
print("El total acumulado de lo ahorros es de:", ahorro_total_recursivo([30, 40, 26, 30, 45]))