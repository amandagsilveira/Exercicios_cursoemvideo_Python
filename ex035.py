#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
seg1 = float(input('Digite o valor do primeiro segmento: '))
seg2 = float(input('Digite o valor do segundo segmento: '))
seg3 = float(input('Digite o valor do terceiro segmento: '))
if seg1 < (seg2 + seg3) and seg2 < (seg1 + seg3) and seg3 < (seg1 + seg2):
    print('\033[0:33mOs segmentos \033[31m{}\033[m, \033[31m{}\033[m \033[0:33me \033[31m{}\033[m \033[0:33mPODEM formar um triângulo'.format(seg1, seg2, seg3))
else:
    print('Os segmentos {}, {} e {} NÃO PODEM formar um triângulo'.format(seg1, seg2, seg3))

