#Peça a distância a ser percorrida e a velocidade média, depois calcule o tempo da viagem

distancia=int(input("Qual sera a distancia percorrida em km?"))
velocidade=int(input("Qual sera a velocidade em km/h?"))
tempo=distancia/velocidade
if tempo >=1:
    print(f"Esse percurso tera uma duraçao de {tempo}h")
else:
    minutos=tempo*60
    print(f"Esse percurso tera uma duraçao de {minutos}min")
