#Crie um programa que converta uma quantia em dólares para euros. Continue pedindo ao usuário quantias em dólares para converter até que ele insira "0".

print("CONVERSOR DE MOEDA")
euro = 0.85
while True:
    dolares = int(input("Quantos DOLARES voce deseja converter para EUROS? Para sair digite (0). "))

    if dolares == 0:
        print("Obrigado por utilizar nosso conversos! Saindo...")
        break

    if dolares >= 0.1:
        conversor = dolares * euro
        print(f"Os seus {dolares} USD convertidos para euros dão {conversor} EUR")