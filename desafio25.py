carlos = joana = 0
# Título apresentável
print('_'*39)
print(f'{'  ELEIÇÔES UFPB':^35}')
print('_'*39)

# Tabela do número referente ao candidato
print("""Nº Dos votos:
    Carlos N° = 10
    Joana  N° = 20""")

# Contabilizando os votos
while True:
    voto = int(input('Digite seu voto [0 para parar]: '))
    if voto == 10:     # Votos para Carlos
        carlos += 1
    elif voto == 20:   # Votos para Joana
        joana += 1
    elif voto == 0:    # Encerrar o programa
        break
    else:   # Caso digite um valor indesejável
        continue

# Mostrando os resultados finais
print(f'{'< FIM DA ELEIÇÃO >':-^35}')
print(f'Votos para Carlos (10): {carlos}')
print(f'Votos para Joana (20): {joana}') 

# Calculando o vencedor/empate
if carlos > joana:
    print(f'O vencedor foi Carlos.')
elif joana > carlos:
    print(f'O vencedor foi Joana.')
elif joana == carlos:
    print('EMPATE! Não ouve ganhador.')
    