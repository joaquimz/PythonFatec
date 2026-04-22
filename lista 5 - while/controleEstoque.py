# Faça um controle de estoque com menu de entrada, saída e exibição.


produtos = ["Camisetas","Tenis","Bones"]
estoque_camisetas = 50
estoque_tenis = 25
estoque_bones = 10

while True:
    print("1 - Ver Estoque")
    print("2 - Adicionar")
    print("3 - Retirar")
    print("4 - Sair")

    opcao = input("Escolha: ")

    if opcao == "4":
        print("Saindo...")
        break

    if opcao == "1":
        print(produtos)
        busca = input("Escolha o produto do Estoque: ").lower()
        if busca == "camisetas":
         print(f"Tem: {estoque_camisetas} camisetas no estoque.")
        elif busca == "tenis":
         print(f"Tem: {estoque_tenis} tenis no estoque.")
        elif busca == "bones":
         print(f"Tem: {estoque_bones} bones no estoque.")

        else:
         print("Produto não encontrado!")

    elif opcao == "2":
        print(produtos)
        busca = input("Escolha o produto do Estoque para Adicionar: ").lower()
        if busca == "camisetas":
           soma_camisetas = int(input("Escolha a quantidade de CAMISETAS que voce deseja adicionar: "))
           estoque_camisetas += soma_camisetas
           print(f"Agora tem: {estoque_camisetas } Camisetas no estoque.")
        elif busca == "tenis":
            soma_tenis = int(input("Escolha a quantidade de TENIS que voce deseja adicionar: "))
            estoque_tenis += soma_tenis
            print(f"Agora tem: {estoque_tenis} Tenis no estoque.")
        elif busca == "bones":
            soma_bone = int(input("Escolha a quantidade de BONES que voce deseja adicionar: "))
            estoque_bones += soma_bone
            print(f"Agora tem: {estoque_bones} Bones no estoque.")

    elif opcao == "3":
        print(produtos)
        busca = input("Escolha o produto do Estoque para Retirar: ").lower()
        if busca == "camisetas":
            retirar = int(input("Quantas Camisetas voce deseja retirar do estoque: "))
            if retirar <= estoque_camisetas:
             estoque_camisetas -= retirar
             print(f"Agora tem: {estoque_camisetas} Camisetas no estoque. ")
            else:
                print("Erro: Estoque Insuficiente!")
        if busca == "tenis":
            retirar = int(input("Quantos Tenis voce deseja retirar do estoque: "))
            if retirar <= estoque_tenis:
             estoque_tenis -= retirar
             print(f"Agora tem: {estoque_tenis} Tenis no estoque. ")
            else:
                print("Erro: Estoque Insuficiente!")
        if busca == "bones":
            retirar = int(input("Quantos Bones voce deseja retirar do estoque: "))
            if retirar <= estoque_bones:
                estoque_bones -= retirar
                print(f"Agora tem: {estoque_bones} Bones no estoque. ")
            else:
                print("Erro: Estoque Insuficiente!")




