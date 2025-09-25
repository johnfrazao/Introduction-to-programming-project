idade = int(input('Digite sua idade: '))
peso = float(input('Digite seu peso: '))
if 18 <= idade <= 69:
    if peso > 50:
        print('Você está apto para doar sangue.')
    else:
        print('Infelizmente você não atende a todos os requesitos para doação nesse momento.')
else:
    print('Infelizmente você não atende a todos os requesitos para doação nesse momento.')