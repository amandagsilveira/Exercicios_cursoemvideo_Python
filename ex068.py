'''Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas
que ele conquistou no final do jogo.'''
from random import randint
v = 0
print('*' * 30)
print('JOGO PAR OU ÍMPAR')
print('*' * 30)
while True:
    numjog = int(input('Digite um número: '))
    numpc = randint(0, 10)
    total = numpc + numjog
    resp = ' '
    while resp not in 'PpIi':
        resp = str(input('PAR OU ÍMPAR [P/I]? ')).strip().upper()[0]
    print(f'Você jogou {numjog} e o computador {numpc}. Total de {total}.')
    if resp == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    elif resp == 'I':
        if total % 2 == 1:
            print('Você venceu!')
            v += 1
        else:
            print('Você perdeu!')
            break
    print('Vamos jogar novamente...')
print(f'GAME OVER! Total de vitórias: {v}.')