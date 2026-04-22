#O usuário deve informar o tipo de produto (Eletrônico, Roupas, Alimentos, Móveis), e o programa exibirá o percentual de desconto correspondente.

while True:
    print("PRODUTOS")
    print("1 - Eletrônico")
    print("2 - Roupas")
    print("3 - Alimentos")
    print("4 - Móveis")
    print("5 - Sair")

    opcao= input("Escolha uma das opções:")

    match opcao:
        case "1":
            print("Eletrônicos estão com desconto de 5%")

        case "2":
            print("Roupas estão com um incrivel desconto de 20%")

        case "3":
            print("Alimentos estão com desconto de 2%")

        case "4":
            print("Móveis infelizmente nao estão com desconto")

        case "5":
            print("Saindo...")
            break

        case _:
            print("Opção inválida. Escolha uma opção válida")
