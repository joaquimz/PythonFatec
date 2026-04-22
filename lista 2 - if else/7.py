#Receba a nota de um aluno e classifique-a como A (90-100), B (80-89), C (70-79), D (60-69), ou F (menos de 60).

nota=float(input("Digite sua nota: "))
if nota > 89:
    print('Sua nota e A')
elif nota > 79:
    print('Sua nota e B')
elif nota>69:
     print('Sua nota e C')
elif nota>59:
    print('Sua nota e D')
else:
    print('Sua nota e E')
