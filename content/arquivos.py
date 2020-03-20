# Operações com arquivos em python
# r: somente leitura
# w: escrita (caso o arquivo já exista, ele será apagado e um novo arquivo vazio será criado)
# a: leitura e escrita (adiciona o novo conteúdo ao fim do arquivo)
# r+: leitura e escrita
# w+: escrita (o modo w+, assim como o w, também apaga o conteúdo anterior do arquivo)
# a+: leitura e escrita (abre o arquivo para atualização)

arq = open("arquivo.txt")
# imprimindo linha por linha (convertendo o conteúdo completo em uma lista)
# linhas = arq.readlines()
# print(linhas)

linhas = arq.readline() # lendo apenas a primeira linha
print(linhas)

# imprimindo texto completo
# texto_completo = arq.read()
# print(texto_completo)
# for linha in linhas:
#     print(linha)