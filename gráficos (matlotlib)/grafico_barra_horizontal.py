'''
    Este exemplo demonstra a criação de um gráfico de barras verticais utilizando 
    a biblioteca MATPLOTLIB.

    Necessário instalar a biblioteca MATPLOTLIB
        pip install matplotlib

    Documentação
        https://matplotlib.org/
'''

import matplotlib.pyplot as pyplot

# Dados para o gráfico
REDUTOR = 1000000
DADOS   = { 'Regiões'    : ['N', 'NE', 'SE', 'S', 'CO'],
            'Populações' : [17834762/REDUTOR, 55389382/REDUTOR, 87348223/REDUTOR, 30685598/REDUTOR, 16492326/REDUTOR],
            'Rótulos'    : ['Norte', 'Nordeste', 'Sudeste', 'Sul', 'Centro-Oeste'],
            'Cores'      : ['red', 'blue', 'green', 'yellow', 'orange'] }

ROTULOS = tuple(DADOS.keys())

fig, graph = pyplot.subplots()

# Criando o gráfico (eixo x = Regiões, eixo y = Populações)
bars = graph.barh(DADOS['Regiões'], DADOS['Populações'], color=DADOS['Cores'], label=DADOS['Rótulos'])

# Adicionando os rótulos nas barras
for bar, rotulo in zip(bars, DADOS['Populações']):
    width = bar.get_width()
    valor = '{:,.0f}'.format(rotulo * REDUTOR).replace(',','.')
    graph.text(width + 1, bar.get_y() + bar.get_height() / 2, valor, ha='left', va='center', fontsize=9, fontweight='bold')

# Definindo o valores mínimo e máximo do eixo Y
eixos = pyplot.gca()
maior_populacao = max([valor for valor in DADOS["Populações"]])
eixos.set_xlim([0, maior_populacao+30])

# Definindo os rótulos dos eixos X e Y
graph.set_xlabel(ROTULOS[0])
graph.set_ylabel(ROTULOS[1] + '/' + str(REDUTOR))

# Definindo o título do gráfico
graph.set_title('Prévia População 2022')

# Exibindo a legenda do gráfico
graph.legend(title='Regiões BR')

# Exibindo o gráfico
pyplot.show()