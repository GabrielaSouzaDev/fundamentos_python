# Autor: Gabriela Souza
# Loop for com if

# Exercicio proposto:
# usuario digita um numero
# se for positivo começa uma contagem

positivo = 0
negativo = 0

for i in range(3):
    numero = int(input('Digite um numero: '))
    print(f'numero digitado: {numero}')
    print(f'valor de i: {i}')

    if numero > 0:
        positivo = positivo + 1
    elif numero < 0:
            negativo = negativo + 1

print(f'Quantidades de numeros positivos: {positivo}')
print(f'Quantidades de numeros negativos: {negativo}')
