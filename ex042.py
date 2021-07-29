'''Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
– EQUILÁTERO: todos os lados iguais
– ISÓSCELES: dois lados iguais, um diferente
– ESCALENO: todos os lados diferentes'''
seg1 = float(input('Digite o valor do primeiro segmento: '))
seg2 = float(input('Digite o valor do segundo segmento: '))
seg3 = float(input('Digite o valor do terceiro segmento: '))
if seg1 < (seg2 + seg3) and seg2 < (seg1 + seg3) and seg3 < (seg1 + seg2):
    print('\033[0:33mOs segmentos \033[31m{}\033[m, \033[31m{}\033[m \033[0:33me \033[31m{}\033[m \033[0:33mPODEM formar um triângulo '.format(seg1, seg2, seg3), end='')
    if seg1 == seg2 and seg2 == seg3:
        print('EQUILÁTERO')
    elif seg1 != seg2 and seg1 != seg3 and seg2 != seg3:
        print('ESCALENO')
    else:
        print('ISÓCELES')
else:
    print('Os segmentos {}, {} e {} NÃO PODEM formar um triângulo'.format(seg1, seg2, seg3))