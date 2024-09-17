def fatorialrec(n):
    if n == 0 or n == 1:
        return 1

    return n * fatorialrec(n-1)

    
resultado = fatorialrec(5)
print(resultado)
