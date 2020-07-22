print('='*3, 'Medidor de tinta: Pintando sua parede', '='*3)
l = float(input('Digite a largura da parede que deseja pintar: '))
h = float(input('Digite a altura da parede que deseja pintar: '))
a = l*h
lt = a/2
print('A parede possui uma área de {:.2f}m² com a dimensão de {}x{} \nVocê precisará de {:.2f}L de tinta'.format(a, l, h, lt))
