'''
    Este exemplo lista a tabela de cores de fonte/bacground disponíveis.
'''

print('-'*128)

for texto in range(8):
    for negrito in ['', ';1']:
        for fundo in range(8):
            str_cor   = f'\033[4{fundo};3{texto}{negrito}'
            str_cor_2 = f'\\033[4{fundo};3{texto}{negrito}m'
            str_saida = f'\033[{str_cor}m {str_cor_2.ljust(15)}'
            print(str_saida, end='')
        print('\033[0m')

print('-'*128)
