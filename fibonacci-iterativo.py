def fibonacci_iterativo(n):
    # Manejar casos especiales
    if n <= 0:
        print("No hay números de Fibonacci para n <= 0")
        return None
    elif n == 1:
        print("fibonacci(1) = 1")
        return 1
    
    # Inicializar variables
    a, b = 0, 1
    print("Inicializando:")
    print(f"a (fibonacci(0)) = {a}")
    print(f"b (fibonacci(1)) = {b}")
    
    # Iterar para calcular los números de Fibonacci
    for i in range(2, n + 1):
        print(f"\nIteración {i}:")
        print(f"Calculando fibonacci({i})")
        
        # Calcular el siguiente número de Fibonacci
        c = a + b
        
        # Mostrar el cálculo
        print(f"  {a} + {b} = {c}")
        
        # Actualizar valores para la siguiente iteración
        a = b
        b = c
        
        print(f"Actualización:")
        print(f"  a = {a}")
        print(f"  b = {b}")
    
    print(f"\nResultado final: fibonacci({n}) = {b}")
    return b

# Ejemplo de uso: calcular el fibonacci de 6
print("Secuencia de Fibonacci Iterativa para n = 6:")
resultado_final = fibonacci_iterativo(10)