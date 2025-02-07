'''
   O programa solicita ao usuário um número inteiro positivo, utiliza o Crivo de
   Eratóstenes para identificar todos os números primos até esse número e, finalmente, 
   exibe os números primos encontrados. 
   
   O algoritmo é eficiente para encontrar primos em um intervalo, especialmente para 
   valores de n não muito grandes.
'''

import sys

valor_n = int(input('Digite um número inteiro positivo: '))

if valor_n < 0:
    sys.exit('Por favor, insira um número inteiro positivo.')

# Cria uma lista de booleanos de tamanho n+1 (para representar números de 0 a n)
primos    = [True] * (valor_n + 1)
primos[0] = primos[1] = False  # 0 e 1 não são primos

# Crivo de Eratóstenes
for i in range(2, int(valor_n**0.5) + 1):
   if primos[i]:
      for j in range(i * i, valor_n + 1, i): primos[j] = False

# Exibe os números primos
print(f'Números primos até {valor_n}:')
for i in range(2, valor_n + 1):
   if primos[i]: print(i, end=' ')
