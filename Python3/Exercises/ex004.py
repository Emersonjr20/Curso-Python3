#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
n = input('Digite algo: ')
print('É um número?', n.isnumeric())
print('É um alfanumérico?', n.isalpha())
print('É um decimal?', n.isdecimal())
print('Está em minúsculo?', n.islower())
print('Tem somente espaços?', n.isspace())
print('Está em maiúsculo?', n.isupper())
print('Está capitalizada?', n.istitle())
