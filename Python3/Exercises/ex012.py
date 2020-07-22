#Desconto de Produto
print('='*3, 'TABELA DE DESCONTOS', '='*3)
price = float(input('Digite o preço atual do produto: '))
discount = price - (price*5/100)
print('O valor desse produto com desconto de 5%, fica: R${:.2f}'.format(discount))
