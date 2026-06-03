#Crie uma função valida_idade(idade) que retorne se a pessoa é maior de idade.

def valida_idade(idade):
    if idade >= 18:
        print(f"Maior de idade!")
    else:
        print(f"Menor de idade!")

idade = int(input("Digite sua idade: "))
valida_idade(idade)