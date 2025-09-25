planta_casa = [
    ["Sala", 5.0, 4.5],
    ["Quarto 1", 3.0, 4.0],
    ["Banheiro", 2.0, 2.5],
    ["Cozinha", 4.0, 4.0]
]
square_area = []
for room in planta_casa:
    area = room[1]*room[2]
    name = room[0]
    square_area.append([name, area])
for room in square_area:
    print(f'| {room[0]:<15}- {room[1]:.2f} m²')

