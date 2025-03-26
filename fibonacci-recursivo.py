def fibonacci_recursivo(n, profundidad=0):
    # Añadimos un parámetro de profundidad para mostrar la indentación de las llamadas recursivas
    espacios = "  " * profundidad  # Crear espaciado para mostrar la jerarquía de llamadas
    
    # Caso base: si n es 0 o 1, retornar n
    if n <= 1:
        print(f"{espacios}fibonacci({n}) = {n}")
        return n
    
    # Llamada recursiva
    print(f"{espacios}Calculando fibonacci({n})")
    
    # Calcular fibonacci de n-1 y n-2
    fib_n_1 = fibonacci_recursivo(n-1, profundidad + 1)
    fib_n_2 = fibonacci_recursivo(n-2, profundidad + 1)
    
    # Calcular y mostrar el resultado
    resultado = fib_n_1 + fib_n_2
    print(f"{espacios}fibonacci({n}) = {resultado}")
    
    return resultado

# Ejemplo de uso: calcular el fibonacci de 6
print("Secuencia de Fibonacci Recursiva para n = 6:")
resultado_final = fibonacci_recursivo(10)
print(f"\nResultado final: {resultado_final}")