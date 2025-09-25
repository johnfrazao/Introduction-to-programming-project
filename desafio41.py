products = [] # List to store the products

# loop to collects the products datas
for c in range(1, 5):
    name = str(input(f'Nome do {c} produto: ')).strip().capitalize()
    price = int(input(f'Quantos em estoque do {c} produto: '))
    products.append([name, price]) # Adds name and price in list products
    print('-'*50)
# Travels the list of products to check the low stock
for product in products:
    if product[1] < 10: # Checks if the stock is below of 10
        print(f'\033[31mAtenção! Estoque baixo para {product[0]}.\033[m')
        print(f'Apenas {product[1]} unidades restantes.')

print('Fim do programa.'.center(50, '-'))