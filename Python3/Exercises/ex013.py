print('='*3, 'Aumento de salário', '='*3)
nome = str(input('Digite o nome do funcionário: '))
s = float(input('Digite o salário atual de {}: '.format(nome)))
a = s*1.15
print('O novo salário de {}, ficará: R${:.2f}'.format(nome, a))
