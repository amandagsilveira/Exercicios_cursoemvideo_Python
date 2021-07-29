#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
n = float(input('Digite o valor em metros: '))
km = n / 1000
hm = n / 100
dam = n / 10
dm = n*10
cm = n*100
mm = n*1000
print('Você digitou {} metros.'.format(n))
print('Este valor, corresponde a: ')
print('{}km \n {}hm \n {}dam \n {}dm \n {}cm \n {}mm'.format(km, hm, dam, dm, cm, mm))
