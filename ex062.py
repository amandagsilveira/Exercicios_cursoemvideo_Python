'''Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.'''
p = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
c = 1
tot = 0
add = 10
while add != 0:
    tot += add
    while c <= tot:
        print('{}'.format(p), end=' -> ')
        p += r
        c += 1
    print('Pausa...')
    add = int(input('Você quer adicionar quantos termos? '))
print('Progressão finalizada...')
