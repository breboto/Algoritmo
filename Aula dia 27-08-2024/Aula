clientes = []
lista_provisoria = []
import random

def adicionar_cliente(nome, email, telefone, endereco):
      lista_provisoria.append(nome)
      lista_provisoria.append(email)
      lista_provisoria.append(telefone)
      lista_provisoria.append(endereco)
      clientes.append(lista_provisoria.copy())
      lista_provisoria.clear()

def exibir_clientes():
      for i in range(len(clientes)):
            print(clientes[i])

def buscar_cliente(email):
      c = 0
      for i in range(len(clientes)):
            if email == clientes[i][1]:
                  for x in clientes[i]:
                        print(x)
                  c +=1
      if c == 0:
            print('Cliente não encontrado')         


def remover_cliente(email):
      c = 0
      for i in range(len(clientes)-1):
            if email == clientes[i][1]:
                  print(f'{clientes[i][0]} foi removido(a) com sucesso.')
                  clientes.remove(clientes[i])
                  c+=1
      
      if c == 0:
            print('Cliente não encontrado') 
                  
while True:
      print('-'*25)
      print('VERSÃO TESTE DE FUNCIONALIDADES DE SISTEMA')
      print('-'*25)
      print('1. Cadastro de Clientes')
      print('2. Exibir Clientes')
      print('3. Buscar Cliente')
      print('4. Remover Cliente')
      print('5. Sair do Sistema')
      print('-'*25)
      
      opcao = int(input('Escolha sua opção:\n'))
      if opcao == 5:
            print('Sistema encerrado.\n')
            break

      elif opcao == 1:
            adicionar_cliente('Pedro Almeida','pedro@gmail.com','(22) 99777-1234', 'avenida lateral')
            adicionar_cliente('Douglas Vignoli','douglas@gmail.com','(22) 2651-1234', 'rua barao anterior')
            adicionar_cliente('Professor Gioliano','gioliano@gmail.com','(22) 9999-9999', 'avenida central')
            adicionar_cliente('Erica','erica@gmail.com','(22) 9999-1234', 'avenida projetada')
            print('Clientes cadastrados com sucesso.\n')
            
            continuar = input('Deseja continuar com o teste? [S/N] ')
            if continuar in 'Ss':
                  continue
            else:
                  break
      
      elif opcao == 2:
            if len(clientes) == 0:
                  print('Nenhum cliente cadastrado ainda.\n')
                  
            else:
                  exibir_clientes()
                  
            continuar = input('Deseja continuar com o teste? [S/N] ')
            if continuar in 'Ss':
                  continue
            else:
                  break
                  
      
      elif opcao == 3:
            if len(clientes) == 0:
                  print('Nenhum cliente cadastrado ainda.\n')
                  
                  
            else:
                  email = random.choice(['pedro@gmail.com','douglas@gmail.com','gioliano@gmail.com','erica@gmail.com'])
                  buscar_cliente(email)
                  
            continuar = input('Deseja continuar com o teste? [S/N] ')
            if continuar in 'Ss':
                  continue
            else:
                  break

      elif opcao == 4:
            email = random.choice(['pedro@gmail.com','douglas@gmail.com','gioliano@gmail.com','erica@gmail.com'])
            remover_cliente(email)
            
            continuar = input('Deseja continuar com o teste? com o teste? [S/N] ')
            if continuar in 'Ss':
                  continue
            else:
                  break
            
      else:
            print('Opção inválida.\n')