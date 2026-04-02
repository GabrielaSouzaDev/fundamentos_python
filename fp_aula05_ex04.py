# Autor: Gabriela Souza
# Fatorial

numero = int(input('Digite um número: '))
fatorial = 1

for i in range (1, numero + 1):
    # o fatorial recebe o resultado de fatorial * i
    fatorial = fatorial * i
    print(f'O fatorial é: {fatorial}')