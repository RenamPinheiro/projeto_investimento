from analise_de_investimento import maximo_fechamento, minimo_fechamento, atual_fechamento, ticker
import pyautogui as pya
import pyperclip as pyp

nome = input('Digite seu nome: ')
email = input('Digite o email de destino: ')

pya.PAUSE = 1

pya.press('win')

pya.write('Google')

pya.press('enter')

pya.click(x=1017, y=640)

pya.write('Outlook.com')

pya.PAUSE = 6

pya.press('enter')

pya.PAUSE = 1

pya.click(x=126, y=226)

pya.write(email)

pya.press('enter')

pya.press('tab')

pyp.copy('Análise de investimentos')

pya.hotkey('ctrl', 'v')

pya.press('tab')

mensagem = f'''
Prezado Gestor,
          
Seguem as análises de investimentos solicitadas da ação {ticker}:
          
Cotação Máxima: R$ {maximo_fechamento}
Cotação Mínima: R$ {minimo_fechamento}
Cotação Atual: R$ {atual_fechamento}

Atenciosamente. 
{nome}
'''

pyp.copy(mensagem)

pya.hotkey('ctrl', 'v')
