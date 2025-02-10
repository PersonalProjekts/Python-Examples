import os, pyqrcode

# --------------------------------------------------------------------------------
# Função principal 
def main():
   # Obtendo o diretório corrente
   DIR_APP = os.path.dirname(__file__)

   # Solicitando o que será gerado o QrCode
   strTexto = input('Digite o que você deseja gerar o QrCode: ')

   # Gerando o QrCode
   imgQrcode = pyqrcode.create(strTexto)

   # Salvando o QrCode no formato SVG
   imgQrcode.svg(DIR_APP + '\\qrcode.svg', scale=8)

   # Salvando o QrCode no formato PNG
   imgQrcode.png(DIR_APP + '\\qrcode.png', scale=6)

# --------------------------------------------------------------------------------
# Chama a função principal
if __name__ == "__main__":
    main()