#Faça um algoritmo que leia a largura e altura de uma parede, calcule e mostre a área a ser pintada e a quantidade de tinta necessária para o serviço, sabendo que cada litro de tinta pinta uma área de 2metros quadrados.

largura=float(input("Qual a largura da parede?"))
altura=float(input("Qual a altura da parede?"))
area = (largura*altura)
tinta = area/2
print(f"A area da parede e de {area}m²")
print(f"Voce precisara de {tinta} litros de tinta")
