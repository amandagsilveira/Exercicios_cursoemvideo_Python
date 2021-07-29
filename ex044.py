'''Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
– à vista dinheiro/cheque: 10% de desconto
– à vista no cartão: 5% de desconto
– em até 2x no cartão: preço formal
– 3x ou mais no cartão: 20% de juros
'''
from time import sleep
print('{:*^40}'.format(' LOJAS SILVEIRA '))
preço = float(input('Digite o valor da compra: '))
opcao = int(input('''Qual a forma de pagamento? Escolha uma opção:
[0] À vista dinheiro (desconto de 10%)
[1] Débito (desconto de 5%)
[2] Crédito em até 2x (sem acréscimo)
[3] Crédito 3x ou mais (acréscimo de 20% de juros) '''))
if opcao == 0:
    total = preço - (preço * 10 / 100)
    print('Pagamento à vista. Desconto de 10%')
elif opcao == 1:
    total = preço - (preço * 5 / 100)
    print('Pagamento no Débito. Desconto de 5%')
elif opcao == 2:
    total = preço
    parcela = total / 2
    print('Pagamento no Crédito sem juros.')
    print('Sua conta será parcelada em 2X de {}'.format(parcela))
elif opcao == 3:
    total = preço + (preço * 20 / 100)
    totparc = int(input('Quantas parcelas? '))
    parcela = total / totparc
    print('Pagamento no Crédito com 20% de juros.')
    print('Sua compra será parcelada em {}X de R${:.2f} COM JUROS'.format(totparc, parcela))
else:
    total = preço
    print('Opção inválida, tente novamente.')
print('O valor da compra foi de R$ {:.2f}'.format(preço))
print('Calculando o valor final...')
sleep(1.5)
print('O valor final da compra foi de R$ {:.2f}'.format(total))
