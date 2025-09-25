# Variáveis iguais a 0
cont = value_total = value_end = discount = 0
porcentagem = 10/100 # Porcentagem de 10%

# Título
print('_'*35)
print(f'{'MERCADINHO UFPB':^35}')
print('_'*35)
# Entrada do preço e cálculo do desconto
while True:
    cont += 1 # Apenas para deixar o input numerado
    preco = float(input(f'Digite o preço do {cont}º produto [0 pra parar]: R$'))

    value_total += preco # Calcula o preço total

    if preco == 0: # Finaliza o programa caso a entrada seja = 0
        break

    if value_total > 200: # Calculo do desconto
        discount = value_total * porcentagem
        value_end = value_total - discount

    else: # Se o desconto não for aplicável, o valor final é o mesmo do total
        value_end = value_total

# Mostrando valores no terminal
print(f'{'< TABELA FINAL >':-^35}')
print(f'Total da compra: R${value_total:.2f}')

if value_total >200: # Caso o desconto seja aplicável, mostra na tela
    print(F'Desconto de 10% : R${discount:.2f}')

print(f'Valor final a pagar: R${value_end:.2f}')
print('-'*35)