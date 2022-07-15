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
pyplot.barh(modalidade, qt_alunos, color="red")

# Rótulo do eixo Y
pyplot.ylabel('Modalidades')

# Rótulo do eixo X
pyplot.xlabel('Qt Alunos')

# Título do Gráfico
pyplot.title('Exemplo #03 - Gráfico de Barras Horizontal')

# Exibindo o gráfico
pyplot.show()