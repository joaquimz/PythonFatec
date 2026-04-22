#Crie um programa que simule um caixa eletrônico, que continue pedindo ao usuário para inserir um valor de saque até que o saldo da conta seja zero ou negativo.

opcao = ""
saldo = 100

while opcao != "4":
    print("1 - Saque")
    print("2 - Deposito")
    print("3 - Saldo")
    print("4 - Sair")

    opcao = (input("Escolha uma opção? "))

    if opcao == "1":
        saque = int(input("Qual o valor do saque? "))
        if saque <= saldo:
         saldo -= saque
         print(f"Saque Concluido, agora o senhor tem  {saldo}R$ na sua conta")

    if opcao == "2":
        deposito = int(input("Qual o valor do deposito? "))
        saldo += deposito
        print(f"Deposito de {deposito}R$, agora voce tem {saldo}R$ na conta")

    if opcao == "3":
        print(f"Seu Saldo é de {saldo}R$")

    else:
        print("Saindo da operação...")
        break



