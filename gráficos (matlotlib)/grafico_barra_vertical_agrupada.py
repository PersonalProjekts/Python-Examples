'''
   Este exemplo demonstra a criação de um gráfico de barras verticais agrupadas 
   utilizando a biblioteca MATPLOTLIB.

   Necessário instalar a biblioteca MATPLOTLIB
      pip install matplotlib

   Documentação
      https://matplotlib.org/
'''

import matplotlib.pyplot as pyplot

# Dados para o gráfico
REDUTOR = 1000000
DADOS   = { 'Regiões'    : ['N', 'NE', 'SE', 'S', 'CO'],
            'Populações (1990)' : [10257266/REDUTOR, 42470225/REDUTOR, 72297351/REDUTOR, 25089783/REDUTOR, 11616745/REDUTOR],
            'Populações (2000)' : [12893561/REDUTOR, 47693253/REDUTOR, 72297351/REDUTOR, 25089783/REDUTOR, 11616745/REDUTOR],
            'Populações (2022)' : [17834762/REDUTOR, 55389382/REDUTOR, 87348223/REDUTOR, 30685598/REDUTOR, 16492326/REDUTOR],
            'Rótulos'    : ['Norte', 'Nordeste', 'Sudeste', 'Sul', 'Centro-Oeste'],
            'Cores'      : ['red', 'blue', 'green', 'yellow', 'orange'] }

ROTULOS = tuple(DADOS.keys())

# Definindo a largura da barra
BAR_WIDTH = 0.25

fig, graph = pyplot.subplots()

# Definindo a posição de cada barra. A posição de cada barra é definida com base na largura da barra anterior
barra_1 = [x for x in range(len(DADOS['Regiões']))]
barra_2 = [x + BAR_WIDTH for x in barra_1]
barra_3 = [x + BAR_WIDTH for x in barra_2]

# Criando as barras
graph.bar(barra_1, DADOS['Populações (1990)'], color='Blue'  , width=BAR_WIDTH, label='Ano 1990')
graph.bar(barra_2, DADOS['Populações (2000)'], color='Yellow', width=BAR_WIDTH, label='Ano 2000')
graph.bar(barra_3, DADOS['Populações (2022)'], color='Green'   , width=BAR_WIDTH, label='Ano 2022')

# Definindo as legendas para cada barra do eixo X
pyplot.xticks([r + BAR_WIDTH for r in range(len(DADOS['Regiões']))], DADOS['Regiões'])

# Definindo os rótulos dos eixos X e Y
graph.set_xlabel(ROTULOS[0])
graph.set_ylabel('Populações/' + str(REDUTOR))

# Título do Gráfico
graph.set_title('População Brasil')

# Exibindo a legenda do gráfico
graph.legend(title='Regiões BR')

# Exibindo o gráfico
pyplot.show()