cadastrado = input("Você está cadastrado? (SIM ou NÃO) ")
atraso = input("Você tem algum atraso? (SIM ou NÃO) ")

if cadastrado == "SIM":
    if atraso == "NÃO":
        print(f"Liberado")
    else:
        print(f"Atrasado")
else:
    print(f"Faça seu cadastro")
