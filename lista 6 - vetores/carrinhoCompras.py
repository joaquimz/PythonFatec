# 19 - Simule um carrinho de compras: adicione produtos até que o usuário digite 'fim' e, no final, mostre o carrinho.

opcao = ""
carrinho = []

while opcao != "6":
    print("CARRINHO DE COMPRAS")
    print("1 - Iphone 17")
    print("2 - Iphone 17 Pro Max")
    print("3 - Iphone Air ")
    print("4 - Iphone 16")
    print("5 - Iphone 16 Pro Max")
    print("6 - COMPRAR ")

    opcao = input("Escolha um Produto: ")

    if opcao == "1":
        carrinho.append("Iphone 17")
        print(f"No seu carrinho tem {carrinho}")

    elif opcao == "2":
        carrinho.append("Iphone 17 Pro Max")
        print(f"No seu carrinho tem {carrinho}")

    elif opcao == "3":
        carrinho.append("Iphone Air")
        print(f"No seu carrinho tem {carrinho}")

    elif opcao == "4":
        carrinho.append("Iphone 16")
        print(f"No seu carrinho tem {carrinho}")

    elif opcao == "5":
        carrinho.append("Iphone 16 Pro Max")
        print(f"No seu carrinho tem {carrinho}")

    elif opcao == "6":
        print(f"No seu carrinho tem {carrinho}")
        print("Redirecionando para compras...")
    else:
        print("Opção inválida! Tente novamente.")