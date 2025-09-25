senha = 'Python123'
resp = ' '
verde = '\033[32m'
vermelho = '\033[31m'
while resp != senha:
    resp = str(input('Digite sua senha: '))
    if resp == senha:
        print(verde,'Acesso permitido!\033[m')
        break
    else:
        print(vermelho,'Senha incorreta. Tente novamente\033[m')