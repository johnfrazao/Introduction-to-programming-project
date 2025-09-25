produto = []
preco = []
maior = float('-inf')
name_greater = ''
for c in range(1, 6):
    nome = str(input(f'Digite o nome do {c} produto: '))
    valor = float(input(f'Digite o preço do {c} produto: R$'))
    produto.append(nome)
    preco.append(valor)
for i, n in enumerate(preco):
    if n > maior:
        maior = n
        name_greater= produto[i]
print(f'O produto mais caro foi {name_greater} custando R${maior:.2f}.')
