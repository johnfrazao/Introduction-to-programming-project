# Variável igual a 0
totpag = 0
# Loop registrando as páginas durante 15 dias
for c in range(1,16):
    pag = int(input(f'Quantas páginas você leu no dia {c}? '))
    totpag += pag # Soma todas as páginas e armazena em uma variável.

# Calcula a média de páginas por dia
media = totpag // 15

# Mostrando valores no terminal
print('='*35)
print(f'Total de páginas lidas: {totpag}.')
print(f'Média de páginas lidas por dia: {media}')
if totpag >= 1200:
    print('Parabéns! Você atingiu sua meta!')
else:
    print('Que pena! Você não atingiu sua meta!')
print('='*35)


