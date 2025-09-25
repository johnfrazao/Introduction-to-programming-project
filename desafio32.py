list = []
while True:
    num = (int(input('Digite um número: ')))
    if num < 0:
        break
    else:
        list.append(num)
list.sort(reverse=True)
print(list)