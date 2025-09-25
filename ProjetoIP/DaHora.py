# Importações das funções criadas para usar no código,
# o [*] indica que ele está importando todas as funções presentes na biblioteca
from ProjetoIP.numeros import lerTelefone, lerData, lerHora
from string import *
from arquivo import *
from string import leiaInt
from time import sleep

# Variáveis que serão usadas no código
valor = 0
unidadesTotal = 0
arq = 'pedidos.txt'

# Lista de todos os produtos REAIS disponíveis na lanchonete
produtos = [
    "Pastel Doce",
    "Pastel Salgado",
    "Coxinha",
    "Bolinha de queijo",
    "Croquete de carne",
    "Balãozinho de calabresa",
    "Rolinho de pizza",
    "Empada Doce",
    "Empada Salgada",
    "Pãozinho misto",
    "Mini frangote",
    "Mini hambúrguer",
    "Mini pizza"
]

pedidos_clientes = [] # Lista para armazenar o produto de escolha do cliente

# Cores para utilizar durante o código de forma rápida e fácil
vermelho = '\033[31m'
verde = '\033[32m'
nada = '\033[m'
amarelo = '\033[33m'
laranja = '\033[38;5;208m'
negrito = '\033[1m'

# Código Principal
tituloFormatado('Bem Vindo ao Lanches Da Hora')

while True:
    unidadesTotal = 0
    pedidos_clientes = []
    resposta = menu(['Sair do Programa', 'Fazer Pedido', 'Ver Cardápio', 'Ver Pedidos'])
    sleep(0.5)

    if resposta == 0:
        tituloFormatado('Saindo do Programa... Volte sempre!')
        break


    elif resposta == 1:
        tituloFormatado('Fazer Pedido')
        print('Obs: Com entrega tem uma taxa de \033[32mR$5,00\033[1;0m')

        resposta = menu(['Sair']+['Retirada na loja', 'Entrega'])


        if resposta == 0:
            tituloFormatado('Saindo do Programa... Volte sempre!')
            break


        tituloFormatado('informações do cliente')
        nome = lerString('Digite seu Nome e Sobrenome: ')
        telefone = lerTelefone('Telefone para contato: ')
        hora = lerHora('Horário do dia de retirada: ')
        data = lerData('Data do dia de retirada do pedido: ')

        if nome == '' or telefone == '' or hora == '' or data == '':
            print(f'{vermelho}Você deixou algum dado em branco, faça o pedido novamente.{nada}')
            tituloFormatado('Saindo do Programa... Volte sempre!')
            break

        print(linha())

        valor = 0

        while True:

            print(linha())
            salgados = menu(['Sair']+produtos,'Escolha uma opção por vez')

            if salgados == 0:
                tituloFormatado('Finalizando pedido...')
                break

            unidade = leiaInt('Digite a quantidade de unidades: ')

            if 1 <= salgados <= 11:
                precoPorUnidade = 0.7
                preco = unidade * precoPorUnidade
                valor += preco
                unidadesTotal += unidade


            elif salgados == 12 or salgados == 13:
                precoPorUnidade = 2
                preco = unidade * precoPorUnidade
                valor += preco
                unidadesTotal += unidade


            else:
                print('\033[31mERRO! Coloque um opção válida!\033[m')


            pedidos_clientes.append(f'{produtos[salgados-1]} - Unidades: {unidade}')
            linha()
            for pedido in pedidos_clientes:
                print(f'{laranja} - {pedido}{nada}')
            print(f'{laranja}{negrito}Total de Salgados: {unidadesTotal}{nada}')
            print(f'{negrito}Valor do pedido: {verde}R${valor:.2f}{nada}{negrito}')

        if unidadesTotal >=200:
            print(f'{vermelho}ATENÇÃO')
            print(f'Seu pedido passou de {verde}200 salgados{vermelho}.\nPara a segurança do comerciante, o pedido só será\n'
                  f'confirmado mediante a {verde}50%{vermelho} vo valor total do pedido{nada}')

        print(f'{negrito}Obs: No Cartão de CRÉDITO tem uma taxa em cima do\nvalor do pedido')
        pagamento = menu(['Cancelar Pedido']+['Dinheiro', 'Cartão', 'Pix'],'Forma de Pagamento')


    # Condições para verificar e declarar a forma de pagamento
        if pagamento == 0:
            print(f'{vermelho}{negrito}Cancelando pedido...')
            sleep(1)
            print(f'{verde}{negrito}Seu pedido foi cancelado com sucesso!{nada}{negrito}')
            continue

        elif pagamento == 1:
            formaDePagamento = 'Dinheiro'

        elif pagamento == 2:
            taxa = 6/100 # 6% de taxa da maquininha
            valor = valor / (1-taxa) # Calcula o valor final com a taxa que será cobrada pela maquininha
            formaDePagamento = 'Cartão'

        elif pagamento == 3:
            formaDePagamento = 'Pix'


    # Condições para adicionar ou não o endereço e taxa de entrega caso seja entrega
        if resposta == 1 and pagamento != 0:
            endereco = '' # Endereço fica vazio, já que a opção escolhida não foi entrega
            cadastrar(arq, nome, telefone, hora, data, endereco, valor, pedidos_clientes, unidadesTotal, formaDePagamento)

        elif resposta == 2 and pagamento != 0:
            endereco = str(input('Informe  o endereço de entrega: '))
            cadastrar(arq, nome, telefone, hora, data, endereco, valor + 5, pedidos_clientes, unidadesTotal, formaDePagamento)

        sleep(0.3)
        print(f'{negrito}{verde}Pedido realizado com sucesso!\nObrigado pela preferência!{nada}{negrito}')
        sleep(1)


    elif resposta == 2:
        mostrar_cardapio(produtos)

    elif resposta == 3:
        verPedidos(arq)




