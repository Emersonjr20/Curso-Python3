from random import choice
print('>'*3, 'Sorteio de Time do 4fun hoje!', '<'*3)
print('*- Time A -*')
ta1 = str(input('Primeiro elemento: '))
ta2 = str(input('Segundo elemento: '))
ta3 = str(input('Terceiro elemento: '))
ta4 = str(input('Quarto elemento: '))
ta5 = str(input('Quinto elemento:'))
listaTa = [ta1, ta2, ta3, ta4, ta5]

print('*- Time B -*')
tb1 = str(input('Primeiro elemento: '))
tb2 = str(input('Segundo elemento: '))
tb3 = str(input('Terceiro elemento: '))
tb4 = str(input('Quarto elemento: '))
tb5 = str(input('Quinto elemento:'))
listaTb = [tb1, tb2, tb3, tb4, tb5]



time1 = choice(lista)
print('O aluno escolhido foi {}'.format(time1))
time1 = choice(lista)
print('O aluno escolhido foi {}'.format(time1))
time1 = choice(lista)
print('O aluno escolhido foi {}'.format(time1))
time1 = choice(lista)
print('O aluno escolhido foi {}'.format(time1))
time1 = choice(lista)
print('O aluno escolhido foi {}'.format(time1))
