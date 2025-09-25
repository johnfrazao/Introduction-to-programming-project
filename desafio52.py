def fraction(name, value, times):
    installment = value / times
    print('-'*35)
    print(f'🛒Produto {name}')
    print(f'💰Valor do Produto: R${value}')
    print(f'💳Parcelado em {times}x: R${installment:.2f}')
    print('-'*35)
fraction('Acer Nitro v15', 4999, 12)
fraction('Iphone 13', 3000, 12)