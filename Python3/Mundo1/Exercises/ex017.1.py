#calculando a hipotenusa ---> a²+b²=c²
from math import hypot
print('='*3, 'Descubra a Hipotenusa', '='*3)
co = float(input('Digite o valor do Cateto Oposto: '))
ca = float(input('Digite o valor do Cateto Adjacente: '))
hip = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hip))
