#Parque: entrada proibida se idade <12 ou >60.

idade = int(input("Digite sua idade: "))

if idade < 12 or idade > 60:
    print("Proibido")
else:
    print("Autorizado")
