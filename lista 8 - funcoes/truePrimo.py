#Crie uma função chamada eh_primo(numero) que retorne True se o número for primo.

def eh_primo():
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

numero = int(input("Digite um numero: "))
primo = eh_primo(numero)
print(primo)