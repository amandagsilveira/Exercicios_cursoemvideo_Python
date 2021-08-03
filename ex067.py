'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.'''

print('-' * 50)
while True:
    n = int(input('Digite um número para ver sua tabuada: '))
    print('-' * 50)
    if n < 0:
        print('Você digitou um número negativo, tente novamente.')
        break
    else:
        for c in range(1, 11):
            print(f'{n} * {c} = {n * c}')
    print('-' * 50)
print('Fim!')
print('-' * 50)
