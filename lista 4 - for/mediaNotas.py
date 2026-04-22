#Peça 5 notas ao usuário e calcule a média delas.

soma = 0

for i in range(5):
    nota = int(input("Digite uma nota:"))
    soma += nota

media = soma / 5

print("Media:", media)
