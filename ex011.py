#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
altura = float(input('Digite a altura da parede em metros: '))
largura = float(input('Digite a largura da parede em metros: '))
area = altura * largura
tinta = area / 2
print('Sua parede tem dimensão de {}x{}, portanto sua área é de {:.2f}m².'.format(altura, largura, area))
print('Para pintar essa parede, você precisa de {:.1f}L de tinta.'.format(tinta))

