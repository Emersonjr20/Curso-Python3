from random import shuffle
print('Ordem de apresentação dos trabalhos:')
t1 = str(input('Primeiro elemento: '))
t2 = str(input('Segundo elemento: '))
t3 = str(input('Terceiro elemento: '))
t4 = str(input('Quarto elemento: '))
t5 = str(input('Quinto elemento: '))
t6 = str(input('Sexto elemento: '))
t7 = str(input('Sétimo elemento: '))
t8 = str(input('Oitavo elemento: '))
t9 = str(input('Nono elemento: '))
t10 = str(input('Décimo elemento: '))

lista = [t1, t2, t3, t4, t5, t6, t7, t8, t9, t10]
shuffle(lista)
print(lista)
