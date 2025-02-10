# Diretório de Exemplos em Python

Este diretório possui exemplos de códigos em Python para operações na rede.

Seguem as descrições de cada um dos exemplos disponibilizados:

---

<details>
  <summary><b>external_host_ip.py</b></summary>

  Este programa foi desenvolvido para obter informações básicas de rede, como o nome do host, o IP interno (local) e o IP externo da rede. Ele utiliza a biblioteca `socket` para obter o nome do host e o IP interno, e a biblioteca `requests` para consultar o IP externo por meio do serviço `checkip.amazonaws.com` da AWS.

  **Funcionalidades:**

  - ***Obtenção do nome do host***:
    - Retorna o nome do computador na rede local.

  - ***Obtenção do IP interno***:
    - Retorna o endereço IP local do computador na rede.

  - ***Obtenção do IP externo***:
    - Consulta o IP público da rede por meio do serviço `checkip.amazonaws.com`.

  - ***Tratamento de erros***:
    - Verifica se a requisição ao serviço de IP externo foi bem-sucedida e exibe uma mensagem de erro caso contrário.

  **Como funciona:**

  O programa utiliza a função `socket.gethostname()` para obter o nome do host e `socket.gethostbyname()` para obter o IP interno. Para o IP externo, ele faz uma requisição HTTP GET ao serviço `checkip.amazonaws.com` e trata possíveis erros de conexão ou falhas na requisição.

  **Serviço da AWS utilizado: `checkip.amazonaws.com`**

  O `checkip.amazonaws.com` é um serviço simples e gratuito fornecido pela **Amazon Web Services (AWS)** que retorna o endereço IP público da rede a partir da qual a requisição é feita. Ele é amplamente utilizado por desenvolvedores para obter o IP externo de forma rápida e confiável.

  - ***Como o serviço funciona:***
    Quando você faz uma requisição HTTP GET para `https://checkip.amazonaws.com`, o serviço retorna o IP público da sua rede em formato de texto puro. Por exemplo:
    ```bash
    $ curl https://checkip.amazonaws.com
    123.45.67.89
    ```

  - ***Por que a AWS oferece esse serviço?***
    A AWS disponibiliza o `checkip.amazonaws.com` como uma utilidade pública para desenvolvedores e usuários que precisam de uma maneira fácil de obter o IP externo de uma rede. Ele é frequentemente usado em scripts, automações ou para configurar regras de firewall dinâmicas, como em grupos de segurança da AWS.

  - ***Confiabilidade:***
    Como é um serviço da AWS, ele é altamente confiável e estável. No entanto, é sempre bom ter alternativas (como `ipify.org`, `ifconfig.me`, etc.) caso o serviço esteja temporariamente indisponível.

  **Dependências:**

  Para utilizar este programa, é necessário instalar a biblioteca `requests`. Isso pode ser feito utilizando o gerenciador de pacotes `pip` com o seguinte comando:

  ```bash
    pip install requests
  ```
  Para mais informações sobre a biblioteca `requests`, consulte a [documentação oficial](https://pypi.org/project/requests/).
</details>
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
  <summary><b>wlan_network_scanner.py</b></summary>

  Este programa foi desenvolvido para listar todas as redes Wi-Fi disponíveis ao redor do dispositivo e exibir informações detalhadas sobre cada uma delas, como tipo de rede, método de autenticação e tipo de criptografia. Ele é compatível com sistemas Windows e Linux, utilizando comandos específicos para cada plataforma.

  **Funcionalidades:**

  - ***Listagem de Redes Wi-Fi***:
    - Identifica todas as redes Wi-Fi disponíveis ao redor do dispositivo.
    - Extrai informações como SSID (nome da rede), tipo de rede, método de autenticação e tipo de criptografia.

  - ***Compatibilidade Multiplataforma***:
    - Funciona tanto no Windows quanto no Linux, adaptando-se automaticamente ao sistema operacional em execução.

  - ***Exibição de Informações***:
    - Exibe as informações das redes Wi-Fi de forma organizada em uma tabela no terminal.

  **Como funciona:**

  O programa detecta o sistema operacional em execução e utiliza comandos específicos para listar as redes Wi-Fi:
  - No **Windows**, o comando `netsh wlan show network` é utilizado.
  - No **Linux**, o comando `nmcli -t -f SSID,SECURITY dev wifi` é utilizado.

  As informações são processadas e organizadas em um dicionário, que é exibido em formato tabular no terminal.

  **Dependências:**

  - **Windows**: Não requer dependências adicionais, pois utiliza comandos nativos do sistema.
  - **Linux**: Requer o `nmcli` (parte do NetworkManager), que geralmente já está instalado na maioria das distribuições Linux. Caso não esteja, pode ser instalado com:
    ```bash
    sudo apt-get install network-manager  # Para distribuições baseadas em Debian/Ubuntu
    sudo yum install NetworkManager       # Para distribuições baseadas em RedHat/CentOS
    ```

  **Exemplo de Saída:**

  O programa exibe uma tabela no terminal com as seguintes colunas:

  - **SSID**: Nome da rede Wi-Fi.
  - **Tipo de Rede**: Tipo de rede (por exemplo, Infraestrutura).
  - **Autenticação**: Método de autenticação utilizado pela rede (por exemplo, WPA2).
  - **Criptografia**: Tipo de criptografia utilizado pela rede (por exemplo, AES).

  ```plaintext
  SSID                           | Tipo de Rede         | Autenticação         | Criptografia
  --------------------------------------------------------------------------------------------
  MinhaRedeWiFi                  | Infraestrutura       | WPA2                 | AES
  OutraRede                      | Infraestrutura       | WPA                  | TKIP
  ```
  </details>