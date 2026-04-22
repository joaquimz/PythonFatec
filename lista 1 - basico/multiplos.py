#Elaborar um algoritmo que lê 2 valores a e b e os escreve com a mensagem: "São múltiplos" ou "Não são múltiplos".

a=int(input("Digite o valor a:"))
b=int(input("Digite o valor b:"))
if (a % b == 0 or b % a == 0):
    print("Seus valores a e b sao multiplos")
else:
    print("Seus valores a e b nao sao multiplos")
