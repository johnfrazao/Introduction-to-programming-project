candidatos = [
    ["João", 5, "Python"],
    ["Maria", 6, "Java"],
    ["Lucas", 3, "Python"],
    ["Fernanda", 7, "Python"],
    ["Marcos", 4, "C#"]
]
print('Candidatos elegíveis: ')
for name in candidatos:
    if name[1] >= 4 and name[2] == 'Python':
        print(f'{name[0]:<10} - Experiência: {name[1]} anos - Linguagem: {name[2]}')
