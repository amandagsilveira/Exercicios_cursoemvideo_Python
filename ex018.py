#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import sin, cos, tan, radians
ang = int(input('Digite o ângulo que você deseja: '))
sn = sin(radians(ang))
cs = cos(radians(ang))
tg = tan(radians(ang))
print('O ângulo de {}° tem: '.format(ang))
print('SENO: {:.2f}'.format(sn))
print('COSSENO: {:.2f}'.format(cs))
print('TANGENTE: {:.2f}'.format(tg))


