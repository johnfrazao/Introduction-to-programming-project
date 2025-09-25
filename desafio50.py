def mostrar_produto(name, preco=0):
    print('-'*25)
    print(f'🛒Produto: \t{name}')
    print(f'💰Preço: \tR${preco:.2f}')
    print('-'*25)
mostrar_produto('Acer Nitro v15', 4999)
mostrar_produto('Iphone 13', 3000 )