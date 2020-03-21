
x = [1, 2, 3, 4, 5]
y = []

print('populando y a partir de x com o quadrado de cada elemento de x com um laço "for"')
for i in x:
    y.append(i**2)
print(x)
print(y)

print('===========================================')

print('utulizando list comprehension sem condição')
print('z = [i**2 for i in x]')
# variavel = [valor_a_adicionar laço condicao]
z = [i**2 for i in x] # nesse exemplo não há condição
print(x)
print(z)

print('===========================================')

print('utulizando list comprehension com condição')
print('w = [i**2 for i in x if i % 2 == 1] => [1, 3, 5] (ímpares)')
# variavel = [valor_a_adicionar laço condicao]
w = [i for i in x if i % 2 == 1] # nesse exemplo não há condição
print(x)
print(w)