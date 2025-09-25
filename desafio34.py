list = []
for c in range(1,8):
    num = int(input(f'Digite o {c} numero: '))
    list.append(num)
print(f'Lista original {list}')
for n in list:
    if n % 2 == 0:
        list.remove(n)
print(f'Lista atualizada sem os números pares {list}')