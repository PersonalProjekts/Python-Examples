import sys

# --------------------------------------------------------------------------------
# Função principal 
def main():
   try:
      intValor = int(input('\nDigite um número inteiro positivo: '))
   except ValueError:
      sys.exit('\nERRO: Informe um inteiro válido...')
   except:
      sys.exit(f'\nERRO: {sys.exc_info()[0]}')
   else:
      if intValor < 0:
         sys.exit('ERRO: Insira um número inteiro positivo.')

      # Cria uma lista de booleanos de tamanho n+1 (para representar números de 0 a n)
      primos    = [True] * (intValor + 1)
      primos[0] = primos[1] = False  # 0 e 1 não são primos

      # Crivo de Eratóstenes
      for i in range(2, int(intValor**0.5) + 1):
         if primos[i]:
            for j in range(i * i, intValor + 1, i):
               primos[j] = False

      # Exibe os números primos
      print(f'Números primos até {intValor}:')
      for i in range(2, intValor + 1):
         if primos[i]: print(i, end=' ')

# --------------------------------------------------------------------------------
# Chama a função principal
if __name__ == '__main__':
   main()