#O usuário escolhe um produto e o programa informa o preço.

while True:
    print("LOJA DO SEU ZÉ")
    print("PRODUTOS")
    print("1 - Pá")
    print("2 - Enxada")
    print("3 - Carreta")
    print("4 - Veneno Formiga")
    print("5 - Adubo")
    print("6 - Irrigador")

    opcao= input("Escolha um Produto:")

    match opcao:
        case "1":
            print("A Pá esta R$49,90, Deseja adicionar ao Carrinho?")

        case "2":
            print("A Enxada esta R$65,99, Deseja adicionar ao Carrinho?")

        case "3":
            print("A Carreta esta R$159,99, Deseja adicionar ao Carrinho?")

        case "4":
            print("O Veneno para Formiga esta R$9,90, Deseja adicionar ao Carrinho?")

        case "5":
            print("O Adubo esta R$29,99, Deseja adicionar ao Carrinho?")

        case "6":
            print("O Irrigador esta R$49,99, Deseja adicionar ao Carrinho?")

        case _:
            print("Opção Invalida, Escolha um produto existente.")
