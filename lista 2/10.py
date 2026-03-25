operacao=(input("Voce deseja sacar ou depositar?"))
if operacao=="sacar":
    sacar=float(input("Voce deseja sacar quantos reais?"))
    if sacar<=100:
        print("Voce nao tem saldo suficiente")
    else:
     print(f"Voce sacou {sacar} reais")
elif operacao=="depositar":
        depositar=float(input("Voce deseja depositar quantos reais?"))
        if depositar <=0:
            print("Voce nao pode depositar este valor!")
        else:
            print(f"Voce depositou {depositar} reais")
