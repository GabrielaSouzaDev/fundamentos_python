# Autor: Gabriela Souza
# Tuplas

# Tuplas são mais rapidas de serem processadas por serem finitas
# Tuplas são imutaveis, não podem ser alteradas
# No backend é chamada de ENUM

meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')
print(*meses , sep=' | ')
print()
dias_semana = ('domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado')
print(*dias_semana, sep=' | ')
print()