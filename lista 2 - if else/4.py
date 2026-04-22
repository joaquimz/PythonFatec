#Crie uma calculadora simples que permita ao usuário escolher uma operação (adição, subtração, multiplicação ou divisão) e dois números, e então exiba o resultado.

n1=float(input("Digite seu primeiro numero:"))
n2=float(input("Digite seu segundo numero:"))
operacao=input("Escolha sua operaçao +, -, *, /")
if operacao=="+":
    print(f"{n1+n2}")
elif operacao=="-":
    print(f"{n1-n2}")
elif operacao=="*":
    print(f"{n1*n2}")
elif operacao=="/":
    print(f"{n1/n2}")
