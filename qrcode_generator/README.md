# Diretório de Exemplos em Python

Este diretório possui exemplos de códigos em Python para geração de QrCodes.

Seguem as descrições de cada um dos exemplos disponibilizados:

---

<details>
  <summary><b>qr_code_generator.py</b></summary>

  Este programa foi desenvolvido para gerar QR Codes a partir de uma entrada de texto fornecida pelo usuário. Ele utiliza a biblioteca `qrcode` para criar e salvar o QR Code em um arquivo de imagem no formato PNG.

  **Funcionalidades:**

  - ***Geração de QR Code***:
    - Cria um QR Code a partir de um texto fornecido pelo usuário.
    - Permite personalizar o tamanho do QR Code, o tamanho de cada "box" (pixel), a espessura da borda, a cor de fundo e a cor do QR Code.

  - ***Salvamento do QR Code***:
    - Salva o QR Code gerado em um arquivo de imagem no formato PNG no diretório onde o script está localizado.

  **Como funciona:**

  O programa solicita ao usuário que insira o texto que deseja codificar no QR Code. Em seguida, ele utiliza a biblioteca `qrcode` para gerar o QR Code com base nas configurações definidas (versão, tamanho do box, borda, cores, etc.). Por fim, o QR Code é salvo como um arquivo PNG no diretório do script.

  **Personalização:**

  O programa permite personalizar várias propriedades do QR Code, como:

  - `VERSAO`: Controla o tamanho do QR Code (valores de 1 a 40).
  - `BOX_SIZE`: Define o tamanho de cada "box" (pixel) do QR Code.
  - `BORDER`: Define a espessura da borda ao redor do QR Code.
  - `BACK_COLOR`: Define a cor de fundo do QR Code (em formato RGB).
  - `FILL_COLOR`: Define a cor do QR Code (em formato RGB).

  **Dependências:**

  Para utilizar este programa, é necessário instalar a biblioteca `qrcode`. Isso pode ser feito utilizando o gerenciador de pacotes `pip` com o seguinte comando:

  ```bash```
  ```pip install qrcode```
  
  Para mais informações sobre a biblioteca `qrcode`, consulte a [documentação oficial](https://pypi.org/project/qrcode/).
</details>

---

<details>
  <summary><b>qr_code_generator.py</b></summary>

  Este programa foi desenvolvido para gerar QR Codes a partir de uma entrada de texto fornecida pelo usuário. Ele utiliza a biblioteca `PyQRCode` para criar e salvar o QR Code em arquivos de imagem nos formatos SVG e PNG.

  **Funcionalidades:**

  - ***Geração de QR Code***:
    - Cria um QR Code a partir de um texto fornecido pelo usuário.
    - Permite personalizar a escala do QR Code ao salvar nos formatos SVG e PNG.

  - ***Salvamento do QR Code***:
    - Salva o QR Code gerado em arquivos de imagem nos formatos SVG e PNG no diretório onde o script está localizado.

  **Como funciona:**

  O programa solicita ao usuário que insira o texto que deseja codificar no QR Code. Em seguida, ele utiliza a biblioteca `PyQRCode` para gerar o QR Code com base no texto fornecido. Por fim, o QR Code é salvo como arquivos SVG e PNG no diretório do script.

  **Dependências:**

  Para utilizar este programa, é necessário instalar a biblioteca `PyQRCode`. Isso pode ser feito utilizando o gerenciador de pacotes `pip` com o seguinte comando:

```bash
    pip install qrcode

  Para mais informações sobre a biblioteca `PyQRCode`, consulte a [documentação oficial](https://pypi.org/project/PyQRCode/).
  </details>