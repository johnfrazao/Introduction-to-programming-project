# Variáveis iguais a 0
kgtomate = kgalface = kgcenoura= total = soma = 0

# Valor em R$ por KG de cada produto
alface = 3
tomate = 5
cenoura = 4

# Loop para fazer os 10 produtos com todos os calculos
for c in range(1,11):
    product = ' '
    while product not in 'TAC':
        print("""Produtos:

|  [T] --> Tomate  
|  [A] --> Alface  
|  [C] --> Cenoura 
""")
        product = str(input(f'Digite o produto {c}: ')).upper().strip()[0]
    kg = float(input('Digite a quantidade de KG: '))
    print('_'*35)
    # Calculando o preço de acordo com os kilos.
    if product == 'T':
        soma = kg * tomate  # Variável soma calcula o preço, isso pra todos os casos.
        kgtomate += kg    # Calcula a quantidade de kilos de tomate

    elif product == 'A':
        soma = kg * alface
        kgalface += kg    # Calcula a quantidade de kilos de alface

    elif product == 'C':
        soma = kg * cenoura
        kgcenoura += kg   # Calcula a quantidade de kilos de cenoura

    total += soma # Pega todas as somas e transforma no preço total final.

# Mostrando valores no terminal
print('_'*35)
print(f'Receita total do dia: R${total:.2f}')
print(f'Kilos de tomate comprado: {kgtomate:.2f}')
print(f'Kilos de alface comprado: {kgalface:.2f}')
print(f'Kilos de cenoura comprado: {kgcenoura:.2f}')
print('_'*35)