# Autor: Gabriela Souza
# BOLOS DE POTE

### 3️⃣ Desafio adicional: A empresa BOLOS DE POTE  precisa investir em novos recursos para melhorar seus produto e precisa de R$ 20.000,00 para realizar as melhorias necessárias, a proprietário foi a um banco para fazer um empréstimo e precisa saber se vale a pena fazer esse empréstimo, para tanto precisa de um sistema que faça o cálculo de quanto vai pagar de juros e se atende as necessidades da empresa, não pode pagar mais de 10% do valor do empréstimo, dados abaixo:

#### Valor do empréstimo: R$ 20.000,00

#### Taxa de juros do banco: Juros Compostos de 1,25% ao mês

#### Quantidade de meses que deseja parcelar

#### Empréstimo está aprovado se o valor do juros for menor ou igual a 10% do valor do emprestimo

valorEmprestimo = float(input('Qual o valor do empréstimo? R$ '))
quantidadeMeses = int(input('Em quantos meses deseja parcelar? '))
taxaJuros = 0.0125
valorTotalComJuros = valorEmprestimo * (1 + taxaJuros) ** quantidadeMeses
print(f'O valor total a ser pago com juros é: R$ {valorTotalComJuros:.2f}')
valorJuros = valorTotalComJuros - valorEmprestimo
print(f'O valor dos juros é: R$ {valorJuros:.2f}')
jurosMaximoPermitido = valorEmprestimo * 0.10
print(f'O valor máximo de juros permitido é: R$ {jurosMaximoPermitido:.2f}')

if valorJuros <= jurosMaximoPermitido:
    print('O empréstimo está aprovado.')
else:
    print('O empréstimo não está aprovado.')