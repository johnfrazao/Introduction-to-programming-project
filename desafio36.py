numeros = []
soma_par =soma_impar = 0
for c in range(1,11):
    numeros.append(int(input(f'Digite o {c} número: ')))
for n in numeros:
    if n % 2 == 0:
        soma_par += n
    else:
        soma_impar += n
print(numeros)
print(f'A soma dos números pares foi {soma_par} e a dos impares foi {soma_impar}')

