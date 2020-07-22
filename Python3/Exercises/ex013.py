#Aumento de Salário
print('='*3, 'Aumento de salário', '='*3)
nome = str(input('Digite o nome do funcionário: '))
s = float(input('Digite o salário atual de {}: '.format(nome)))
a = s + (s*15/100)
print('O novo salário de {}, ficará: R${:.2f}'.format(nome, a))
