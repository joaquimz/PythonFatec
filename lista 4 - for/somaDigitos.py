#Peça um número ao usuário e some seus dígitos (exemplo: 123 → 1+2+3 = 6).

numero =(input("Digite um numero:"))

soma = 0

for i in numero:
    soma += int(i)

print("Soma dos digitos: ", soma)