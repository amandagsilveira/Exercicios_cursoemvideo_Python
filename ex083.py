'''Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá
analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.'''
exp = str(input('Digite uma expressão: '))
par = []
for simb in exp:
    if simb == '(':
        par.append('(')
    elif simb == ')':
        if len(par) > 0:
            par.pop()
        else:
            par.append(')')
            break
if len(par) == 0:
    print('Sua expressão foi validada!')
else:
    print('Sua expressão está errada!')
