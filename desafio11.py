print('_'*39)
print(f'{'  BEM VINDO A CIA AÉREA VIAGEM SEGURA':^35}')
print('_'*39)
malas = int(input('Digite o número de malas: '))
print('='*35)
print("""Categorias: 
[1] = Bronze (Cliente Geral)
[2] = Prata
[3] = Ouro
[4] = Diamante """)
print('='*35)
classe = int(input('Digite sua categoria de acordo com o número: '))

custo = 0

if malas <= 2:
    if malas == 1:
        custo = 0
    else:
        if classe == 1:
            custo = 120
        elif classe == 2:
            custo = 60
        elif classe == 3 or classe == 4:
            custo = 0 
    print(f'Custo da bagagem: R${custo:.2f}')
else:
    print('Números inválidos de malas para esta simulação.')
