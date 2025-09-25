def reportstudent(name,nota1,nota2,nota3,nota4):
    average = (nota1 + nota2 + nota3 + nota4) / 4
    print(f' Relatório do aluno {name} '.center(50, '-'))
    print(f'|  1ª Nota: {nota1:>4.1f} |  2ª Nota: {nota2:>4.1f}')
    print(f'|  3ª Nota: {nota3:>4.1f} |  4ª Nota: {nota4:>4.1f}')
    print('-'*50)
    print(f'|  Média: {average:.1f}')
    if average >= 7:
        print('|  Situação: \033[32m✅Aprovado\033[m')
    else:
        print('|  Situação: \033[31m❌Reprovado\033[m')
    print('-'*50)
    print()
reportstudent('John',10,10,9,10)
reportstudent('Cleiton',8,4,5,10)