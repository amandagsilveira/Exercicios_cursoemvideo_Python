'''Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o'''
s = 0
for c in range(1, 7):
    n = int(input('Digite o {} número inteiro: '.format(c)))
    if n % 2 == 0:
        s = s + n
print('A soma dos números pares digitados é {}'.format(s))