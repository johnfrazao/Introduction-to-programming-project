
relatorio_vendas = [
    ["Mariana", 55000.00],
    ["Rafael", 72000.00],
    ["Mariana", 89000.00],
    ["Lucas", 68000.00],
    ["Rafael", 45000.00],
    ["Mariana", 120000.00]
]
sales = qtd_sales = 0
while True:
    name = str(input('Nome do vendedor: ')).strip().capitalize()
    if name.isalpha():
        break
    else:
        print('ERRO! digite um nome válido.')

for seller in relatorio_vendas:
    if seller[0] == name:
        sales += seller[1]
        qtd_sales += 1

if sales > 0:
    average = sales / qtd_sales
    print(f'O total de vendas de {name} foi: R${sales:.2f}')
    print(f'Quantidade de vendas realizadas: {qtd_sales}')
    print(f'Média das vendas: R${average:.2f} ')
else:
    print('Vendedor não encontrado.')