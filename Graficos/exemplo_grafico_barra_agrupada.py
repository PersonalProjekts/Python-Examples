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

# Listas com os nomes das diretorias
diretorias = ['DIATINF', 'DIAREN', 'DIACON', 'DIACIN']

# Listas com os valores (DIATINF, DIAREN, DIACON, DIACIN)
alunos_integrado   = [150, 300, 125, 237]
alunos_subsequente = [78, 61, 79, 63]
alunos_tecnologo   = [196, 154, 137, 121]
alunos_engenharia  = [0, 0, 0, 129]

# Definindo a largura da barra
largura_barra = 0.25

# Definindo a posição de cada barra. A posição de cada barra é definida com base na largura da barra anterior
barra_1 = [x for x in range(len(diretorias))]
barra_2 = [x + largura_barra for x in barra_1]
barra_3 = [x + largura_barra for x in barra_2]
barra_4 = [x + largura_barra for x in barra_3]

# Criando as barras
pyplot.bar(barra_1, alunos_integrado  , color='#7FFFD4', width=largura_barra, label='Integrado')
pyplot.bar(barra_2, alunos_subsequente, color='#DAA520', width=largura_barra, label='Subsequente')
pyplot.bar(barra_3, alunos_tecnologo  , color='#FF00FF', width=largura_barra, label='Tecnologo')
pyplot.bar(barra_4, alunos_engenharia , color='#B0E0E6', width=largura_barra, label='Engenharia')

# Definindo as legendas para cada barra do eixo X
pyplot.xticks([r + largura_barra for r in range(len(alunos_integrado))], diretorias)

# Rótulo do eixo X
pyplot.xlabel('Modalidades')

# Rótulo do eixo Y
pyplot.ylabel('Qt. Alunos')

# Título do Gráfico
pyplot.title('Exemplo #04 - Gráfico de Barras Agrupadas')

# Criando a Legendas
pyplot.legend()

# Exibindo o gráfico
pyplot.show()