import sys, socket, requests

# Obtem o nome do seu computador
hostname = socket.gethostname()

# Obtem o IP do seu computador na sua rede
ip_interno = socket.gethostbyname(hostname)

# Obtem o IP externo da sua rede através da Amazon Web Services (AWS)
reqServer = requests.get('https://checkip.amazonaws.com')

# Verifica se a requisição não foi bem sucedida
if reqServer.status_code != 200:
   sys.exit(f'ERRO:Erro ao obter o IP externo\n{reqServer.status_code}')

# Obtem o IP externo da sua rede
ip_externo = reqServer.text.strip()
print('\n'+'-'*80)
print(f'Hostname ..: {hostname}')
print(f'IP Interno : {ip_interno}')
print(f'IP Externo : {ip_externo}')
print('-'*80+'\n')
