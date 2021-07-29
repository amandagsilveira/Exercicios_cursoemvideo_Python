'''Escreva um programa em Python que leia um número inteiro qualquer e
peça para o usuário escolher qual será a base de conversão:
1 para binário, 2 para octal e 3 para hexadecimal.'''
num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[1] para binário
[2] para octal
[3] para hexadecimal''')
opcao = int(input('Digite sua opção: '))
if opcao == 1:
    print('O valor {} em binário é {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('O valor {} em binário é {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('O valor {} em binário é {}'.format(num, hex(num)[2:]))
else:
    print('Você digitou uma opção inválida, tente novamente!')