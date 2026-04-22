#Exiba uma contagem regressiva de 10 até 1 e, ao final, exiba "Fogo!".
import time

for numero in range(10, 0 , -1):
    time.sleep(1)
    print(numero)
print(f"Fogo!")