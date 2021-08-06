'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de
Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.'''
times = ('Palmeiras', 'Atlético - MG', 'Fortaleza', 'Bragantino', 'Flamengo',
         'Atlético - PR', 'Ceará', 'Santos', 'Atlético - GO', 'Bahia',
         'Corinthians', 'Fluminense', 'Juventude', 'Internacional', 'Sport',
         'Cuiabá', 'São Paulo', 'América - MG', 'Grêmio', 'Chapecoense')
print(f'Os 5 primeiros colocados são: {times[0:5]}')
print(f'Os quatro últimos colocados são: {times[16:]}')
print(f'Times em ordem alfabética: {sorted(times)}')
print(f'O time da Chapecoense está na {times.index("Chapecoense") + 1}º posição.')
