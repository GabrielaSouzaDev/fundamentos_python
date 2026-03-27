# Autor: Gabriela Souza
# Projeto Estrutura Condicional - Login

# Usando and (e) e or (ou)
usuario = input('Digite o nome de usuário: ')
senha = input('Digite sua senha: ')

if (usuario == 'Gabriela' or usuario == 'gabriela') and senha == 'lalala123':
    print('Acesso permitido!')
else:
    print('Acesso negado!')