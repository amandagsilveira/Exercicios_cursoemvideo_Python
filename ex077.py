'''Crie um programa que tenha uma tupla com várias palavras(não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são suas vogais.'''
palavras = ('computador', 'curso', 'python', 'linguagem', 'programar')
for p in palavras:
    print(f'\nA palavra {p} tem as vogais: ', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
