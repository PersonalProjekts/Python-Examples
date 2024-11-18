'''
   Este exemplo gera um QRCode utilizando a biblioteca PYQRCODE

   Necessário instalar a biblioteca PYQRCODE
      pip install pyqrcode

   Documentação
      https://pypi.org/project/PyQRCode/
'''

import os
import pyqrcode

# Obtendo o diretório corrente
DIR_APP = os.path.dirname(os.path.realpath(__file__))

# Solicitando o que será gerado o QrCode
str_input = input('Digite o que você deseja gerar o QrCode: ')

# Gerando o QrCode
img_qrcode = pyqrcode.create(str_input)

# Salvando o QrCode no formato SVG
img_qrcode.svg(DIR_APP + '\\qrcode.svg', scale=8)

# Salvando o QrCode no formato PNG
img_qrcode.png(DIR_APP + '\\qrcode.png', scale=6)
