idade = int(input('Digite sua idade: '))
if idade <= 10:
    print('INFANTIL')
elif idade <= 17:
    print('JUVENIL')
elif idade <= 49:
    print('ADULTO')
else:
    print('SÊNIOR')