turma = []
maior = float('-inf')
menor = float('inf')
nome_maior = ''
nome_menor = ''
for c in range(1,6):
    nome = str(input(f'Digite o nome do {c} aluno: '))
    nota = float(input(f'Digite a nota do {c} aluno: '))
    turma.append([nome,nota])
for nome, nota in turma:
    if nota > maior:
        maior = nota
        nome_maior = nome
    if nota < menor:
        menor = nota
        nome_menor = nome
print(f'{nome_maior} tirou a maior nota que foi {maior}')
print(f'{nome_menor} tirou a menor nota que foi {menor}')