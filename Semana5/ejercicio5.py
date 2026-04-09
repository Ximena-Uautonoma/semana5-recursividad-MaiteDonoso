"""
Ejercicio 5:
Calcular la potencia de una base elevada a un exponente entero positivo.
"""

def potencia_ciclo(base, exponente):
    resultado = 1
    # _ es un valor nulo temporal de que no se utilizara en la función
    for _ in range(exponente):
        resultado = resultado*base
    return resultado
print("El resultado de 2 elevado a 4 es:", potencia_ciclo(2,4))



def potencia_recursiva(base, exponente):
    if exponente == 0:
        return 1
    return base*potencia_recursiva(base, exponente - 1)
print("El resultado de 2 elevado a 4 es:", potencia_recursiva(2,4))