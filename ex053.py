''' Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
desconsiderando os espaços. Exemplos de palíndromos:
APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.'''
frase = str(input('Digite uma frase: ')).upper().strip()
palavras = frase.split()
tudojunto = ''.join(palavras)
inverso = tudojunto[::-1]
'''inverso = ''
for l in range(len(tudojunto) -1, -1, -1):
    inverso += tudojunto[l]'''
print('O inverso de {} é {}'.format(frase, inverso))
if inverso == tudojunto:
    print('Temos um \033[36mPALÍNDROMO!')
else:
    print('A frase digitada NÃO É UM PALÍNDROMO.')
#print('Você digitou: {}'.format(frase))
