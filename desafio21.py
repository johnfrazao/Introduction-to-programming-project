valor = 0
cont = 0
for c in range(10):
    print('-'*35)
    print("""Dia da Viagem:
    U --> Dia útil 
    F --> Fim de semana""")
    print('-'*35)
    dia = str(input(f'Qual dia será a {c+1}ª viagem? ')).upper().strip()[0]
    if dia == 'U':
        valor += 4.50
        cont += 1
    elif dia == 'F':
        valor += 3
        cont += 1
    else:
        print('\033[31mDia da viagem não identificado. Nenhum custo será somado.\033[m')
print(f'O gasto total com {cont} viagens foi \033[32mR${valor:.2f}\033[m.')
    

   
    
    
