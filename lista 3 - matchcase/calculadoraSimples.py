#O usuário escolhe uma operação matemática (+, -, *, /) e insere dois números. O programa exibe o resultado.

while True:
    print("CALCULADORA")
    print("1 - +")
    print("2 - -")
    print("3 - *")
    print("4 - /")

    opcao= input("Escolha uma Operação Matematica:")
    n1= float(input("Digite o primeiro numero:"))
    n2= float(input("Digite o segundo numero:"))

    match opcao:
        case "1":
            somar= n1+n2
            print(f"{n1} + {n2} = {somar}")

        case "2":
            subtrair= n1-n2
            print(f"{n1} - {n2} = {subtrair}")

        case "3":
            multiplicar= n1*n2
            print(f"{n1} * {n2} = {multiplicar}")

        case "4":
            dividir= n1/n2
            print(f"{n1} / {n2} = {dividir}")
            break

        case _:
            print("Opção Invalida, Escolha Uma Operação Valida...")
