import re
import requests
import locale

locale.setlocale(locale.LC_ALL, 'pt-BR.UTF-8')

def pegaSelic():
    selic = requests.get('https://www.gov.br/receitafederal/pt-br/assuntos/orientacao-tributaria/pagamentos-e-parcelamentos/taxa-de-juros-selic')
    selic = selic.text
    regex = r"<td align=\"CENTER\"><b>2020<\/b><\/td>[\w\W]{0,3314}([\d\,\%]{0,6})%"

    match = re.findall(regex, selic)
    match = match[0]
    matchReplace = match.replace(',', '.')
    matchFloat = float(matchReplace)
    matchFloat /= 100

    return matchFloat

def calcularPoupança(ano, investimentoInicial, investimentoMensal):

    saldo = investimentoInicial
    ano *= 12
    count = 0
    selic = pegaSelic()
    
    while count <= ano:
        
        saldo = (saldo + investimentoMensal) + saldo * selic
        count += 1

    print(f'\n[+] - Investimento Inicial: R${locale.currency(investimentoInicial, grouping=True, symbol=None)}')
    print(f'[+] - Investimento Mensal: R${locale.currency(investimentoMensal, grouping=True, symbol=None)}')
    print(f'[+] - Mêses: {ano}')
    print(f'[+] - Renda Final: R${locale.currency(saldo, grouping=True, symbol=None)}')
    print(f'[+] - Renda Fixa: R${locale.currency(saldo * selic, grouping=True, symbol=None)}\n')

calcularPoupança(5, 0, 1000)