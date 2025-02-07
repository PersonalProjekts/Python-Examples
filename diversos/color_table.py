'''
    Este código gera uma tabela completa de combinações de cores e estilos ANSI que podem ser 
    usados em terminais que suportam escape sequences ANSI.

    Ele percorre todas as combinações possíveis de:
        - Cores de texto (30 a 37)
        - Cores de fundo (40 a 47)
        - Estilos de texto (normal, negrito, sublinhado, negrito e sublinhado)

    Para cada combinação, o código:
        1. Aplica a cor e o estilo a um texto de exemplo.
        2. Exibe o texto formatado no terminal.
        3. Mostra o código ANSI correspondente ao lado do texto formatado.

    O resultado é uma tabela visual que ajuda a entender como as cores e estilos ANSI funcionam 
    no terminal.
'''


# ----------------------------------------------------------------------
# Cores de texto (30-37) e fundo (40-47)
coresTexto = range(30, 38)
coresFundo = range(40, 48)


# ----------------------------------------------------------------------
# Estilos (negrito, sublinhado, etc.)
estilosTexto = {
    'normal'            : '',
    'negrito'           : ';1',
    'sublinhado'        : ';4',
    'negrito_sublinhado': ';1;4'
}


# ----------------------------------------------------------------------
# Exibir a tabela de cores
for estiloTexto, estiloCodigo in estilosTexto.items():
    print(f'\n--- Estilo: {estiloTexto} ---\n')
    for corTexto in coresTexto:
        for corFundo in coresFundo:
            # Código ANSI para a cor e estilo
            codigoCor = f'\033[{corTexto};{corFundo}{estiloCodigo}m'
            # Representação do código ANSI
            codigoRepr = f'\\033[{corTexto};{corFundo}{estiloCodigo}m'
            # Exibir a linha formatada
            print(f'{codigoCor}{'Texto Colorido'.ljust(20)}\033[0m  {codigoRepr}')
        print()