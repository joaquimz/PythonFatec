# 9 - Crie uma lista com 5 notas de alunos, calcule a média e diga quais alunos ficaram acima da média.

alunos = []

for i in range(5):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    nota = float(input(f"Digite a nota de {nome}: "))
    alunos.append([nome, nota])

total_notas = sum(aluno[1] for aluno in alunos)
media = total_notas/ 5

print(f"--A nota dos alunos foi {alunos}--")
print(f"---A média da turma foi de {media}---")

print(f"Alunos acima da média:")
for aluno in alunos:
    nome_alunos = aluno[0]
    nota_alunos = aluno[1]

    if nota_alunos > media:
        print(f" {nome_alunos} (Nota: {nota_alunos})")
