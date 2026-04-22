#Crie um programa que solicite ao usuário para inserir números e some esses números até que o usuário insira zero. Quando zero for inserido, o programa deve imprimir a soma total.

soma = 0

while True:
    numero = int(input("Digite um numero (ou 0 para sair): "))

    if numero == 0:
        print("Saindo...")
        break

    soma += numero

print(f"A soma total é {soma}")