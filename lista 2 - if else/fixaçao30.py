#Jogo de adivinhação: vence se número igual ao secreto ou ±1.
import random

segredo = random.randint(1,10)

print ("--- JOGO DA ADIVINHAÇÃO ---")
print(f"(DICA: Voce ganha se acertar ou chegar a mais ou menos 1 de distância)")
advinha = int(input("Digite um numero entre 1 e 10:"))

if advinha == segredo or advinha == segredo + 1 or advinha == segredo - 1:
    print(f"VOCE VENCEU! PARABENS! O numero era {segredo}")

else:
    print(f"Que pena! O número era {segredo}. Você ficou longe demais.")

