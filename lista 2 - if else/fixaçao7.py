#Solicite a idade e classifique: criança, adolescente, adulto ou idoso.

idade=int(input("digite sua idade:"))
if idade<13:
    print("Criança")
elif idade<18:
    print("Adolescente")
elif idade<60:
    print("Adulto")
else: print("Idoso")
