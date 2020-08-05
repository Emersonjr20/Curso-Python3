frase = '  Eu Adoro Torta de Limão'
print(frase.upper().count('o'))
print(len(frase.strip()))
print(frase.replace('Torta', 'Suco'))
#no caso do replace, ele não substitui a palavra efetivamente, é necessário salvar dessa maneira:
# frase = frase.replace('Torta', 'Suco')      - Desta forma você substitui de forma que frase receba o que acontecer no replace.

#Uma string nos seus microelementos é imutável, a não ser que haja uma função de transformação de string e faça uma atribuição.

print('Torta' in frase)
print(frase.find('Limão'))
print(frase.find('limão')) #mostrará -1 pois, não há nenhuma posição desse formato
print(frase.lower().find('limão'))

dividido = frase.split()
print(dividido)
print(dividido[1][2])
