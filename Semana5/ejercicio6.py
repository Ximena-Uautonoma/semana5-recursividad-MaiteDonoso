"""
Ejercicio 6:
Una tienda registra sus ventas diarias en una lista de números. Cada número representa el monto de ventas de un día.
Se solicita calcular el total de ventas acumuladas.

Debe implementar dos funciones:
1. Una usando iteración (for o while)
2. Una usando recursividad
"""

def total_ventas_ciclo(ventas):
    """
    Retorna el total de ventas usando ciclos.
    """
    total = 0
    for monto in ventas:
        total += monto
    return total
print("El total de las sumas es:", total_ventas_ciclo([150, 200, 50, 300]))


def total_ventas_recursivo(ventas):
    """
    Retorna el total de ventas usando recursividad.
    """
    if not ventas:
        return 0
    valor = ventas [0] #Para iniciar una lista se le asigna un valor 0 para comenzar
    ventas.pop(0) #Se elimina el primer valor que es 0 para que la lista sea normal
    return valor + total_ventas_recursivo(ventas)
print("El total de las sumas es:", total_ventas_recursivo([150, 200, 50, 300]))
