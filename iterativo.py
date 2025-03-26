def factorial_iterativo(n):
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado
# Calcular el factorial de 5
factorial_de_5 = factorial_iterativo(5)
print(f"El factorial de 5 es: {factorial_de_5}")