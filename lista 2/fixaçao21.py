idade=int(input("Qual sua idade?"))
pais=input("Esta acompanhado dos responsaveis? (SIM/NAO) ")

if idade>=18 or pais =="SIM":
    print("Liberado, aproveite a festa.")
else:
    print("Infelizmente, sua entrada não é permitida.")
