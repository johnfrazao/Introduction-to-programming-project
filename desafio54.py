def check_stock(name, value):
    print('-'*50)
    print(f'📦 Estoque do Produto: {name}'.center(50))
    print(f'➡️Quantidades disponiveis: {value}')
    if value == 0:
        print("\033[31m🔴Sem Estoque. Reabastecer Imediatamente.\033[m")
    elif 1 < value <10:
        print('\033[33m🟡Estoque Baixo. Recomendado Reabastecer.\033[m')
    else:
        print('\033[32m🟢Estoque Ok. Não é necessário reabastecer.\033[m')
    print('-'*50)
check_stock('Acer Nitro v15', 11)
check_stock('Iphone 13', 3)
check_stock('Café', 0)