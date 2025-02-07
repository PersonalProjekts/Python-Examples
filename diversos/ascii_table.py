'''
   Programa para imprimir a tabela ASCII estendida (0 a 255) com valores decimais, hexadecimais 
   e binários de 8 dígitos.
'''

print(f'{'Caractere':<10} {'Decimal':<10} {'Hexa':<10} {'Binário':<10}')
print('-' * 40)

for i in range(256):
   caractere = chr(i) if chr(i).isprintable() else 'n/d'   
   decimal   = i
   hexa      = hex(i)
   binario   = bin(i)[2:].zfill(8)
   # Exibe os valores
   print(f'{caractere:<10} {decimal:<10} {hexa:<10} 0b{binario}')

