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
