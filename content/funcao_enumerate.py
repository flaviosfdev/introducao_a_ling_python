# função enumerate
# serve para obter elementos de uma lista junto com o seu índice

lista = ['abacate', 'bola', 'cachorro']

# obtendo lista numerada a partir de range
for i in range(len(lista)):
    print(i, lista[i])

# imprimindo em forma de tuplas
for i in enumerate(lista):
    print(i)

# imprimindo formatado da maneira desejada
for index, value in enumerate(lista):
    print('index =', index, '| value =', value)