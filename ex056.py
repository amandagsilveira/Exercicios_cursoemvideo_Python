'''Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.'''
somaidade = 0
maioridadehomem = 0
nomevelho = ''
totmulher20 = 0
for c in range(1, 5):
    nome = str(input('Digite o nome da {}° pessoa: '.format(c)))
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo [M/F]: ')).strip().upper()
    somaidade += idade
    if c == 1 and sexo == 'M':
        maioridadehomem = idade
        nomevelho = nome
    elif sexo == 'M' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    elif sexo == 'F' and idade < 20:
        totmulher20 += 1
media = somaidade / 4
print('A média de idade do grupo é {} anos '.format(media))
print('O homem mais velho se chama {} e tem {} anos '.format(nomevelho, maioridadehomem))
print('Tem {} mulheres com menos de 20 anos'.format(totmulher20))


