#O usuário seleciona uma opção de atendimento telefônico:
#1 - Suporte Técnico
#2 - Financeiro
#3 - Cancelamento
#4 - Falar com um atendente

while True:
    print("ATENDIMENTO TELEFÔNICO")
    print("1 - Suporte Telefônica")
    print("2 - Financeiro")
    print("3 - Cancelamento")
    print("4 - Falar com um Atendente")

    opcao= input("Escolha uma opção")

    match opcao:
        case "1":
            print("Ligue para (11) 96776-6910 ")
        case "2":
            print("Redirecionando para Financeiro...")
        case "3":
            print("Cancelando Atendimento...")
        case "4":
            print("Redirecionando para o Atendente...")
            break
        case _:
            print("Opção Invalida, Escolha uma opção valida.")
