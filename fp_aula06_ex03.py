# Autor: Gabriela Souza
# Fatorial com Loop While
# Fatorial é um numero multiplicado por seu antecessores
# Ex: 5! -> 5*4*3*2*1

# Se no exemplo o usuario digitar 5
numero = int(input('Fatorial de qual número? '))
fatorial = 1

# O loop vai contar de 5 até 1
while numero >= 0:
    fatorial = fatorial * numero
    numero = numero - 1
    print(f'Variavel numero é {numero} e o fatorial é {fatorial}')
    
print(f'O fatorial é: {fatorial}')