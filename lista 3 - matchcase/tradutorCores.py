#O usuário informa uma cor em português (vermelho, azul, verde, amarelo), e o programa exibe sua tradução para inglês.

cores= (input("Digite uma cor para tradução em inglês:"))

match cores:
    case "vermelho":
        print("Vermelho traduzido para inglês é Red")

    case "azul":
        print("Azul traduzido para inglês é Blue")

    case "amarelo":
        print("Amarelo traduzido para inglês é Yellow")

    case "preto":
        print("Preto traduzido para inglês é Black")

    case "branco":
        print("Branco traduzido para inglês é White")

    case "verde":
        print("Verde traduzido para inglês é Green")

    case "cinza":
        print("Cinza traduzido para inglês é Gray")

    case _:
        print("Opção de cor invalida, escolha outra.")
