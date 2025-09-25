# Variável igual a 0
totpassos = 0

# Loop registrando os passos e somando eles em uma variável.
for c in range(1,8):
    passos = int(input(f'Digite a quantidade de passos no dia {c}: '))
    totpassos += passos

media = totpassos // 7 # Calcula a média de passos inteiros

# Mostrando valores no terminal
print('-'*35)
print(f'O total de passos dados foi: {totpassos}.')
print(f'A média de passos dados foi: {media}.')
print('-'*35)