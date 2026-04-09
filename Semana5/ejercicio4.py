"""
Ejercicio 4:
Dado un número entero positivo N, contar cuántos números pares existen entre 1 y N.
"""

def contar_pares_ciclo(n):
    contar = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            contar += 1
    return contar
print("La cantidad de numeros pares entre el 1 y el 22 es:", contar_pares_ciclo(22))

def contar_pares_recursivo(n):
    if n == 0:
        return 0
    if n % 2 == 0:
        print("Es par:", n)
        return 1 + contar_pares_recursivo(n-1)
    return contar_pares_recursivo(n - 1)
print("La cantidad de numeros pares entre el 1 y el 22 es:", contar_pares_recursivo(22))
        
    
