'''
    Este exemplo demonstra a criação de um gráfico de pizza utilizando a biblioteca]
    MATPLOTLIB.

    Necessário instalar a biblioteca MATPLOTLIB
        pip install matplotlib

    Documentação
        https://matplotlib.org/
'''

import matplotlib.pyplot as pyplot

# ------------------------------------------------------------------------------------------
# Dados para o gráfico
DADOS   = { 'Regiões'    : ['N', 'NE', 'SE', 'S', 'CO'],
            'Populações' : [17834762, 55389382, 87348223, 30685598, 16492326],
            'Rótulos'    : ['Norte', 'Nordeste', 'Sudeste', 'Sul', 'Centro-Oeste'],
            'Cores'      : ['red', 'blue', 'green', 'yellow', 'orange'] }

ROTULOS = tuple(DADOS.keys())

fig, (graph, table_ax) = pyplot.subplots(1, 2, figsize=(12, 6), gridspec_kw={'width_ratios': [2, 1]})

# ------------------------------------------------------------------------------------------
# Criando o gráfico
fatias, _, text_pct = graph.pie(DADOS['Populações'], labels=[''] * len(DADOS['Regiões']), autopct='%1.2f%%')

# ------------------------------------------------------------------------------------------
# Definindo a cor dos rótulos das fatias
for text in text_pct:
    text.set_color('White')

# ------------------------------------------------------------------------------------------
# Criando a tabela manualmente
table_data = [DADOS['Regiões'], DADOS['Populações']]
table_rows = len(DADOS['Rótulos'])
table_cols = len(DADOS['Regiões'])
table_ax.axis('off')
table_ax.table(cellText=table_data, rowLabels=['Regiões', 'Populações'], loc='center',
               cellLoc='center', colWidths=[0.2] * table_cols, colLabels=DADOS['Rótulos'], 
               fontsize=14)

# ------------------------------------------------------------------------------------------
# Ajustando o layout para evitar sobreposições
pyplot.subplots_adjust(wspace=0.2)

# ------------------------------------------------------------------------------------------
# Definindo o título do gráfico
graph.set_title('Prévia População 2022')

# ------------------------------------------------------------------------------------------
# Exibindo a legenda do gráfico
graph.legend(fatias, DADOS['Rótulos'], title='Regiões BR', loc='upper right', bbox_to_anchor=(1.50, 1))

# ------------------------------------------------------------------------------------------
# Exibindo o gráfico
pyplot.show()