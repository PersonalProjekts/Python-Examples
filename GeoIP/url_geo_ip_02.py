import socket
from geolite2 import geolite2

# Informando o endereço desejado
hostname = input('\nInforme a URL: ')

# Obtendo o IP da URL
ip_address = socket.gethostbyname(hostname)

print('\n'+'-'*80)
print(f'URL ......: {hostname}')
print(f'IP address: {ip_address}')

# Criando o objeto
reader    = geolite2.reader()

# Efetuando a busca pelo IP
localizar = reader.get(ip_address)

if localizar is not None:
    print('\n'+'-'*80)
    print(localizar)
    print('\n'+'-'*80)
    print(f'IP .........: {ip_address}')
    print(f'Cidade......: {localizar["city"]["names"]["pt-BR"]}')
    print(f'Estado .....: {localizar["subdivisions"][0]["names"]["en"]}')
    print(f'País .......: {localizar["country"]["names"]["pt-BR"]}')
    print(f'Continente .: {localizar["continent"]["names"]["pt-BR"]}')
    print(f'Localização : ({localizar["location"]["latitude"]}, {localizar["location"]["longitude"]})')
    print(f'Time-Zone ..: {localizar["location"]["time_zone"]}')
    print('-'*80+'\n')
