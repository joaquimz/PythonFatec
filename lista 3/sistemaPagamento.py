while True:
        print("ESCOLHA UMA FORMA DE PAGAMENTO")
        print("1 - Credito")
        print("2 - Debito")
        print("3 - PIX")
        print("4 - Sait")

        opcao= input("Escolha Uma Forma de Pagamento:")

        match opcao:
            case "1":
                print("No Credito a um juros de 2% por parcela em sua compra")

            case "2":
                print("No Debito a um desconto de 3% em sua compra")

            case "3":
                print("No PIX a um desconto imperdivel! Hoje e seu dia de sorte 10% de desconto em sua compra")

            case "4":
                print("Saindo...")
