'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''
lista = ('Lápis', 1.5,
         'Borracha', 1.75,
         'Caneta', 2.5,
         'Corretivo', 3.5,
         'estojo', 15.50,
         'caderno', 34.90,
         'agenda', 39.90)
print('-' * 38)
print(f'{"LISTA DE PREÇOS":^40}')
print('-' * 38)
for item in range(0, len(lista)):
    if item % 2 == 0:
        print(f'{lista[item]:.<30}', end='')
    else:
        print(f'R$ {lista[item]:>5.2f}')
print('-' * 38)

