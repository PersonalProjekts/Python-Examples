import os
import pyqrcode

# Obtendo o diretório corrente
diretorio_atual = os.path.dirname(os.path.realpath(__file__))

# Solicitando o que será gerado o QrCode
str_input = input('Digite o que você deseja gerar o QrCode: ')

# Gerando o QrCode
img_qrcode = pyqrcode.create(str_input)

# Salvando o QrCode no formato SVG
img_qrcode.svg(diretorio_atual + '\\qrcode.svg', scale=8)

# Salvando o QrCode no formato PNG
img_qrcode.png(diretorio_atual + '\\qrcode.png', scale=6)
