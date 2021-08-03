'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o
programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.'''
tot18 = 0
totM = 0
totF20 = 0
while True:
    idade = int(input('Digite sua idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite seu sexo [M/F]: ')).strip().upper()[0]
    if idade > 18:
        tot18 += 1
    if sexo == 'M':
        totM += 1
    if sexo == 'F' and idade < 20:
        totF20 += 1
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Você quer continuar? ')).strip().upper()[0]
    if resp == 'N':
        break
print(f'Foram cadastradas {tot18} pessoas com mais de 18 anos.')
print(f'Foram cadastrados {totM} pessoas do sexo masculino.')
print(f'Foram cadastradas {totF20} pessoas do sexo feminino com menos de 20 anos.')







