# Autor: Gabriela Souza
# Escola IANES

# 1️⃣ A escola IANES fez uma reestruturação em seu sistema de aprovação de alunos, agora para ser aprovado o aluno precisa atender aos requisitos abaixo:

# Aprovação vai depender de nota e presença:

# Presença ≥75% - Aprovado
# Presença<75% - Reprovado

# Nota ≤5 - Aluno Reprovado;
# Nota >5 e <7  - Aluno em recuperação
# Nota ≥7 - Aluno Aprovado

nota = float(input('Digite a nota do aluno: '))
presenca = float(input('Digite a presença do aluno [25%, 50%, 75% ou 100%]: '))

if presenca >= 75:
    if nota >= 7:
        print('Aluno Aprovado')
    elif nota > 5 and nota < 7:
        print('Aluno em recuperação')
    else:
        print('Aluno Reprovado')
if presenca < 75:
    print('Aluno Reprovado')