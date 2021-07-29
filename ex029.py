#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
vel = float(input('Digite a velocidade do carro: '))

if vel > 80:
    valor = (vel - 80) * 7
    print('Você estava acima do limite permitido, foi MULTADO!. \n O valor da sua multa foi de R${:.2f}.'.format(valor))

print('Use sempre o cinto e dirija com segurança!')
