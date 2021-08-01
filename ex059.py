'''Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
Seu programa deverá realizar a operação solicitada em cada caso.'''
from time import sleep
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
opção = 0
while opção != 5:
    print('''Suas opções:
    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opção = int(input('Digite sua opção: '))
    if opção == 1:
        s = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, s))
    elif opção == 2:
        m = n1 * n2
        print('A multiplicação entre {} e {} é {}'.format(n1, n2, m))
    elif opção == 3:
        if n1 > n2:
            maior = n1
            print('Entre {} e {}, o maior valor é {}'.format(n1, n2, maior))
        else:
            maior = n2
            print('Entre {} e {}, o maior valor é {}'.format(n1, n2, maior))
    elif opção == 4:
        print('Informe os números novamente')
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro número: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida, tente novamente!')
    sleep(2)
print('Fim do Programa')