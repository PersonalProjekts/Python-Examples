import subprocess, platform, re, sys, ipaddress

# --------------------------------------------------------------------------------
# Converte a máscara de sub-rede em formato CIDR
def ip2CIDR(mascara: str) -> int:
    # Converte a máscara de sub-rede em formato CIDR
    mask_parts = mascara.split(".")
    mask_bin   = ''.join([bin(int(part))[2:].zfill(8) for part in mask_parts])
    cidr       = mask_bin.count('1')

    return cidr

# --------------------------------------------------------------------------------
# Obtém as informações de IP no Windows
def getWindowsIPInfo() -> dict:
   # Inicializa o dicionário para armazenar as informações
   dictResultado = dict()

   # Obter informações de IP no Windows
   strResultado = subprocess.check_output('ipconfig /all', stderr=subprocess.PIPE)

   # Tentar decodificar com cp850 (codificação do terminal no Windows)
   try:
      strResultado = strResultado.decode('cp850', errors='replace')
   except UnicodeDecodeError:
      strResultado = strResultado.decode('utf-8', errors='replace')

   # Regex para capturar as informações
   ip_regex      = r'Endereço IPv4.*: (\d+\.\d+\.\d+\.\d+)'
   mask_regex    = r'Máscara de Sub-rede.*: (\d+\.\d+\.\d+\.\d+)'
   gateway_regex = r'Gateway Padrão.*: (\d+\.\d+\.\d+\.\d+)'
   dhcp_regex    = r'Servidor DHCP.*: (\d+\.\d+\.\d+\.\d+)'
      
   # Encontrar os valores correspondentes
   ip_match      = re.search(ip_regex, strResultado)
   mask_match    = re.search(mask_regex, strResultado)
   gateway_match = re.search(gateway_regex, strResultado)
   dhcp_match    = re.search(dhcp_regex, strResultado)

   # Adiciona as informações ao dicionário
   dictResultado['IP']            = ip_match.group(1)                 if ip_match                 else None
   dictResultado['Máscara']       = mask_match.group(1)               if mask_match               else None
   dictResultado['CIDR']          = ip2CIDR(dictResultado['Máscara']) if dictResultado['Máscara'] else None 
   dictResultado['Gateway']       = gateway_match.group(1)            if gateway_match            else None
   dictResultado['Servidor DHCP'] = dhcp_match.group(1)               if dhcp_match               else None

   return dictResultado
   
# --------------------------------------------------------------------------------
# Obtém as informações de IP no Linux/macOS
def getLinuxIPInfo() -> dict:
   # Inicializa o dicionário para armazenar as informações
   dictResultado = dict()

   # Comando para obter configurações de rede no Linux/macOS
   strResultado = subprocess.check_output('ifconfig', stderr=subprocess.PIPE)

   # Ignorar erros de codificação
   strResultado = strResultado.decode('utf-8', errors='ignore')  

   # Regex para capturar as informações
   ip_regex      = r'inet (\d+\.\d+\.\d+\.\d+)'
   mask_regex    = r'inet \d+\.\d+\.\d+\.\d+/(\d+)'
   gateway_regex = r'default via (\d+\.\d+\.\d+\.\d+)'
        
   # Encontrar os valores correspondentes
   ip_match = re.search(ip_regex, strResultado)
   mask_match = re.search(mask_regex, strResultado)
   gateway_match = re.search(gateway_regex, strResultado)

   # Adiciona as informações ao dicionário
   dictResultado['IP']      = ip_match.group(1)         if ip_match                 else None
   dictResultado['Máscara'] = mask_match.group(1)       if mask_match               else None
   dictResultado['CIDR']    = dictResultado['Máscara']  if dictResultado['Máscara'] else None
   dictResultado['Gateway'] = gateway_match.group(1)    if gateway_match            else None

   # Para encontrar o servidor DHCP, pode ser necessário usar o comando 'nmcli' ou outra ferramenta
   strResultadoDHCP = subprocess.run(['nmcli', '-t', '-f', 'IP4.DHCP4.SERVER', 'device', 'show'], stdout=subprocess.PIPE, text=True)
   strResultadoDHCP = strResultadoDHCP.stdout.strip()
   dictResultado['Servidor DHCP'] = strResultadoDHCP if strResultadoDHCP else None

   return dictResultado

# --------------------------------------------------------------------------------
# Obtém as informações de rede
def getNetworkInfo() -> dict:
   # Obtém o nome do sistema operacional
   strSistemaOperacional = platform.system().lower()

   # Inicializa o dicionário para armazenar as informações
   dictNetworkInfo = dict()

   try:
      if strSistemaOperacional == 'windows':
         dictNetworkInfo = getWindowsIPInfo()
      elif strSistemaOperacional in ['linux','darwin']:
         dictNetworkInfo = getLinuxIPInfo()
   except:
      print(f'\nERRO: Erro ao obter as informações: {sys.exc_info()[0]}\n')
      dictNetworkInfo = None
   
   return dictNetworkInfo

# --------------------------------------------------------------------------------
# Obtém a lista de IPs válidos na rede
def getIPValidos(network_info: dict) -> list:
    if not network_info or not network_info['IP'] or not network_info['CIDR']:
        return None
    
    ip_network = f'{network_info['IP']}/{network_info['CIDR']}'
    network = ipaddress.ip_network(ip_network, strict=False)
    
    # Retorna todos os IPs válidos na rede
    return [str(ip) for ip in network.hosts()]

# --------------------------------------------------------------------------------
# Função principal 
def main():
    # Obtém as informações de rede
    netInfo = getNetworkInfo()

    # Exibe as informações de rede
    for k, v in netInfo.items():
        print(f'{k}: {v}')

    # Obtém e exibe a lista de IPs válidos
    IPsValidos = getIPValidos(netInfo)
    print(f'IP\'s válidos na rede: {len(IPsValidos)} ({IPsValidos[0]} - {IPsValidos[-1]})')

# --------------------------------------------------------------------------------
# Chama a função principal
if __name__ == "__main__":
    main()