# veiculos = ["carro", "bicicleta"]
# # novo = []

# # for x in veiculos:
# #     if "i" in x:
# #         novo.append(x)

# novo1 = [x for x in veiculos if "i" in x]
# print(novo1)

# lista_tarefas = [{}]
lista_tarefas =  [] 

def adicionar_tarefa(lista_tarefas, descricao, status, prioridade):
    if lista_tarefas:  
        id = max(tarefa['id'] for tarefa in lista_tarefas) + 1 
    else:
        id = 1          
           
    novas = ({"id": id ,"descricao": descricao, "status": status , "prioridade": prioridade})
    lista_tarefas.append(novas)
          
def visualizar_tarefas(lista_tarefas):
    for i in lista_tarefas:
        print(f" ID: {i["id"]}\n  Descrição: {i["descricao"]}\n  Status: {i["status"]}\n  Prioridade: {i["prioridade"]}\n")
        print("-"*30)

def filtrar_tarefas(lista_tarefas, status = None, prioridade = None):
    if status is None and prioridade is None:
        visualizar_tarefas(lista_tarefas)
    
    elif status is None:
         prioridades = [i for i in lista_tarefas if i["prioridade"] == prioridade]
         visualizar_tarefas(prioridades)
    
    elif prioridade is None:
        prioridades = [i for i in lista_tarefas if (i["status"] == status)]
        visualizar_tarefas(prioridades)
    else:
        prioridades = [i for i in lista_tarefas if (i["status"] == status or i["prioridade"] == prioridade)]
        visualizar_tarefas(prioridades)
            

    


adicionar_tarefa(lista_tarefas,"Tarefa 1", "Pendente", "Baixa")
adicionar_tarefa(lista_tarefas,"Tarefa 2", "Pendente", "Média")
adicionar_tarefa(lista_tarefas,"Tarefa 3", "Concluída", "Alta")
adicionar_tarefa(lista_tarefas,"Tarefa 4", "Em Andamento", "Alta")
adicionar_tarefa(lista_tarefas,"Tarefa 5", "Pendente", "Média")
adicionar_tarefa(lista_tarefas,"Tarefa 4", "Em Andamento", "Média")

#filtrar_tarefas(lista_tarefas)
#filtrar_tarefas(lista_tarefas, "Concluída")
#filtrar_tarefas(lista_tarefas, "Em Andamento", "Alta")
filtrar_tarefas(lista_tarefas, None, "Média")

# visualizar_tarefas(lista_tarefas)