month=int(input("Qual mês voce deseja saber, digite em numeros (1-12):"))
if month==1 or month==12 or month==2:
    print("Verão")
elif month==3 or month==4 or month==5 or month==6:
    print("Outono")
elif month==7 or month==8 or month==9:
    print("Inverno")
elif month==10 or month==11:
    print("Primavera")
else: print("Mês Invalido")
