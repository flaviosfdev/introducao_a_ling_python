# Filtra lista e atribui a variável a partir da condição passada no filtro
# Função que cria lista a partir de filtro realizado em outra lista

def pares(i):
    if i % 2 == 0:
        return i

def impares(i):
    if i % 2 == 1:
        return i

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

lista_pares = filter(pares, lista) # (funcao, lista)
lista_impares = filter(impares, lista)

print(list(lista_pares))
print(list(lista_impares))