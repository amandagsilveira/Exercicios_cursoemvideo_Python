'''Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).'''

n = 0
cont = 0
soma = 0
n = int(input('Digite um número qualquer para somar e digite 999 para parar: '))
while n != 999:
    soma = soma + n
    cont = cont + 1
    n = int(input('Digite um número qualquer para somar e digite 999 para parar: '))
print('Você digitou {} números. A soma entre eles foi {}'.format(cont, soma))
