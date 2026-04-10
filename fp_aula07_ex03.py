# Autor: Gabriela Souza
# Desafio - Listas de Alunos do curso

# O curso tem 10 alunos;
# 2 desistiram;
# 1 entrou;
# colocar em ordem alfabetica.

alunos = ['Amanda', 'Julia', 'Pedro', 'Jorge', 'Mayla', 'Beatriz', 'Luiz', 'Gabriela', 'Vitor', 'Juliana']
print(alunos)


del alunos[2]
del alunos[6]
print(alunos)

alunos.append('Olivia')
print(alunos)

alunos.sort()
print(alunos)