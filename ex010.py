#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
real = float(input('Qual valor, em reais, você gostaria de trocar por dólares? '))
dolar = real/5.18
print(
    'Seus R$ {:.2f} reais podem ser trocados por $ {:.2f} doláres.'.format(real, dolar)
)
