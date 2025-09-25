bateria = 100
cont = 0
while True:
    resposta = str(input('Usar ou Carregar? ')).upper().strip()
    valor = int(input('Quantos % ? '))

    if resposta == 'USAR':
        bateria -= valor
        cont += 1
    elif resposta == 'CARREGAR':
        if bateria + valor > 100:
            bateria = 100
        else:
            bateria += valor
    
    print(f'Bateria: {bateria}%')
    if bateria <= 0:
         print('Celular descarregado.')
         print(f'Total de ações usadas antes de descarregar: {cont}')
         break
    