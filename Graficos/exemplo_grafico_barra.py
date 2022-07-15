# --------------------------------------------------------------------------------
# Documentação:
#       https://matplotlib.org/
#
# Atualizando o PIP
#       python -m pip install --upgrade --user pip
#
# Instalando o MATPLOTLIB
#       pip install matplotlib
# --------------------------------------------------------------------------------

import matplotlib.pyplot as pyplot

modalidade = ['Técnico Integrado', 'Subsequente', 'Tecnologo', 'Licenciatura', 'Engenharia']
qt_alunos  = [5459, 865, 2365, 1169, 421]

# Criando o gráfico (eixo x = modalidades, eixo y = quantidade de alunos)
pyplot.bar(modalidade, qt_alunos, color="red")

# Definindo as legendas para cada barra do eixo X
pyplot.xticks(modalidade)

# Rótulo do eixo Y
pyplot.ylabel('Qt Alunos')

# Rótulo do eixo X
pyplot.xlabel('Modalidades')

# Título do Gráfico
pyplot.title('Exemplo #02 - Gráfico de Barras')

# Exibindo o gráfico
pyplot.show()