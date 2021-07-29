#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
from random import choice
alu1= input('Digite o nome do primeiro aluno: ')
alu2= input('Digite o nome do segundo aluno: ')
alu3= input('Digite o nome do terceiro aluno: ')
alu4= input('Digite o nome do quarto aluno: ')
lista = [alu1, alu2, alu3, alu4]
escolha = choice(lista)
print('O aluno escolhido foi', escolha)


