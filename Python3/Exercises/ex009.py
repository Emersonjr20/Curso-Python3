#Neste exercício, eu lembrava mais ou menos como funcionava e tentei fazer do meu jeito
n = int(input('Digite um número para saber sua tabuada: '))
for x in range(10):
    print('{} x {} = '.format(n, x+1), (x+1)*n)
