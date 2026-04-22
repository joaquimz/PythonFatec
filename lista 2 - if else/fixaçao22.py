#Meia-entrada no cinema: estudante ou menor de 18 anos.

idade=int(input("Qual sua idade?"))
estudante=(input("Voce e estudante? (SIM/NÃO)"))
if estudante=="SIM" or idade<18:
    print("Voce tem direito a Meia-entrada no cinema!")
else:
    print("Voce nao tem direito a meia entrada,pague a inteira.")
