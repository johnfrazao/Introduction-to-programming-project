pontos = 0
print('-'*35)
print(f'{'  JOHN-DEV INVESTIMENTOS':^35}')
print('-'*35)
idade = int(input('Qual a sua idade? '))
tempo = int(input('Por quanto tempo pretende manter o investimento (Em anos)? '))
print('_'*35)
print("""Qual a sua reação a uma queda de 20% no mercado?
    [1] = Vendo tudo
    [2] = Vendo parte
    [3] = Mantenho
    [4] = Compro mais""")
print('_'*35)
resp = int(input('Responda de acordo com o número referente: '))
# Calculando pontos de idade
if idade <= 30:
    pontos = 10
elif idade <= 50:
    pontos = 5
else:
    pontos = 2
# Calculando pontos de tempo
if tempo <= 2:
    pontos += 2
elif 2 <= tempo <= 5:
    pontos += 5
else:
    pontos += 10
# Calculando pontos da reação ao mercado
if resp == 1:
    pontos = pontos
elif resp == 2:
    pontos += 5
elif resp == 3:
    pontos += 10
elif resp == 4:
    pontos += 15
else: 
    print('Resposta inválida. O perfil do cliente pode receber uma classficação inadequada. Por favor responda corretamente o programa novamente.')
print(f'Você fez {pontos} pontos. Classificação:', end=' ')
if pontos <= 15:
    print('Perfil Conservador. ')
elif pontos <= 20:
    print('Perfil Moderado.')
else:
    print('Perfil Agressivo.')