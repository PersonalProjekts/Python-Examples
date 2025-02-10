# Diretório de Exemplos em Python

Este diretório possui exemplos de códigos em Python para operações na rede.

Seguem as descrições de cada um dos exemplos disponibilizados:

---

<details>
  <summary><b>network_info.py</b></summary>

  Este programa foi desenvolvido para obter informações de rede (como IP, máscara de sub-rede, gateway e servidor DHCP) e listar todos os IPs válidos na rede local. Ele é compatível com sistemas Windows, Linux e macOS.

  **Funcionalidades:**

  - ***Obtenção de informações de rede***:
    - IP local.
    - Máscara de sub-rede.
    - Gateway padrão.
    - Servidor DHCP.
    - Conversão da máscara de sub-rede para formato CIDR.

  - ***Listagem de IPs válidos***:
    - Gera uma lista de todos os IPs válidos na rede local com base no IP e na máscara de sub-rede.


  **Como funciona:**

  O programa utiliza comandos do sistema operacional (`ipconfig` no Windows e `ifconfig` no Linux/macOS) para obter as informações de rede. Em seguida, ele converte a máscara de sub-rede para o formato CIDR e calcula todos os IPs válidos na rede.
</details>

---

<details>
  <summary><b>color_table.py</b></summary>

  Este código gera uma tabela completa de combinações de cores e estilos ANSI que podem ser usados em terminais que suportam escape sequences ANSI.

  Ele percorre todas as combinações possíveis de:

  - Cores de texto: 30 a 37;
  - Cores de fundo: 40 a 47;
  - Estilos de texto (normal, negrito, sublinhado, negrito e sublinhado).

  Para cada combinação, o código:

  1. Aplica a cor e o estilo a um texto de exemplo;
  2. Exibe o texto formatado no terminal;
  3. Mostra o código ANSI correspondente ao lado do texto formatado.

  O resultado é uma tabela visual que ajuda a entender como as cores e estilos ANSI funcionam no terminal.
</details>

---

<details>
  <summary><b>sieve_of_eratosthenes.py</b></summary>

  Este código implementa o Crivo de Eratóstenes, um algoritmo clássico para encontrar todos os números primos até um determinado número `n`. Abaixo está uma explicação detalhada do que cada parte do código faz:

  - **Entrada do Usuário:**
    - O código solicita ao usuário que insira um número inteiro positivo (`valor_n`). Esse número define o limite superior até o qual os números primos serão buscados.

  - **Validação da Entrada:**
    - Se o usuário inserir um número negativo, o programa exibe uma mensagem de erro e termina a execução usando `sys.exit()`. Isso garante que apenas números positivos sejam processados.

  - **Inicialização da Lista de Booleanos:**
    - Uma lista chamada `primos` é criada com tamanho `valor_n + 1`. Essa lista é inicializada com `True`, indicando que, inicialmente, todos os números de 0 a `n` são considerados primos.
    - Os valores `primos[0]` e `primos[1]` são definidos como `False`, pois 0 e 1 não são números primos.

  - **Crivo de Eratóstenes:**
    - O algoritmo começa a iterar a partir do número 2 (o menor número primo) até a raiz quadrada de `valor_n`. A raiz quadrada é usada como limite porque, se um número `n` não for primo, ele deve ter pelo menos um fator menor ou igual à sua raiz quadrada.
    - Para cada número `i` que ainda está marcado como primo (`primos[i] == True`), o algoritmo marca todos os múltiplos de `i` como não primos (`primos[j] = False`), começando de `i * i` e indo até `valor_n` com incrementos de `i`.

  - **Exibição dos Números Primos:**
    - Após a execução do Crivo de Eratóstenes, o código percorre a lista `primos` de 2 até `valor_n` e imprime os números que ainda estão marcados como primos (`primos[i] == True`).
</details>

