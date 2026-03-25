nome=(input("Qual o seu nome jogador?"))
idade=int(input("Qual a sua idade?"))
if idade < 18:
    print("Voce esta na categoria juvenil do clube.")
elif idade <35:
    print("Voce esta na categoria adulto do clube.")
else:
    print("Seja bem vindo veterano.")
