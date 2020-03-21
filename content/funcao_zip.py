# concatina listas

numeros = [1, 2, 3, 4]
frutas = ['Abacate', 'Banana', 'Cajarana', 'Damasco']
precos = [4.59, 2.89, 1.59, 8.49]

# for numero, fruta in zip(numeros, frutas): # o numero de listas é indeterminado
#     print(numero, fruta)

produto = {}
bd = []
# criando map a partir de listas
for numero, fruta, preco in zip(numeros, frutas, precos):
    produto = {'cod': numero}
    produto = {'produto': fruta}
    produto = {'preco': preco}

    bd.append(produto)

for x in bd:
    print(x)
