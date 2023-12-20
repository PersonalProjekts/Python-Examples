# --------------------------------------------------------------------------------
# Este exemplo gera um QRCode com as credenciais para autenticação em uma rede 
# WIFI utilizando a biblioteca PYQRCODE.
#
# Necessário instalar a biblioteca PYQRCODE
#       pip install pyqrcode
#
# Documentação
#       https://pypi.org/project/PyQRCode/
# --------------------------------------------------------------------------------

import os, pyqrcode
#from PIL import Image
from pyqrcode import QRCode

# Credenciais da Rede WIFI
WIFI_SSID = 'YOUR_WIFI_SSID'
WIFI_PWD  = 'YOUR_WIFI_PWD'
WIFI_SEC  = ['WPA', 'WEP', 'WPA', 'nopass', 'WEP40']

# Obtendo o diretório corrente
DIR_APP    = os.path.dirname(os.path.realpath(__file__))

# Definindo a string para criação do QRCode
wifi_credentials = f'WIFI:T:{WIFI_SEC[0]};S:{WIFI_SSID};P:{WIFI_PWD};;'

# Criando o QRCode
img_qrcode = pyqrcode.create(wifi_credentials)

# Salvando o QRCode
img_qrcode.png(DIR_APP + '\\wifi_qrcode.png', scale=10)
