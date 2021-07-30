#Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
n = int(input('Digite um número: '))
div = 0
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end=' ')
        div += 1

    else:
        print('\033[m', end=' ')
    print('{}'.format(c), end=' ')
print('\nO número {} foi divisível {} vezes.'.format(n, div))
if div == 2:
    print('\033[mPor isso ele é \033[36mPRIMO\033[m!')
else:
    print('\033[mNÃO É PRIMO!!')


