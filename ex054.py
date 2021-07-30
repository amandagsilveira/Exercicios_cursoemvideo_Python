'''Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.'''
from datetime import date
totmaior = 0
totmenor = 0
for c in range(1, 8):
    nasc = int(input('Digite o ano de nascimento da {}º pessoa: '.format(c)))
    idade = date.today().year - nasc
    if idade >= 21:
        totmaior += 1
        #print('A {}º pessoa já é maior de idade.'.format(c))
    else:
        totmenor += 1
        #print('A {}º pessoa NÃO É MAIOR DE IDADE.'.format(c))
print('São {} pessoas maior de idade e {} menor de idade.'.format(totmaior, totmenor))

