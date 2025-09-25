# Variável iniciada com zero
tot_parafusos = 0

# Loop para registrar a quantidade de parafusos
for c in range(1,9):
    parafusos = int(input(f'Digite a quantidade de parafusos da {c}ª hora:  '))
    tot_parafusos += parafusos # Somando todos os parafusos a cada loop

# Calculando a média de unidades por hora.
media = tot_parafusos // 8

# Mostrando dados no terminal
print('_'*38)
print(f'A produção total foi de: {tot_parafusos} unidades.')
print(f'Média de {media} parafusos por hora.')
if tot_parafusos > 1000:
    print('Parabéns! A equipe receberá o bônus.')
else:
    print('A meta de bônus não foi atingida.')
print('_'*38)