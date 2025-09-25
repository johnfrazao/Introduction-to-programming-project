frete = valortot = 0
for c in range(8):
    preco = float(input(f'Digite o preço da {c+1}ª compra: R$'))
    valortot += preco
    print('-'*35)
    print("""Regiões: 
    N --> Norte/Nordeste, Centro-Oeste 
    S --> Sul/Sudeste""")
    print('-'*35)
    regiao = str (input('Digite a região: ')).upper().strip()[0]
    if preco <= 100:
        frete += 25
    elif preco > 100:
        if regiao == 'N':
            frete += 25
        elif regiao == 'S':
            frete += 0
media = valortot / 8
print(f'O valor total arrecadado com o fretes foi R${frete:.2f}.')
print(f'O valor total da compra foi R${valortot:.2f}.')
print(f'O valor médio das compras foi R${media:.2f}.')
