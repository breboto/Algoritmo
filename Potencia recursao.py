def potencia(n,p):
    if p == 0:
        return 1
        
    return n * potencia(n,p-1)


resultado = potencia(5,5)
print(resultado)