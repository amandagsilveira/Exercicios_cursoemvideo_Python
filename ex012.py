#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input('Digite o preço do produto em reais: '))
promo = preco - (preco * 5 / 100)
print('O produto que custava R${:.2f}, na promoção com 5% de desconto está custando R${:.2f}'.format(preco, promo))



