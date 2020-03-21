a = 2
b = 0

try: # caso ocorra erro nesse laço, passara para o except
    print('dividindo a por b')
    print(a/b)
except:
    print('Não foi possível realizar divisão')

print('continuando execução do programa')