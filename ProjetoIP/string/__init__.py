from time import sleep
verde = '\033[32m'
nada = '\033[m'
amarelo = '\033[33m'
laranja = '\033[38;5;208m'
negrito = '\033[1m'

def leiaInt(msg): # Função para validar apenas números inteiros
    while True:
        try:
            valor = int(input(msg))
            return valor

        except (ValueError, TypeError):
            print('\033[31mERRO! Por favor digite um número válido.\033[m')

        except KeyboardInterrupt:
            valor = 0
            print('\n\033[31mO usuário decidiu não informar nenhuma opção.\033[m')
            print('Finalizando o Programa...')
            return valor



def lerString(msg): # Valida apenas strings

    while True:
        try:
            resposta = input(msg).strip()

            # Verifica se tem apenas letras e espaços
            if resposta.replace(" ", "").isalpha():
                return resposta.title()  # cada palavra com inicial maiúscula
            else:
                print('\033[31mERRO! Por favor, digite apenas letras.\033[m')

        except ValueError:
            print('\033[31mERRO! Entrada inválida.\033[m')

        except KeyboardInterrupt:
            print('\n\033[31mO usuário decidiu não informar uma opção.\033[m')
            sleep(1)
            return ''

def linha(tam = 50): # Printa uma linha com tamanho = tam
    linha = '-' * tam
    linha = f'{linha}'
    return linha

def tituloFormatado(titulo): # Formata uma mensagem em um título formatado
    """

    :param titulo: Mensagem que queira utilizar no título
    :return: Retorna o titulo formatado
    """
    titulo = titulo.upper()
    print()
    print(f'{negrito}{linha()}{laranja}')
    print(f'{titulo}'.center(50))
    print(f'{nada}{negrito}{linha()}')
    sleep(0.5)

def menu(lista, titulo=''):
    """
    :param lista: Recebe uma lista e transforma em um menu numerado
    :param titulo: Titulo que queira utilizar para identificar a lista
    :return: retorna uma lista com opções numeradas para a escolha
    """

    while True:
        print(f'{titulo}'.center(50, '-'))

        for i, item in enumerate(lista):
            print(f"\033[1;1;1m[{i}] - {item}")
        print(linha())

        opcao = leiaInt("Digite sua opção: ")

        if 0 <= opcao <= len(lista): # verifica se a opção escolhida tem na lista
                return opcao
        else:
            print("\033[31mERRO! Escolha uma opção válida.\033[m")






def mostrar_cardapio(produtos): # Mostra uma lista formatada, como se fosse um cardápio
    verde = '\033[32m'
    nada = '\033[m'
    amarelo = '\033[33m'
    laranja = '\033[38;5;208m'
    negrito = '\033[1m'


    print(linha())
    tituloFormatado('📃😋PRODUTOS DISPONÍVEIS😋📃')
    print(linha())


    for produto in produtos:
        print(f'{laranja}- {produto.title()}')


    print(nada, linha())
    print(f'- {negrito}{laranja}Cento: {verde}R$70,00{nada}')
    print(f'- {negrito}{laranja}Cento Mini Hambúrguer ou Mini Pizza: {verde}R$200,00')
    print(f'- {negrito}{laranja}Entrega: {verde}R$5,00{nada}')
    print(f'- {negrito}{laranja}Cartão de Crédito: {verde}Taxa de acréscimo em cima do\n'
          f'  valor total do pedido{nada}')
    print(f'- {negrito}{laranja}A partir de {verde}200{laranja} salgados, o pedido só será\n'
          f'  confirmado mediante a pagamento de {verde}50%{laranja} do\n'
          f'  valor total do pedido{nada}')
    print(linha())
    sleep(0.5)
