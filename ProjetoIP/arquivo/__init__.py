from string import *
vermelho = '\033[31m'
verde = '\033[32m'
nada = '\033[m'
amarelo = '\033[33m'
laranja = '\033[38;5;208m'
negrito = '\033[1m'
azul = '\033[34m'

def cadastrar(arq, nome, telefone, hora, data, endereco, valor, pedidos, totalSalgados, FormaDePagamento):
    """

    :param arq: Nome do arquivo
    :param nome: Nome do Cliente
    :param telefone: Telefone do Cliente para contato
    :param hora: Hora para retirar o pedido
    :param data: Data de retirada do pedido
    :param endereco: Endereço do cliente
    :param valor: Valor final do pedido
    :param pedidos: Produtos do cliente em específico, não confundir com pedidos geral de todos os clientes
    :param totalSalgados: Total de unidades de todos os salgados do pedido do cliente
    :param FormaDePagamento: Forma de pagamento do cliente
    :return: Escreve e formata todos os dados descritos em um arquivo
    """
    with open(arq, 'a', encoding='utf-8') as arquivo:
        arquivo.write(negrito+linha() + '\n')
        arquivo.write(f'{negrito}{laranja}Cliente: {nada} {nome}\n')
        arquivo.write(f'{negrito}{laranja}Telefone: {nada} {telefone}\n')
        arquivo.write(f'{negrito}{laranja}Horário: {nada} {hora}\n')
        arquivo.write(f'{negrito}{laranja}Data: {nada} {data}\n')
        arquivo.write(f'{negrito}{laranja}Endereço: {nada} {endereco}\n')
        arquivo.write(f'{negrito}{laranja}Forma de Pagamento:{nada}  {FormaDePagamento}\n')
        arquivo.write(f'{negrito}{laranja}Pedidos:{nada}\n')


        for item in pedidos:
            arquivo.write(f'{negrito}{amarelo}  - {item}\n')

        arquivo.write(f'{negrito}{laranja}Total de salgados:{amarelo}  {totalSalgados}  {nada}\n')
        arquivo.write(f'{negrito}{laranja}Valor Final: {verde}  R${valor:.2f}  {nada}\n')
        arquivo.write(negrito+linha() + '\n')

        arquivo.write('-' * 50 + '\n')




def verPedidos(arq):
    """
    :param arq: Nome do arquivo
    :return: Retorna todos os pedidos feitos caso tenha no arquivo
    """
    with open(f'{arq}', 'r', encoding='utf-8') as arquivo:
        pedidos = arquivo.read()
        if pedidos == '' or pedidos == '\n':
            print(f'\033[1;31mNenhum pedido foi encontrado\033[m')
        else:
            print(pedidos)
