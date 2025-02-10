import sys

# --------------------------------------------------------------------------------
# Função principal 
def main():
    valor_n = int(input('Digite um número inteiro positivo: '))

    if valor_n < 0:
        sys.exit('Por favor, insira um número inteiro positivo.')

    # Cria uma lista de booleanos de tamanho n+1 (para representar números de 0 a n)
    primos    = [True] * (valor_n + 1)
    primos[0] = primos[1] = False  # 0 e 1 não são primos

    # Crivo de Eratóstenes
    for i in range(2, int(valor_n**0.5) + 1):
        if primos[i]:
            for j in range(i * i, valor_n + 1, i):
                primos[j] = False

    # Exibe os números primos
    print(f'Números primos até {valor_n}:')
    for i in range(2, valor_n + 1):
        if primos[i]:
            print(i, end=' ')

# --------------------------------------------------------------------------------
# Chama a função principal
if __name__ == "__main__":
    main()