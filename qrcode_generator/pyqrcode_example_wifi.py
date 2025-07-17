import os, pyqrcode

# --------------------------------------------------------------------------------
# Função principal 
def main():
   # Credenciais da Rede WIFI
   WIFI_SSID = 'YOUR_WIFI_SSID'
   WIFI_PWD  = 'YOUR_WIFI_PWD'
   WIFI_SEC  = ['WPA', 'WEP', 'WPA', 'nopass', 'WEP40']

   # Obtendo o diretório corrente
   DIR_APP = os.path.dirname(__file__)

   # Definindo a string para criação do QRCode
   strWIFICredentials = f'WIFI:T:{WIFI_SEC[0]};S:{WIFI_SSID};P:{WIFI_PWD};;'

   # Criando o QRCode
   imgQrcode = pyqrcode.create(strWIFICredentials)

   # Salvando o QRCode
   imgQrcode.png(DIR_APP + '\\wifi_qrcode.png', scale=10)

# --------------------------------------------------------------------------------
# Chama a função principal
if __name__ == '__main__':
    main()