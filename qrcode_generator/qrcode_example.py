import os
import qrcode

# --------------------------------------------------------------------------------
# Função principal 
def main():
    # Obtendo o diretório corrente
    DIR_APP = os.path.dirname(__file__)

    # Definições para o QrCode
    VERSAO     = 1.0              # Tamanho do QR Code gerado (1 a 40)
    BOX_SIZE   = 5                # Tamanho de cada box em pixels
    BORDER     = 1                # Espessura da borda
    BACK_COLOR = (255, 255, 255)  # Cor de fundo
    FILL_COLOR = (0, 0, 0)        # Cor do QrCode

    # Solicitando o que será gerado o QrCode
    strTexto = input('Digite o que você deseja gerar o QrCode: ')

    # Criando uma instância do tipo QRCode
    qrCode = qrcode.QRCode(version=VERSAO, box_size=BOX_SIZE, border=BORDER)

    # Gerando o qrcode
    qrCode.add_data(strTexto)
    qrCode.make(fit=True)

    # Salvando o qrcode
    imgQrcode = qrCode.make_image(back_color=BACK_COLOR, fill_color=FILL_COLOR)
    imgQrcode.save(DIR_APP + '\\qr_code.png')

# --------------------------------------------------------------------------------
# Chama a função principal
if __name__ == "__main__":
    main()