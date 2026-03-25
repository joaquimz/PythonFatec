peso=float(input("Qual o seu peso em Kg?"))
altura=float(input("Qual a sua altura em metros?"))
imc=peso/(altura*altura)
if imc <=18.5:
    print("Voce esta abaixo do peso")
elif imc >=18.5 and imc <=25:
    print("Voce esta no peso ideal")
elif imc >=25 and imc <=30:
    print("Voce esta com sobrepeso")
else:
        print("Voce esta com obesidade")
print(f"Seu IMC e de {imc}")
