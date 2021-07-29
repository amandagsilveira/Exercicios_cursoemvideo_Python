#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep
print('-*-'*10)
print('JOGO DA ADIVINHAÇÃO...')
print('-*-'*10)
print('Estou pensando em um número entre 0 e 5...')
comp = randint(0, 5)
num = int(input('Tente adivinhar o número em que pensei: '))
print('Processando...')
sleep(2)
if num == comp:
    print('Parabéns, você GANHOU!')
else:
    print('Você PERDEU... eu pensei em {}...tente novamente...'.format(comp))
