# vai aplicar uma função a todos os elementos de uma lista
# ex.:

def dobro(x):
    return x * 2

lista = [1, 2, 3, 4, 5]
lista_dobro = map(dobro, lista)# (funcao, lista)
print(type(lista_dobro))
print(list(lista_dobro))