'''Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros
 termos da progressão usando a estrutura while'''
p = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
c = 1
while c <= 10:
    print('{}'.format(p), end=' -> ')
    p += r
    c += 1
print('Acabou...')
