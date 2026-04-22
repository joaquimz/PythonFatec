#Escreva um programa que continue pedindo ao usuário para inserir notas (0 a 10) e calcule a média dessas notas. O programa deve parar quando o usuário digitar uma nota negativa.

soma = 0
quantidade = 0

while True:
    nota = int(input("Digite sua nota (0 - 10)? Para encerrar, digite uma nota negativa -. "))

    if nota < 0:
        break

    if 0 <= nota <= 10:
        soma += nota
        quantidade += 1
    else:
        print("Nota Invalida! Digite uma nota entre 0 e 10.")

if quantidade > 0:
    media = soma / quantidade
    print(f"Sua media foi {media:.2f}")


