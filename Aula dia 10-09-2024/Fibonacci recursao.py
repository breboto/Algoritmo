def fibonacci(n):
    if n < 0:
        return "Não existe termo negativo em Fibonacci."
    if n < 2:
        return n
    
    return (fibonacci(n-1))+(fibonacci(n-2))
    
resultado = fibonacci(2)
print(resultado)