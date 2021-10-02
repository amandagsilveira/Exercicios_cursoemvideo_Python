'''Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, mostre:
A) Quantos números foram digitados. B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.'''
num = []
while True:
    num.append(int(input('Digite um número: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'nN':
        break
print((f'Você digitou {len(num)} elementos.'))
num.sort(reverse=True)
print(f'Os valores digitados em ordem decrescente: {num}')
if 5 in num:
    print('O número 5 faz parte da lista!')
else:
    print('O número 5 não faz parte da lista!')