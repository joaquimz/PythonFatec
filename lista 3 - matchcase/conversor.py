#Implemente um conversor de moedas que permita ao usuário escolher entre Dólar (USD), Euro (EUR) e Libra (GBP) e converter um valor informado para Reais (BRL).

while True:
    print("CONVERSOR DE MOEDAS")
    print("1 - (USD) Dolar")
    print("2 - (EUR) Euro")
    print("3 - (GBP) Libras")
    print("4 - Sair")

    opcao= input("Escolha uma opção")

    match opcao:
        case "1":
            valor = float(input("Digite um valor em (R$) para converter:"))
            usd= valor*5.20
            print(f"{valor} convertido para dolares é {usd} USD")

        case "2":
            valor = float(input("Digite um valor em (R$) para converter:"))
            eur= valor * 6.03
            print(f"{valor} convertido para euros é {eur} EUR")

        case "3":
            valor = float(input("Digite um valor em (R$) para converter:"))
            gbp= valor * 6.98
            print(f"{valor} convertido para libras é {gbp} GBP")

        case "4":
            print("Saindo...")
            break
        case _:
          print("Opção inválida. Escolha uma opção válida de conversão.")
