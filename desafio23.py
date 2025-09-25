nota1 = nota2 = nota3 = 0
for c in range(1,4):
    nota = float(input(f'Digite a {c}ª nota: '))
    if c == 1:
        nota1 = nota
    elif c == 2:
        nota2 = nota
    elif c == 3:
        nota3 = nota
if nota1 < nota2 < nota3:
    print('Parabéns! Você vai ganhar o prémio.')
else:
    print('Que pena... Não foi dessa vez... Continue se esforçando!')