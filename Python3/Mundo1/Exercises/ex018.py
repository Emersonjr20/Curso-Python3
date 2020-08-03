import math
ang = float(input('Digite o ângulo que você deseja obter: '))
sen = math.sin(math.radians(ang))
print('O ângulo de {} tem o Seno de {:.2f}'.format(ang, sen))
cos = math.cos(math.radians(ang))
print('O ângulo de {} tem o Cosseno de {:.2f}'.format(ang, cos))
tang = math.tan(math.radians(ang))
print('O ângulo de {} tem a Tangente de {:.2f}'.format(ang, tang))

'''
from math import radians, sin, cos, tan
ang = float(input('Digite o ângulo que você deseja obter: '))
sen = sin(radians(ang))
print('O ângulo de {} tem o Seno de {:.2f}'.format(ang, sen))
cos = cos(radians(ang))
print('O ângulo de {} tem o Cosseno de {:.2f}'.format(ang, cos))
tang = tan(radians(ang))
print('O ângulo de {} tem a Tangente de {:.2f}'.format(ang, tang))
'''