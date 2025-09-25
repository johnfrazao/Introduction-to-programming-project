from unidecode import unidecode
def saudacao(nome, cidade):
    cidade= unidecode(cidade).upper()
    if cidade == 'JOAO PESSOA':
        print(f'Bem vindo à cidade de João Pessoa!\nÉ um prazer ter você por aqui, {nome}!')
    else:
        print(f'Bem Vindo {nome}!' )
saudacao('John','João Pessoa')
saudacao('Ryevellyn', 'Guarabira')