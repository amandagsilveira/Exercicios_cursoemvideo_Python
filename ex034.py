#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
sal = float(input('Digite o valor do salário: '))
if sal > 1250:
    novosal = sal + (sal * 10 / 100)
    print('Seu novo salário será: R${:.2f}'.format(novosal))
else:
    novosal = sal + (sal * 15 / 100)
    print('Seu novo salário será: R${:.2f}'.format(novosal))
