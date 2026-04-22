#O computador escolhe um número aleatório de 1 a 10, e o usuário tem 3 tentativas para adivinhar. Dê dicas se o número é maior ou menor.

import random

numero_escolhido = random.randint(1, 10)

for i in range (3):

    chute = int(input("Digite um numero entre 1 e 10: "))

    if chute == numero_escolhido:
        print("Parabens Voce Acertou!")
        break

    elif chute > numero_escolhido:
        print("Voce errou! O numero sorteado e menor que o seu chute.")

    else:
        print("Voce errou! O numero sorteado e maior que o seu chute.")

else:
    print(f"Voce errou todas os seus chutes! O numero sorteado era {numero_escolhido}.")
