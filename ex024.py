#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
cid = str(input('Digite a cidade onde você nasceu: ')).strip().upper()
print(cid[:5] == 'SANTO')
