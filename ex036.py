'''Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
 A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.'''
valor = float(input('Digite o valor da casa em R$: '))
sal = float(input('Digite o valor do salário do comprador em R$: '))
anos = int(input('Digite em quantos anos você pretende pagar: '))
prestacao = valor / (anos * 12)
if prestacao > (sal * 30 / 100):
    print('Ao comprar uma casa no valor de R${:.2f} para pagar em {} anos, sua prestação ficará no valor de R${:.2f}, o que corresponde a mais de 30% do seu salário, portanto o empréstimo foi NEGADO!'.format(valor, anos, prestacao))
else:
    print('O empréstimo pode ser CONCEDIDO!')

