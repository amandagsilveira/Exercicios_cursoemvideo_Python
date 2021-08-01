'''Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
palpites foram necessários para vencer.'''
from random import randint
from time import sleep
print('-*-'*10)
print('JOGO DA ADIVINHAÇÃO...')
print('-*-'*10)
print('Estou pensando em um número entre 0 e 10...')
comp = randint(0, 10)
print('Pensando...')
sleep(1)
acertou = False
palpites = 0
while not acertou:
    num = int(input('Tente adivinhar o número em que pensei: '))
    palpites += 1
    if num == comp:
        acertou = True
    else:
        if num < comp:
            print('Mais...Tente novamente!')
        elif num > comp:
            print('Menos...Tente novamente!')
print('Pensei no número {}. Você acertou com {} tentativas!'.format(comp, palpites))
