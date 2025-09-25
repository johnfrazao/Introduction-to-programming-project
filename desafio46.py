programacao_cinema = [
    ["Duna: Parte Dois", "Sala 1", "20:30"],
    ["O Menino e a Garça", "Sala 3", "19:00"],
    ["Kung Fu Panda 4", "Sala 2", "17:45"],
    ["Godzilla e Kong", "Sala 1", "18:00"]
]
print('Filmes no catálogo:')
print('-'*50)
for movie in programacao_cinema:
    print(f'\tFilme: {movie[0]}')
    print(f'\tLocal: {movie[1]}')
    print(f'\tHorário: {movie[2]}')
    print('-'*50)