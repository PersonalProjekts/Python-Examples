# Diretório de Exemplos em Python

Este diretório possui exemplos de códigos em Python para geração de QrCodes.

Seguem as descrições de cada um dos exemplos disponibilizados:

---

<details>
  <summary><b>qrcode_example.py</b></summary>

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

  ```bash
  pip install qrcode
  ```
  
  Para mais informações sobre a biblioteca `qrcode`, consulte a [documentação oficial](https://pypi.org/project/qrcode/).
</details>

---

<details>
  <summary><b>pyqrcode_example.py</b></summary>

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
    pip install pyqrcode
  ```

  Para mais informações sobre a biblioteca `PyQRCode`, consulte a [documentação oficial](https://pypi.org/project/PyQRCode/).
  </details>

  ---

<details>
  <summary><b>pyqrcode_example_wifi.py</b></summary>

  Este programa foi desenvolvido para gerar um QR Code contendo as credenciais de uma rede Wi-Fi, permitindo que dispositivos móveis se conectem facilmente à rede ao escanear o código. Ele utiliza a biblioteca `PyQRCode` para criar e salvar o QR Code em um arquivo de imagem no formato PNG.

  **Funcionalidades:**

  - ***Geração de QR Code para Wi-Fi***:
    - Cria um QR Code com as credenciais da rede Wi-Fi, incluindo SSID, senha e tipo de segurança.
    - O formato do QR Code segue o padrão `WIFI:T:<Tipo de Segurança>;S:<SSID>;P:<Senha>;;`.

  - ***Salvamento do QR Code***:
    - Salva o QR Code gerado em um arquivo de imagem no formato PNG no diretório onde o script está localizado.

  **Como funciona:**

  O programa define as credenciais da rede Wi-Fi (SSID, senha e tipo de segurança) e gera uma string no formato adequado para a criação do QR Code. Em seguida, ele utiliza a biblioteca `PyQRCode` para criar o QR Code com base nessa string. Por fim, o QR Code é salvo como um arquivo PNG no diretório do script.

  **Explicando as variáveis:**

  - ***WIFI_SSID***
    - Descrição: Esta variável armazena o nome da rede Wi-Fi (SSID - Service Set Identifier).
    - Tipo: String.
    - Exemplo: 
       ```python
       WIFI_SSID = 'MinhaRedeWiFi'
       ```

  - ***WIFI_PWD***
    - Descrição: Esta variável armazena a senha da rede Wi-Fi.
    - Tipo: String.
    - Exemplo:
      ```python
      WIFI_PWD = 'SenhaSegura123'
      ```  

  - ***WIFI_SEC***
    - Descrição: Esta variável define o tipo de segurança da rede Wi-Fi. Ela é uma lista que contém os possíveis tipos de segurança suportados.
    - Tipo: Lista de strings.
    - Valores possíveis:
      - `'WPA'`: Wi-Fi Protected Access (recomendado para redes modernas).
      - `'WEP'`: Wired Equivalent Privacy (menos seguro, utilizado em redes antigas).
      - `'nopass'`: Rede aberta, sem senha.
      - `'WEP40'`: Uma variante do WEP com chave de 40 bits.
      - Exemplo:
        ```python
        WIFI_SEC = ['WPA', 'WEP', 'nopass', 'WEP40']
        ```

  **Dependências:**

  Para utilizar este programa, é necessário instalar a biblioteca `PyQRCode`. Isso pode ser feito utilizando o gerenciador de pacotes `pip` com o seguinte comando:

  ```bash
    pip install pyqrcode
  ```
  Para mais informações sobre a biblioteca `PyQRCode`, consulte a [documentação oficial](https://pypi.org/project/PyQRCode/).
  </details>