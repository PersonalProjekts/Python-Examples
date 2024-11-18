'''
    Este exemplo lista as redes WIFI que já foram conectadas e suas senhas.
'''

import subprocess

# Armazenando os dados dos perfis (redes wi-fi) na variável "data"
# executando o primeiro comando CMD usando subprocess.check_output
data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles'])
data = data.decode('utf-8', errors ='backslashreplace').split('\n')

# Armazenando os perfis (redes wi-fi) em uma lista
perfis = [i.split(':')[1][1:-1] for i in data if 'Todos os Perfis de Usu\\xa0rios' in i]

# Checando e imprimindo as senhas wi-fi se elas estiverem disponíveis
for perfil in perfis:
    try:
        # Armazenando as senhas dos perfis (redes wi-fi) na variável "senha"
        # executando o segundo comando CMD usando subprocess.check_output
        senhas = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', perfil, 'key=clear'])
        senhas = senhas.decode('utf-8', errors ='backslashreplace').split('\n')
        # Armazenando as senhas ("Chave -> "Key Content")
        senhas = [b.split(":")[1][1:-1] for b in senhas if "Chave" in b]
        # Imprimindo as redes wi-fi e suas senhas 
        try:
            print (f'{perfil:<30}|  {senhas[1]:<}')
        except IndexError:
            print (f'{perfil:<30}|  {"*****":<}')
    except subprocess.CalledProcessError:
        print (f'{perfil:<30}|  {"ERRO DE CODIFICAÇÃO":<}')
