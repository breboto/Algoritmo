clientes = []
lista_temporaria = []

def adicionar_cliente(nome, email, telefone, endereco):
    lista_temporaria.append(nome)
    lista_temporaria.append(email)
    lista_temporaria.append(telefone)
    lista_temporaria.append(endereco)
    clientes.append(lista_temporaria.copy())
    lista_temporaria.clear()    


def exibir_clientes():
    for i in range(len(clientes)):
        print(clientes[i])

def buscar_clientes(email):
    for i in range(len(clientes)):
        if email in clientes[i][1]:
            print(clientes[i])

def remover_cliente(email):
    for i in range(len(clientes)):
        if email in clientes[i][1]:
            clientes.remove(clientes[i])



def testar_funcoes():
    adicionar_cliente("Douglas", "doug@hotmail.com", "2226511402", "Rua barao de saquarema 711")
    adicionar_cliente("Pedro", "pedro@hotmail.com", "2226531202", "Avenida Oceanica 789")
    adicionar_cliente("Erica", "erica@hotmail.com", "2226531602", "Nossa Senhora de Nazareth 457")

    print(clientes)

    exibir_clientes()

    buscar_clientes("pedro@hotmail.com")

    remover_cliente("erica@hotmail.com")

    print(clientes)



testar_funcoes()


