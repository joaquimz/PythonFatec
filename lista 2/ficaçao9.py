peso=int(input("digite seu peso em kg:"))
altura=float(input("digite sua altura em metros:"))
imc=peso/(altura**2)
print(f"Seu IMC é {imc}")
if imc<18.5:
    print("Abaixo do peso")
elif imc<24.9:
    print("Peso normal")
elif imc<29.9:
    print("Sobrepeso")
elif imc<34.9:
    print("Obesidade Grau 1")
elif imc<39.9:
    print("Obesidade Grau 2")
else:
    print("Obesidade Grau 3")
