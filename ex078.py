'''Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual
foi o maior e o menor valor digitado e as suas respectivas posições na lista.'''
maior = 0
menor = 0
num = []
for c in range(0, 5):
    num.append(int(input('Digite um número: ')))
    if c == 0:
        maior == menor == num[c]
    else:
        if num[c] > maior:
            maior = num[c]
        if num[c] < menor:
            menor = num[c]
print('Você digitou: ', num)
print('O maior valor foi: ', maior)
print('O menor valor foi: ', menor)


