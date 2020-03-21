frutas = ['abacate', 'abacaxi', 'laranja', 'banana', 'jaboticaba']

for fruta in frutas:
    print(fruta)

print('=====================')

dicionario = {'nome':'meu_nome', 'idade':'minha_idade'}

for i in dicionario.keys():
    print(i)
print('=====================')
for i in dicionario.values():
    print(i)
print('=====================')
for i in dicionario:
    print(i + ' - ' + dicionario[i])
