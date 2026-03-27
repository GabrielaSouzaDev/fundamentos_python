# Autor: Gabriela Souza
# Bafometro

cnh = input('Possui CNH? [sim/nao]')
bafometro = float(input('Nivel de alcool: '))

if cnh == 'sim' and bafometro <= 0.04:
    print('Tudo ok, liberado!')
elif cnh == 'sim' and bafometro <= 0.33:
    print('Limite excedido, infração gravíssima!')
else:
    print('Limite excedido, crime de trânsito!')