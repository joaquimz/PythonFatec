km=float(input("Quantos km foram percorridos com o carro?"))
dias=int(input("Quantos dias o carro o carro esta alugado?"))
pd= dias*90 #pd é preço por dias usados.
kr= km*0.20 #kr é os km rodados pelo preço dos km.
total= dias+pd
print(f"O valor total a ser pago pelo aluguel do carro por {dias} dias e por {km}km rodados e de {total} reais")
