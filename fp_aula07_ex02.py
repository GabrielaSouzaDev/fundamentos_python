# Autor: Gabriela Souza
# Listas

filmes = ['Verity', 'Homem Aranha', 'Gente Grande', 'Harry Potter']

print(filmes[2])

# adiciona no fim da lista um novo item
filmes.append('Barbie')
print(filmes)

# adiciona em uma posição especifica o novo item
filmes.insert(2,'John Wick')
print(filmes)

# listar em ordem alfabetica
filmes.sort()
print(filmes)

# como remover colchetes [] e adicionando pipe | para separar os itens
print(*filmes , sep=' | ')