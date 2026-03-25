idade=int(input("Qual sua idade?"))
estudante=(input("Voce e estudante? (SIM/NÃO)"))
if estudante=="SIM" or idade<18:
    print("Voce tem direito a Meia-entrada no cinema!")
else:
    print("Voce nao tem direito a meia entrada,pague a inteira.")
