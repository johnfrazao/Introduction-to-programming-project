students = [] # List to store the stundents

# Loop to collect students data
for c in range(1,5):
    name = str(input(f'Digite o nome do {c} aluno: ')).strip().capitalize()
    note1 = float(input(f'Digite a 1ª nota do {c}º aluno: '))
    note2 = float(input(f'Digite a 2ª nota do {c} aluno: '))
    average = (note1 + note2) / 2 # Calculates the average of students
    students.append([name, note1, note2, average]) # Adds all data in list

    print('='*35)
print('Tabela de Notas'.center(50, '-'))
for i, student in enumerate(students):
    print(f'{i+1}. Aluno(a): {student[0]:<10} | Nota 1: {student[1]:^5.2f} - Nota 2: {student[2]:^5.2f} - Média: {student[3]:^5.2f}')
print('-'*50)