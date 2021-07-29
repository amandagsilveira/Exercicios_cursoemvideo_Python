#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
dist = float(input('Digite a distância da viagem em km: '))
if dist <= 200:
    valor = 0.5 * dist
    print('O valor da passagem é R$: {:.2f}'.format(valor))
else:
    valor = 0.45 * dist
    print('O valor da passagem é R$: {:.2f}'.format(valor))
print('Boa viagem!')
