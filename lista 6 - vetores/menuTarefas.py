# 20 - Desenvolva um menu de opções para gerenciar uma lista de tarefas: adicionar, remover, exibir e sair.

opcao = ""
lista_tarefas = []

while opcao != "4":
    print("---LISTA DE TAREFAS---")
    print("---MENU DE OPÇÕES---")
    print("1 - ADICIONAR")
    print("2 - REMOVER")
    print("3 - EXIBIR")
    print("4 - SAIR")

    opcao = input(f"Escolha uma opção do menu:")

    if opcao == "1":
        print("<ADICIONAR>")
        adicionar = input("Adicionar tarefa: ").lower()
        lista_tarefas.append(adicionar)

    elif opcao == "2":
        print("<REMOVER>")
        remover = input("Remover tarefa: ").lower()
        if remover in lista_tarefas:
            lista_tarefas.remove(remover)
            print(f"Tarefa '{remover}' removida com sucesso!")
        else:
           print("Essa tarefa não foi encontrada na lista.")

    elif opcao == "3":
        print("<LISTA DE TAREFAS>")
        print(lista_tarefas)

    elif opcao == "4":
        print("Saindo...")

    else:
        print("Opção invalida! Tente novamente.")



