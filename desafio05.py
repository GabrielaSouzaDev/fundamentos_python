# Autor: Gabriela Souza
# Loja VESTE BEM

# 2️⃣ A loja VESTE BEM criou um sistema de fidelidade aos seus clientes, caso o cliente seja cadastrado na loja o mesmo tem 5% de descoto em qualquer compra independente da forma de pagamento, se o cliente não for cadastrado e pagar em dinheiro ou pix terá 3% de desconto, se for no crédito não tem desconto nenhum.

cadastro = input('O cliente é cadastrado na loja? [s/n]: ')
forma_pagamento = input('Qual a forma de pagamento? \n [1] - dinheiro \n [2] - pix \n [3] - credito: ')

# Usando o match case para verificar a forma de pagamento escolhida pelo cliente
match forma_pagamento:
    case '1':
        forma_pagamento = 'dinheiro'
    case '2':
        forma_pagamento = 'pix'
    case '3':
        forma_pagamento = 'crédito'

if cadastro == 's':
    print('O cliente tem 5% de desconto em qualquer compra.')
elif cadastro == 'n' and (forma_pagamento == 'dinheiro' or forma_pagamento == 'pix'):
    print('O cliente tem 3% de desconto.')
elif cadastro == 'n' and forma_pagamento == 'crédito':
    print('O cliente não tem desconto.')
