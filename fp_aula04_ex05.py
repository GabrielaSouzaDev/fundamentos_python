# Autor: Gabriela Souza
# Condicional com !=

# Usando != (diferente)
idade = int(input('Digite sua idade: '))
bebida = input('Consumiu alcool? [sim/nao]: ')

if idade >= 18 and bebida != 'sim':
    print('Pode dirigir!')
else:
    print('Não pode dirigir!')