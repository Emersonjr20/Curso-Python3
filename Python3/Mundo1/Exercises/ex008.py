print('Conversor de medida:')
n = float(input('Digite o valor: '))
km = n/1000
hm = n/100
dam = n/10
dm = n*10
cm = n*100
mm = n*1000
print('O valor digitado é: {:.3f}m \nConversão para quilometros: {:.3f}km \nConversão para hectômetro: {:.3f}hm \nConversão para decâmetro: {:.3f}dam \nConversão para decímetros: {:.3f}dm \nConversão para centímetros: {:.3f}cm \nConversão para milímetros: {:.3f}mm'.format(n, km, hm, dam, dm, cm, mm))
