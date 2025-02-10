import os, qrcode

# Obtendo o diretório corrente
DIR_APP = os.path.dirname(os.path.realpath(__file__))

# Definições para o QrCode
VERSAO     = 1.0              # Tamanho do QR Code gerado (1 a 40)
BOX_SIZE   = 5                # Tamanho de cada box em pixels
BORDER     = 1                # Espessura da borda
BACK_COLOR = (255, 255, 255)  # Cor de fundo
FILL_COLOR = (  0,   0,   0)  # Cor do QrCode

# Solicitando o que será gerado o QrCode
str_input = input('Digite o que você deseja gerar o QrCode: ')

# Criando uma instância do tipo QRCOde 
qr_code = qrcode.QRCode(version=VERSAO, box_size=BOX_SIZE, border=BORDER)

# Gerando o qrcode
qr_code.add_data(str_input)
qr_code.make(fit=True)

# Salvando o qrcode
img_qrcode = qr_code.make_image(back_color=BACK_COLOR, fill_color= FILL_COLOR)
img_qrcode.save(DIR_APP + '\\qr_code.png')