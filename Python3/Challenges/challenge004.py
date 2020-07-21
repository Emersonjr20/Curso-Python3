#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
n = input('Digite algo: ')
print(n.isnumeric())
print(n.isalpha())
print(n.isdecimal())
print(n.islower())
print(n.isspace())
print(n.isupper())
