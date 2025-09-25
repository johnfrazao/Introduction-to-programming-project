numeros = []
totzero = totnegative = totpositive = 0
for c in range(1,6):
    num = int(input(f'Digite o {c} numero: '))
    numeros.append(num)
for n in numeros:
    if n == 0:
        totzero += 1
    elif n < 0:
        totnegative += 1
    else:
        totpositive += 1
print(f'A lista tem {totzero} números 0, {totnegative} números negativos e {totpositive} positivos')