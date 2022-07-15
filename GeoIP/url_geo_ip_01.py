import socket
from geoip import geolite2

# Informando o endereço desejado
hostname = input('\nInforme a URL: ')

# Obtendo o IP da URL
ip_address = socket.gethostbyname(hostname)

print('\n'+'-'*80)
print(f'URL ......: {hostname}')
print(f'IP address: {ip_address}\n')

localizar = geolite2.lookup(ip_address)

if localizar is not None:
    print(localizar)
    print(localizar.to_dict())
    print('\n'+'-'*80)
    print('IP .........:', localizar.ip)
    print('País .......:', localizar.country)
    print('Continente .:', localizar.continent)
    print('Time zone ..:', localizar.timezone)
    print('Localização :', localizar.location)
    print('-'*80+'\n')
