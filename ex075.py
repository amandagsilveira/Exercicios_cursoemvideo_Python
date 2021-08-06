'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.'''
num = (int(input('Digite o 1° número: ')),
       int(input('Digite o 2° número: ')),
       int(input('Digite o 3° número: ')),
       int(input('Digite o 4° número: ')))
print(f'Você digitou o valor 9 {num.count(9)} vezes.')
if 3 in num:
       print(f'O valor 3 foi digitado pela primeira vez na {num.index(3) + 1}° posição.')
else:
       print('Você não digitou o número 3')
print('Os números pares digitados foram: ', end=' ')
for n in num:
       if n % 2 == 0:
              print(n, end=' ')

