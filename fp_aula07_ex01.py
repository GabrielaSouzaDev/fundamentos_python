# Autor: Gabriela Souza
# Listas

# listas em Python permite misturar tipos
# listas são mutaveis, é possivel alterar, incluir e excluir valores
# listas iniciam apartir do 0
nomes = ['Maria', 'Joâo', 'Marta', 'Anakin', 'Leia']

print(nomes)
print(nomes[2])

# é possivel alterar o conteudo da lista
nomes[3] = 'Cleber'
print(nomes)

# incluir conteudo na lista
nomes.append('Mateus')
print(nomes)

# del e .remove podem ser usados para remover itens de uma lista
del nomes[5]
print(nomes)

nomes.remove('Maria')
print(nomes)
