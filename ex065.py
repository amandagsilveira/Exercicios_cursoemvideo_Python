'''Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''
n = 0
med = 0
cont = 0
soma = 0
maior = 0
menor = 0
continuar = 'S'
while continuar in 'Ss':
    n = int(input('Digite um número: '))
    cont = cont + 1
    soma = soma + n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    continuar = str(input('Você quer continuar [S/N]? ')).strip().upper()
med = soma / cont
print('A média entre os {} valores digitados foi {:.2f}'.format(cont, med))
print('O menor valor foi {} e o maior {}.'.format(menor, maior))
