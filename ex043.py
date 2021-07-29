'''Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida'''
altura = float(input('Digite sua altura em metros: '))
peso = float(input('Digite seu peso em quilos: '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Seu IMC é de {:.1f}. Você está \033[31mABAIXO\033[m do peso.'.format(imc))
elif 18.5 <= imc < 25:
    print('Seu IMC é de {:.1f}. Você está no \033[32mPESO IDEAL\033[m PARABÉNS!.'.format(imc))
elif 25 <= imc < 30:
    print('Seu IMC é de {:.1f}. Você está em \033[33mSOBREPESO\033[m.'.format(imc))
elif 30 <= imc < 40:
    print('Seu IMC é de {:.1f}. Você está \033[33mOBESO\033[m.'.format(imc))
else:
    print('Seu IMC é de {:.1f}. Você está em \033[31mOBESIDADE MÓRBIDA\033[m.'.format(imc))