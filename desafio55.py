def football_lineup(name, team):
    print(f'🎮 Time - {name} 🎮'.center(50, '-'))
    print('👥Jogadores: ')
    for i, player in enumerate(team):
        print(f'{i+1}. {player.capitalize()}')
    print('-'*50)
football_lineup('UFPB SPORTS', ['john','victor','junior'])
football_lineup('LCC News Students', ['John','José','Pedro','Emanuel','Mayara', "Yasmin", 'Juliana', 'nathalia'])
