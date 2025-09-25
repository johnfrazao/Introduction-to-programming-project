print('='*35)
print(f'{'  CENTRAL DE ATENDIMENTO H. SAÚDE'}')
print('='*35)

custo = 0
print('_'*35)
print("""Tipos de Quarto:
    [1] = Quarto Particular
    [2] = Quarto Semi-Particular
    [3] = Quarto Coletivo  """)
print('_'*35)
quarto = int(input("Digite o tipo de quarto referente ao número: "))
dias = int(input('Quantos dias vão passar nesse quarto? '))
equip = str(input('Houve uso de equipamentos da UTI? [S/N] ')).upper().strip()[0]
if quarto <= 3:
    if quarto == 1:
        custo = dias * 500
    elif quarto == 2:
        custo = dias * 350
    else:
        custo = dias * 200
    if equip == 'S':
        custo = custo + 1200
    print('_'*35)
    print(f'O valor total da internação é de: R${custo:.2f}')
else:
    print('_'*35)
    print('Tipo de quarto inválido.')