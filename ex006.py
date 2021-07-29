#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n = int(input('Digite um número: '))
print('Você digitou {} \n O dobro é: {}\n O triplo é: {}\n A raiz quadrada é: {:.2f}'.format(n, (n * 2), (n * 3), (n ** 0.5)) )