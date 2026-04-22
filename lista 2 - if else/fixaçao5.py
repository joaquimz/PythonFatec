#Pergunte a altura e informe se a pessoa pode entrar no brinquedo (mínimo 1,50m).

altura=float(input("Qual a sua altura em metros?"))
if altura<=1.50:
    print(f"Voce nao pode entrar no brinquedo, pois sua altura esta abaixo do permitido.")
else: print("Voce pode entrar no brinquedo.")
