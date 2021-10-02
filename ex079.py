num = list()
while True:
    n = int(input('Digite um número: '))
    if n not in num:
        num.append(n)
        print('O número adicionado!')
    else:
        print('Esse número já foi adicionado.')
    r = str(input('Você quer continuar? [S/N]'))
    if r in 'Nn':
       break
num.sort()
print(f'Os valores digitados foram {num}')