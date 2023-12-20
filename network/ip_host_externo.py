# --------------------------------------------------------------------------------
# Este exemplo informa o IP externo da sua conexão.
# --------------------------------------------------------------------------------

import socket, requests

# Obtem o nome do seu computador
hostname = socket.gethostname()

# Obtem o IP do seu computador na sua rede
ip_interno = socket.gethostbyname(hostname)

# Obtém o IP externo da sua rede através do IPIFY (https://www.ipify.org/)
print(requests.get('https://api.ipify.org'))
ip_externo = requests.get('https://api.ipify.org').text

print('\n'+'-'*80)
print(f'Hostname ..: {hostname}')
print(f'IP Interno : {ip_interno}')
print(f'IP Externo : {ip_externo}')
print('-'*80+'\n')