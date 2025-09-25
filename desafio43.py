cardapio = [
    ["Pão Francês", 0.50],
    ["Café Expresso", 4.00],
    ["Coxinha", 5.50],
    ["Bolo de Fubá", 12.00]
]
percent = 15/100
print('Cardápio antes do reajuste: ')
for item in cardapio:
    print(f'| {item[0]:<15} \tR${item[1]:.2f}')
print('\nCardápio depois do reajuste de 15%:')
for item in cardapio:
    increase = item[1]+ (item[1]*percent)
    print(f'| {item[0]:<15} \tR${increase:.2f}')
