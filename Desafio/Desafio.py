import random
import string


def gerar_senha(tamanho, senha=''):
    if tamanho == 0:
        return senha
    else:
        caractere = random.choice(string.ascii_letters + string.digits)
        return gerar_senha(tamanho - 1, senha + caractere)


def cifra_cesar(senha, deslocamento):
    letras = string.ascii_letters
    digitos = string.digits
    
    senha_criptografada = ''
    
    for caractere in senha:
        if caractere in letras:
            novo_indice = (letras.index(caractere) + deslocamento) % len(letras)
            senha_criptografada += letras[novo_indice]
        elif caractere in digitos:
            novo_indice = (digitos.index(caractere) + deslocamento) % len(digitos)
            senha_criptografada += digitos[novo_indice]
        else:
            senha_criptografada += caractere
            
    return senha_criptografada


tamanho_senha = 8


senha = gerar_senha(tamanho_senha)


senha_cripto = cifra_cesar(senha, 3)

print(f'Senha original: {senha}')
print(f'Senha criptografada: {senha_cripto}')