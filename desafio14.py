saldo = 2500
resp = 0
print('-'*39)
print(f'{"BEM VINDO AO BANCO CENTRAL JDEV":^35}')
print('-'*39)

while saldo != 0:
    
    resp = float(input('Digite o valor do saque: R$'))
    print('_'*35)
    if resp <= saldo:
        saldo = saldo - resp
        print(f'Transação concluída!\nSaldo atual: R${saldo:.2f}')
        if saldo == 0:
            print('Fim das operações. Tenha um bom dia!')
            print('_'*35)
            break
    else:
        print(f'Saldo insuficiente para este saque. Saldo atual: R${saldo:.2f}')