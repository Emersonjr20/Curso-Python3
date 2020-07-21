n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1+n2
m = n1*n2
d = n1/n2
di = n1//n2 #divisão inteira
e = n1**n2 #exponênciação
#{} as chaves indicam as variáveis que serão inseridas.
#{:.2f} indica que caso seja um número real, terá apenas 2 casas após o ponto flutuante.
print('A soma é: {}, o produto é: {} e a divisão é: {:.2f}'.format(s, m, d), end=' ')
#para que tudo saia na mesma linha basta usar o end=' ', como no exemplo à cima.
#Também é possível quebrar a linha, utilizando \n
print('A divisão inteira é: {} e a potência é: {}'.format(di, e))
