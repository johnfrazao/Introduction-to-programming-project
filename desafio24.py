hp = 100
contvida = contmonstro = 0
for c in range(1,9):
    print('_'*35)
    print("""Desafios:
    [M] --> Monstro
    [P] --> Poção de Vida""")
    desafio = str(input('Digite o desafio: ')).upper().strip()[0]
    if desafio == 'M':
        dano = int(input('Quanto foi o dano? '))
        hp -= dano
        if hp > 0:
            contmonstro += 1
    elif desafio == 'P':
        cura = int(input('Quanto foi a cura? '))
        if cura + hp > 100:
            hp = 100
            contvida += 1
        else:
            hp += cura
            contvida += 1
    print('_'*35)
    print(f'PV: {hp}')
    if hp <= 0:
        print('Você morreu.')
        break
print('_'*35)
print(f"""Estatísticas:
Pontos de Vida [PV]: {hp}
Poções de vida usadas: {contvida}
Lutas sobrevividas: {contmonstro}
""")