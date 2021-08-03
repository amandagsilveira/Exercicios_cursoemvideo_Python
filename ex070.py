'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar
se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.'''
prod1000 = 0
tot = 0
menor = 0
totprod = 0
maisbarato = ' '
while True:
    nome = str(input('Digite o nome do produto: '))
    preço = float(input('Digite o preço do produto R$ '))
    totprod += 1
    tot += preço
    if preço > 1000:
        prod1000 += 1
    if totprod == 1 or preço < menor:
        menor = preço
        maisbarato = nome
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()
    if resp == 'N':
        break
print(f'Total gasto na compra R$ {tot}')
print(f'Ao todo foram {prod1000} produtos que custam mais de R$ 1000.00.')
print(f'O produto mais barato foi {maisbarato}.')



