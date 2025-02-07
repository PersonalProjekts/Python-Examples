# Diretório de Exemplos em Python

Este diretório possui exemplos diversos de códigos em Python.

Seguem as descrições de cada um dos exemplos disponibilizados:

---

<details>
  <summary><b>ascii_table.py</b></summary>

  Este programa imprime a tabela ASCII estendida, que inclui todos os 256 caracteres (valores de 0 a 255).

  Para cada caractere, são exibidas as seguintes informações:

  1. **Caractere**: O símbolo ou caractere correspondente ao valor ASCII, sempre ocupando 10 posições (preenchido com espaços à esquerda) - Se o caractere for não imprimível, ele será substituído por 'n/d';
  2. **Decimal**: O valor numérico em base decimal;
  3. **Hexadecimal**: O valor numérico em base hexadecimal, formatado com o prefixo '0x';
  4. **Binário**: O valor numérico em base binária, formatado com o prefixo '0b' e sempre com 8 dígitos (preenchido com zeros à esquerda, se necessário).

  **Funcionamento:**

  - A função `chr(i)` converte o valor inteiro `i` para o caractere correspondente;
  - O método `isprintable()` verifica se o caractere é imprimível. Caso contrário, ele é substituído por 'n/d';
  - A função `hex(i)` converte o valor inteiro `i` para uma string hexadecimal;
  - A função `bin(i)[2:].zfill(8)` converte o valor inteiro `i` para uma string binária, remove o prefixo '0b' e garante que o resultado tenha 8 dígitos;
  - A formatação com `f-strings` é usada para alinhar as colunas e garantir uma saída legível.

  **Observações:**

  - Os primeiros 32 caracteres (0 a 31) são caracteres de controle não imprimíveis e serão substituídos por 'n/d';
  - Os caracteres de 128 a 255 fazem parte da tabela ASCII estendida, que inclui caracteres especiais, como letras acentuadas e símbolos;
  - Se o terminal não suportar a exibição de caracteres não-ASCII, alguns caracteres podem não ser exibidos corretamente.
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