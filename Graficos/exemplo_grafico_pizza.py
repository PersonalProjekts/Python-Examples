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

rotulos     = ('Aprovados', 'Trancados', 'Evadidos', 'Reprovados')
percentuais = [45, 30, 15, 30]

#pyplot.pie(percentuais, labels=rotulos)

pyplot.pie(percentuais, labels=rotulos, autopct='%1.2f%%')

#pyplot.pie(percentuais, labels=rotulos, autopct='%1.2f%%', counterclock=False)

#pyplot.pie(percentuais, labels=rotulos, autopct='%1.f%%', counterclock=False, startangle=90)

# Título do Gráfico
pyplot.title('Exemplo #01 - Gráfico de Pizza')

# Legenda do Gráfico
#pyplot.legend()

# Exibindo o gráfico
pyplot.show()