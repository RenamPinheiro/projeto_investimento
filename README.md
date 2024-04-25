Projeto Análise de Investimentos e Automação de envio de email 
====================

Este é projeto em Python chamado **projeto\_investimento** que permite realizar análises simples de investimento em ações usando a biblioteca `yfinance`. Além disso, também podemos automatizar o envio do e-mail com informações da análise.

Requisitos
----------

Antes de executar o projeto, certifique-se de ter o Python instalado em seu sistema. Além disso, você precisará instalar as bibliotecas `yfinance`, `pyautogui` e `pyperclip`. Você pode instalar as bibliotecas executando os seguintes comandos no seu terminal:

```
pip install yfinance
pip install pyautogui
pip install pyperclip
```

Como usar
---------
*   Execute o arquivo `analise_de_investimento.py` para realizar a análise de investimento em ações.
*   Execute o arquivo `email_automatico.py` para automatizar o envio do e-mail com informações da análise.

Arquivo `analise_de_investimento.py`
---------

1.  O programa solicitará que você insira o código ticker da ação que deseja analisar.
2.  Em seguida, você precisará fornecer a unidade de tempo para a análise (dias [d], meses [m] ou anos [a]).
3.  Depois, especifique a duração da análise (número inteiro de dias, meses ou anos).
4.  O programa então recuperará os dados da ação usando `yfinance` e calculará a cotação máxima, mínima e atual.
5.  Os resultados serão exibidos no terminal.

Exemplo de uso
--------------

```
Digite o código ticker da ação: AAPL

Digite se você vai fazer a análise em dias [d], meses [m] ou anos [a]: m

Digite até quantos meses é a análise (escreva um número inteiro): 6

Cotação Máxima: R$ 150.29
Cotação Mínima: R$ 135.12
Cotação Atual: R$ 147.63

```
Arquivo `email_automatico.py`
---------

O código desse arquivo utiliza as bibliotecas `pyautogui` e `pyperclip` para automatizar o envio de e-mails com informações da análise de investimento.

1.  **Atenção!** Certifique-se de ajustar as coordenadas dos cliques do mouse (usando o arquivo `coordenada_mouse.py`) nas funções `pya.click()` do script email_automatico.py para corresponder à posição dos elementos na sua tela. Por
favor, note que este script foi configurado para funcionar em um ambiente específico e pode ser necessário ajustar as coordenadas dos cliques do mouse para que funcione corretamente em outros computadores.
2.  O programa realizará a mesma análise de investimento que foi feita em analise_de_investimento.py.
3.  Em seguida, solicitará que você insira seu nome.
4.  Depois, você precisará fornecer o endereço de email de destino.
5.  Veja a mágica acontecer 😉.

Notas
-----

*   Certifique-se de ter uma conexão de internet ativa para recuperar os dados da ação.
*   Os resultados podem variar dependendo da disponibilidade e precisão dos dados fornecidos pela API do Yahoo Finance.
