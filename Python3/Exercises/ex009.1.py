#Neste caso tentei aprimorar o que havia feito no ex009
n = int(input('Digite um número para saber sua tabuada: '))
print('-'*15)
for x in range(10):
    print('{} x {:2} = '.format(n, x+1), (x+1)*n)
print('-'*15)
