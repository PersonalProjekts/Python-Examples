<p>Este diretório possui exemplos diversos de códigos em Python.</p>

<p>Seguem as descrições de cada um dos exemplos disponibilizados:</p>

<!-- --------------------------------------------------------------------------------------------- -->
<hr/>
<details>
  <summary>color_table.py</summary>
  <p>&nbsp;</p>
  <p>Este código gera uma tabela completa de combinações de cores e estilos ANSI que podem ser usados em terminais que suportam escape sequences ANSI.</p>

  <p>Ele percorre todas as combinações possíveis de:</p>
  <ul>
    <li>Cores de texto: 30 a 37;</li>
    <li>Cores de fundo: 40 a 47;</li>
    <li>Estilos de texto (normal, negrito, sublinhado, negrito e sublinhado).</li>
  </ul>

  <p>Para cada combinação, o código:</p>
  <ol>
    <li>Aplica a cor e o estilo a um texto de exemplo.</li>
    <li>Exibe o texto formatado no terminal.</li>
    <li>Mostra o código ANSI correspondente ao lado do texto formatado.</li>
  </ol>

  <p>O resultado é uma tabela visual que ajuda a entender como as cores e estilos ANSI funcionam 
  no terminal.</p>
</details>


<!-- --------------------------------------------------------------------------------------------- -->
<hr/>
<details>
  <summary>crivo_eratostenes.py</summary>
  <p>&nbsp;</p>
  <p>Este código implementa o Crivo de Eratóstenes, um algoritmo clássico para encontrar todos os números primos até um determinado número n. Abaixo está uma explicação detalhada do que cada parte do código faz:</p>

  <ul>
    <li>Entrada do Usuário:</li>
    <p>O código solicita ao usuário que insira um número inteiro positivo (valor_n). Esse número define o limite superior até o qual os números primos serão buscados.</p>
    <li>Validação da Entrada:</li>
    <p>Se o usuário inserir um número negativo, o programa exibe uma mensagem de erro e termina a execução usando sys.exit(). Isso garante que apenas números positivos sejam processados.</p>
    <li>Inicialização da Lista de Booleanos:</li>
    <p>Uma lista chamada primos é criada com tamanho valor_n + 1. Essa lista é inicializada com True, indicando que, inicialmente, todos os números de 0 a n são considerados primos.</p>
    <p>Os valores primos[0] e primos[1] são definidos como False, pois 0 e 1 não são números primos.</p>
    <li>Crivo de Eratóstenes:</li>
    <p>O algoritmo começa a iterar a partir do número 2 (o menor número primo) até a raiz quadrada de valor_n. A raiz quadrada é usada como limite porque, se um número n não for primo, ele deve ter pelo menos um fator menor ou igual à sua raiz quadrada.</p>
    <p>Para cada número i que ainda está marcado como primo (primos[i] == True), o algoritmo marca todos os múltiplos de i como não primos (primos[j] = False), começando de i * i e indo até valor_n com incrementos de i.</p>
    <li>Exibição dos Números Primos:</li>
    <p>Após a execução do Crivo de Eratóstenes, o código percorre a lista primos de 2 até valor_n e imprime os números que ainda estão marcados como primos (primos[i] == True).</p>
  </ul>
</details>

