def contagem_num(n):
    if n < 10:
        return 1
    return 1 + contagem_num(n//10)

resultado = contagem_num(25)
print(resultado)