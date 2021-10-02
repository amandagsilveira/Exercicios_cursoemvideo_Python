'''Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares e
os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das
três listas geradas.'''
num = []
par = []
impar = []
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'nN':
        break
for i, n in enumerate(num):
    if n % 2 == 0:
        par.append(n)
    elif n % 2 == 1:
        impar.append(n)
print(f'Os números digitados foram: {num}')
print(f'Os números pares digitados foram: {par}')
print(f'Os números ímpares digitados foram: {impar}')
