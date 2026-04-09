# Autor: Gabriela Souza
# Loop While - Tabuada

# Diferente do loop for, preciso declarar o valor da variavel i
numero = int(input('Tabuada de qual número? '))
i = 1

# Enquanto i for menor que 10 faça...
while i <= 10:
    print(f'{numero} x {i} = {numero * i}')
    i = i+1
    # i += 1