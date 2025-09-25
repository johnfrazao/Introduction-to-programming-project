agend = []
for c in range(1,5):
    while True:
        nome = str(input('Digite seu nome: ')).strip()
        if nome.replace(' ', '').isalpha():
            break
        else:
            print('\033[31mERRO! Por favor digite um nome válido.\033[m')
    while True:
        num = str(input('Digite seu Telefone (com DDD): ')).strip()
        num = num.replace('(', '').replace(')', '').replace('-', '').replace(' ', '')
        if num.isnumeric() and len(num) == 11:
            break
        else:
            print('\033[31mERRO! Por favor digite um número válido.\033[m')
    agend.append([nome, num])
print('Sua Agenda de Contatos'.center(50, '-'))
for i, n in enumerate(agend):
    phone_formatted = f'({n[1][:2]}) {n[1][2:7]}-{n[1][7:]}'
    print(f'{i}.Nome: {n[0]:<20} | Telefone: {phone_formatted}')
print('-'*50)