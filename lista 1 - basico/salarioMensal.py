#Crie um programa que leia o número de dias trabalhados em um mês e mostre o salário de um funcionário, sabendo que ele trabalha 8 horas por dia e ganha R$25,00 por hora trabalhada.


dias=int(input("Quantos dias o funcionario trabalhou no mês?"))
hmes= 8*dias
salario= hmes*25
print(f"Este trabalhador tera um salario de {salario} reais este mes.")
