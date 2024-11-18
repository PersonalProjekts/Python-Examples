'''
   Este exemplo demonstra a criação de um gráfico de pizza utilizando a biblioteca
   MATPLOTLIB.

   Necessário instalar a biblioteca MATPLOTLIB
      pip install matplotlib

   Documentação
      https://matplotlib.org/
'''

import matplotlib.pyplot as pyplot

# ------------------------------------------------------------------------------------------
# Dados para o gráfico
dados = { 'Regiões': ['Norte', 'Nordeste', 'Sudeste', 'Sul', 'Centro-Oeste'],
          'Populações' : [17834762, 55389382, 87348223, 30685598, 16492326] }

rotulos = list(dados.keys())

# ------------------------------------------------------------------------------------------
# Criando o gráfico
pyplot.pie(dados['Populações'], labels=dados['Regiões'], autopct='%1.2f%%')

# ------------------------------------------------------------------------------------------
# Título do Gráfico
pyplot.title('Prévia População 2022')

# ------------------------------------------------------------------------------------------
# Exibindo o gráfico
pyplot.show()