maior = totDoacao = quantDoacao = doacao = 0
print('-'*39)
print(f'{'  ONG Patinhas Aquecidas':^35}')
print('-'*39)
while True:
    doacao = float(input('Digite o valor da doação: R$'))
    if doacao < 0:
        print('\033[31mNenhuma doação foi registrada.\033[m')
        break
    else:
        print('\033[32mDoação registrada com sucesso!\033[m')
    print('_'*35)
    quantDoacao += 1
    totDoacao += doacao
    if doacao > maior:
        maior = doacao
print('_'*35)
print(f"Foram feitas {quantDoacao} doações no total.")
print(f"O valor total arrecadado foi de R${totDoacao:.2f}.")
print(f"A maior doação registrada foi de: R${maior:.2f}")
print('_'*35)
