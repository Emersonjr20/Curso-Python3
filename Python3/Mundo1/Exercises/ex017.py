#calculando a hipotenusa ---> a²+b²=c²
from math import pow
print('='*3, 'Descubra a Hipotenusa', '='*3)
co = float(input('Digite o valor do Cateto Oposto: '))
ca = float(input('Digite o valor do Cateto Adjacente: '))
hip = (pow(co, 2) + pow(ca, 2)) ** (1/2)
print('Cateto Oposto: {:.2f} \nCateto Adjacente: {:.2f} \nHipotenusa: {:.2f}'.format(co, ca, hip))

'''
co = float(input('Digite o valor do Cateto Oposto: '))
ca = float(input('Digite o valor do Cateto Adjacente: '))
hip = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir{:.2f}'.format(hip))
'''