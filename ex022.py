#Crie um programa que leia o nome completo de uma pessoa e mostre:

#– O nome com todas as letras maiúsculas e minúsculas.

#– Quantas letras ao todo (sem considerar espaços).

#– Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: ')).strip()
mai = nome.upper()
min = nome.lower()
div = nome.split()
print('Seu nome em letras maiúsculas é: ', mai)
print('Seu nome em letras maiúsculas é: ', min)
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {} letras'.format(len(div[0])))







