import yfinance as yf

ticker = input('\nDigite o código ticker da ação: ')
unidade_tempo = input('\nDigite se você vai fazer a análise em dias [d], meses [m] ou anos [a]: ')

match unidade_tempo:
    case 'd':
        tipo_tempo = 'dias'
    
    case 'm':
        tipo_tempo = 'meses'
    
    case 'a':
        tipo_tempo = 'anos'

    case _:
        tipo_tempo = 'Formato inválido!'
        exit()

tempo = input(f'\nDigite até quantos {tipo_tempo} é a análise (escreva um número inteiro): ')

match unidade_tempo:
    case 'd':
        tempo = f'{tempo}d'
    
    case 'm':
        tempo = f'{tempo}mo'
    
    case 'a':
        tempo = f'{tempo}y'

dados = yf.Ticker(ticker).history(tempo)
fechamento = dados.Close

maximo_fechamento = round(fechamento.max(), 2)
minimo_fechamento = round(fechamento.min(), 2)
atual_fechamento = round(fechamento[-1])

print()
print(f'Cotação Máxima: R$ {maximo_fechamento}')
print(f'Cotação Mínima: R$ {minimo_fechamento}')
print(f'Cotação Atual: R$ {atual_fechamento}', '\n')





