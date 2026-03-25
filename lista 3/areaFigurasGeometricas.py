while True:
    print("CALCULO DA AREA DE FIGURAS GEOMÉTRICAS")
    print("1 - QUADRADO")
    print("2 - RETÂNGULO")
    print("3 - TRIÂNGULO")
    print("4 - SAIR")

    opcao= input("Escolha uma opção")

    match opcao:
        case "1":
            lado=float(input("Digite o lado do quadrado:"))
            area= lado**2
            print(f"A area do quadrado é {area}cm")

        case "2":
            comprimento=float(input("Digite o comprimento do  retângulo:"))
            largura=float(input("Digite a largura do retângulo:"))
            area2= comprimento * largura
            print(f"A area do retângulo é {area2}cm")

        case "3":
            base= float(input("Digite a base do triângulo:"))
            altura=  float(input("Digite a altura do triangulo:"))
            area3= base * altura /2
            print(f"A area do triângulo é {area3}cm")

        case "4":
            print("Saindo...")
            break

        case _:
            print("Opção inválida. Escolha uma opção válida de conversão.")
