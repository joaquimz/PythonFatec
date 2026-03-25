while True:
    print("ESCOLHA UM DESTINO")
    print("1 - São Paulo")
    print("2 - Rio de Janeiro")
    print("3 - Curitiba")
    print("4 - Salvador")

    opcao=input("Escolha uma Passagem:")

    match opcao:
        case "1":
            print("A partir de R$58,85 passagens para São Paulo")

        case "2":
            print("A partir de R$145,75 passagens para Rio de Janeiro")

        case "3":
            print("A partir de R$150,99 passagens para Curitiba")

        case "4":
            print("A partir de R$351,50 passagens para Salvador")
            break

        case _:
            print("Opção Invalida, Escolha uma passagem Valida.")
