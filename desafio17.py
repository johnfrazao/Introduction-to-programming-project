estoque = 100
while True:
    if estoque > 0:
        print('_'*35)
        print("""Opções:
            [0] - Sair
            [1] - Adicionar
            [2] - Remover
            """)
    
        resp = int(input('O que deseja fazer? '))
        if resp == 0:
            print('< FIM DO PROGRAMA >')
            print(f'Estoque atual: {estoque}')
            break

        quantd = int(input('Quantidade? '))
        if quantd <= estoque:    
            if resp == 1:
                estoque += quantd
            elif resp == 2:
                    estoque -= quantd
                
        else:
            print('Estoque insuficiente para essa remoção.')
        print('-'*35)
        print(f'Estoque atual: {estoque}')
    else:
        print('_'*35)
        print('< FIM DO PROGRAMA >')
        break
    
