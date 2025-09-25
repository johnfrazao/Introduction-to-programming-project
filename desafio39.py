
athletes = []

# Loop para coletar os dados
print('Competicão de Atletismo'.center(50, '-'))
for c in range(1,4):
#Valída se o nome é realmente um nome ou uma string
    while True:
        name = str(input(f'Nome do {c}º atleta: ')).strip()
        if name.replace(' ','').isalpha():
            break
        else:
            print('\033[31mERRO! Por favor digite um nome válido.\033[m')

# Valída se o tempo é realmente um número
    while True:
        try:
            time = float(input('Digite o tempo em segundos: '))
        except:
            print('\033[31mERRO! Por favor digite um tempo válido.\033[m')
        else:
            break


    athletes.append([name, time]) # Adiciona o nome e o tempo em uma lista.
# Coloca o primeiro atleta como o melhor tempo ja que foi o primeiro a ser digitado.
name_small = athletes[0][0]
shorter_time = athletes[0][1]
# Aqui verifica quem fez o menor tempo.
for person in athletes:
    if person[1] < shorter_time:
        shorter_time = person[1]
        name_small = person[0]

# Mostrando dados no terminal
print('Resultado final da competição'.center(50, '-'))
print(f'O(A) vencedor foi {name_small} com o tempo: {shorter_time:.2f}')