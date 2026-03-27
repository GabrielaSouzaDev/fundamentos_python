# Autor: Gabriela Souza
# Credencial

idade = float(input('Digite sua idade: '))
credencial = input('Tem credencial? [sim/nao]')

if idade >= 18 and credencial == 'sim':
    print('Entrada liberada para área vip')
else:
    print('Entrada negada')