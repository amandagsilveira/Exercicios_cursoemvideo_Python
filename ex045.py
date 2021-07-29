#Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
print('{:*^40}'.format('  PEDRA PAPEL TESOURA  '))
print('''Suas opções: 
[0] Pedra
[1] Papel
[2] Tesoura  ''')
computador = randint(0, 2)
jogador = int(input('Digite sua opção: '))
print('Pedra...')
sleep(1)
print('Papel...')
sleep(1)
print('Tesoura...')
sleep(1)
print('=' * 30)
print('O computador escolheu {}'.format(itens[computador]))
print('O jogador escolheu {}'.format(itens[jogador]))
print('=' * 30)
if computador == 0: #COMPUTADOR JOGA PEDRA
    if jogador == 0:
        print('EMPATE!!!')
    elif jogador == 1:
        print('JOGADOR VENCEU!!')
    elif jogador == 2:
        print('COMPUTADOR VENCEU!!')
    else:
        print('Jogada inválida!!')
elif computador == 1: #COMPUTADOR JOGA PAPEL
    if jogador == 0:
        print('COMPUTADOR VENCEU!!!')
    elif jogador == 1:
        print('EMPATE!!!')
    elif jogador == 2:
        print('JOGADOR VENCEU!!')
    else:
        print('Jogada inválida!!')
elif computador == 2: #COMPUTADOR JOGA TESOURA
    if jogador == 0:
        print('JOGADOR VENCEU!!!')
    elif jogador == 1:
        print('COMPUTADOR VENCEU!!!')
    elif jogador == 2:
        print('EMPATE!!!')
    else:
        print('Jogada inválida!!')