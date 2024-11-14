'''
   Este exemplo informa o IP de uma determinada URL.
'''

import socket

host = input('Informe a URL: ')

ip = socket.gethostbyname(host)

print(f'\nO IP para a URL informada é: {ip}\n')
