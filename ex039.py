'''Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''
from datetime import date
nasc = int(input('Digite o ano de nascimento: '))
idade = (date.today().year) - nasc
if idade < 18:
    tempo = 18 - idade
    print('Você tem {} anos. Faltam {} anos para o seu alistamento.'.format(idade, tempo))
elif idade == 18:
    print('Você tem {} anos, está na hora de se alistar.'.format(idade))
else:
    tempo = idade - 18
    print('Você tem {} anos, você já deveria ter se alistado a {} anos'.format(idade, tempo))

