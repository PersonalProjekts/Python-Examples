# --------------------------------------------------------------------------------
# Função principal 
def main():
   print(f'{'Caractere':<10} {'Decimal':<10} {'Hexa':<10} {'Binário':<10}')
   print('-' * 40)

   for i in range(256):
      caractere = chr(i) if chr(i).isprintable() else 'n/d'
      decimal   = i
      hexa      = hex(i)
      binario   = bin(i)[2:].zfill(8)
      print(f'{caractere:<10} {decimal:<10} {hexa:<10} 0b{binario}')

# --------------------------------------------------------------------------------
# Chama a função principal
if __name__ == '__main__':
   main()