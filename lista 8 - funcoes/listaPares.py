#Crie uma função que receba uma lista de números e retorne quantos são pares.

def par (lista):
    pares = 0
    for item in lista:
        if item % 2 == 0:
            pares += 1
    return pares

lista= [1,2,3,4,5,6,7,8,9,10]

print(par(lista))


