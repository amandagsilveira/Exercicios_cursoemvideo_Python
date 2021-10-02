'''Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.  B) Uma listagem com as pessoas mais pesadas.
 C) Uma listagem com as pessoas mais leves.'''
temporaria = list()
principal = list()
maior = menor = 0
while True:
    temporaria.append(str(input('Digite o nome: ')))
    temporaria.append(float(input('Digite o peso: ')))
    if len(principal) == 0:
        maior = menor = temporaria[1]
    else:
        if temporaria[1] > maior:
            maior = temporaria[1]
        if temporaria[1] < menor:
            menor = temporaria[1]
    principal.append(temporaria[:])
    temporaria.clear()
    resposta = str(input('Quer continuar? [S/N]'))
    if resposta in 'Nn':
        break
print(f'Os dados digitados foram: {principal}')
print(f'Ao todo foram {len(principal)} pessoas cadastradas')
print(f'O maior peso foi {maior} Kg e o menor peso foi {menor} Kg ')
for p in principal:
    if p[1] == maior:
        print(f' Maior peso: {p[0]}', end=' ')
print()
for p in principal:
    if p[1] == menor:
        print(f'Menor peso: {p[0]}', end=' ')
print()