senha = 'root'
resp = ' '
verde = '\033[32m'
vermelho = '\033[31m'
cont = 0
while resp != senha:
    resp = str(input('Digite sua senha: '))
    if resp == senha:
        print(verde,'Acesso permitido!\033[m')
        break
    else:
        cont += 1
        print(vermelho,f'Senha incorreta. Tentativa({cont}/3)\033[m')
        if cont == 3:
            print('Conta bloqueada por excesso de tentativas.')
            break