# Autor: Gabriela Souza
# Dicionários
# Consumo de API dentro de um dicionário

# importação da biblioteca
import requests

cep = input('Digite seu cep: ')
url = f'https://viacep.com.br/ws/{cep}/json/'
# importando o valor que esta dentro da url
resposta = requests.get(url)
# armazena o valor dentro de uma variável
dados = resposta.json()

print(f'Logradouro: {dados['logradouro']}')
print(f'Bairro: {dados['bairro']}')
print(f'Cidade: {dados['localidade']}')
print(f'UF: {dados['uf']}')