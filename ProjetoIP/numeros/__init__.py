vermelho = '\033[31m'
verde = '\033[32m'
nada = '\033[m'
amarelo = '\033[33m'
laranja = '\033[38;5;208m'
negrito = '\033[1m'

def lerTelefone(msg):
    while True:

        try:
            print(f'{negrito}Telefone: (00) 0 0000-0000')
            telefone = str(input(msg)).strip()
            telefone = (telefone.replace(' ','')
                        .replace('(', '').replace(')', '')
                        .replace('.', '')).replace('-','')

            if telefone.isdigit() and len(telefone) == 11:
                telefoneFormatado = f'({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}'
                return telefoneFormatado
            else:
                print(f'{negrito}{vermelho}ERRO! Por favor digite um número válido.{nada}')

        except KeyboardInterrupt:
            print(f'\n{negrito}{vermelho}O usuário decidiu não informar nenhuma opção.{nada}')
            return ''
def lerData(msg):
    while True:
        try:
            print(f'{negrito}Data: Dia/Mês/Ano')
            data = str(input(msg)).strip()
            data = data.replace('/', '').replace(' ', '')
            if data.isdigit() and len(data) == 8:
                dataFormatada = f'{data[:2]}/{data[2:4]}/{data[4:]}'
                return dataFormatada
            else:
                print(f'{negrito}{vermelho}ERRO! Por favor digite uma data válida.{nada}')
        except KeyboardInterrupt:
            print(f'\n{negrito}{vermelho}O usuário decidiu não informar nenhuma opção.{nada}')
            return ''

def lerHora(msg):
    while True:
        try:
            print(f'{negrito}Hora: XX:XX')
            hora = str(input(msg)).strip()
            hora = hora.replace(' ', '').replace(':', '')
            if hora.isdigit() and len(hora) == 4:
                horaFormatada = f'{hora[:2]}:{hora[2:]}'
                return horaFormatada
            else:
                print(f'{negrito}{vermelho}ERRO! Por favor digite uma data válida.{nada}')
        except KeyboardInterrupt:
            print(f'\n{negrito}{vermelho}O usuário decidiu não informar nenhuma opção.{nada}')
            return ''
