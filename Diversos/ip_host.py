import socket

host = input('Informe a URL: ')

ip = socket.gethostbyname(host)

print(ip)