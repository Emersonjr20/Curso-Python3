print('='*3, 'Conversor de reais para Dolar', '='*3)
r = float(input('Digite a quantia que deseja converter: R$'))
d = r/5.09
e = r/5.89
print('Com essa quantia de R${:.2f}, você pode obter US${:.2f} \nou também {:.2f}£'.format(r, d, e))
