valor_decimal = int(input('Informe um valor decimal inteiro: '))

if valor_decimal >= 0:
    valor_binario = ''
    while valor_decimal > 0:
        valor_binario = str(valor_decimal % 2) + valor_binario
        valor_decimal = valor_decimal // 2
    
    if (valor_binario == ''): valor_binario = '0'
    print(valor_binario)
else:
    print('Informe um Valor >= 0 ...')