# --------------------------------------------------------------------------------
# Função principal 
def main():
    # Cores de texto (30-37) e fundo (40-47)
    coresTexto = range(30, 38)
    coresFundo = range(40, 48)

    # Estilos (negrito, sublinhado, etc.)
    estilosTexto = {
        'normal': '',
        'negrito': ';1',
        'sublinhado': ';4',
        'negrito_sublinhado': ';1;4'
    }

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
                print(f'{codigoCor}{"Texto Colorido".ljust(20)}\033[0m  {codigoRepr}')
            print()

# --------------------------------------------------------------------------------
# Chama a função principal
if __name__ == "__main__":
    main()