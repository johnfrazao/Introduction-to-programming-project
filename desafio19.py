saldo = 200
cont = 0
while saldo < 1500:
    cont += 1
    deposito = float(input(f'Digite o valor o valor do mês {cont}: R$'))
    saldo += deposito
    print(f'Novo saldo: \033[32mR${saldo:.2f}\033[m.')
    print('_'*35)
print('\033[32mParabéns! Você atingiu sua meta.\033[m')
print(f'Valor total guardado: R${saldo:.2f}.')
print(f'Você levou {cont} meses para atingir a meta.')
print('_'*35)
