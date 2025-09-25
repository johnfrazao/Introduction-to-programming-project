horas = int(input('Digite a hora (Apenas os dois primeiros dígitos): '))
if 5 <= horas <= 11:
    print('Bom dia!')
elif 12 <= horas <= 17:
    print('Boa tarde!')
elif 18 <= horas <= 23:
    print('Boa noite!')
elif 0 <= horas <= 4:
    print('Boa madrugada!')