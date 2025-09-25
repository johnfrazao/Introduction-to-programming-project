def create_roadmap(city,roadmap):
    print(f' ✈️Roteiro para a cidade: {city} ✈️'.center(50, '-'))
    for i, item in enumerate(roadmap):
        print(f'{i+1}. {item}')
    print(' ☀️Boa Viajem e aproveite o roteiro! '.center(50, '-'))
    print('\n')
create_roadmap('Paris',['Museu', 'Praça', 'Restaurante', 'Sorveteria', 'Zoologico'])
create_roadmap('Guarabira', ['Frei Damião', 'Praça dos Pombos', 'Casa Do Açai', 'Praça do Victor', 'Esplanada'])


