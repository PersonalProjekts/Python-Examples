import sys, socket, requests

# --------------------------------------------------------------------------------
# Função principal 
def main():
   # Obtém o nome do seu computador
   hostname = socket.gethostname()

   # Obtém o IP do seu computador na sua rede
   ip_interno = socket.gethostbyname(hostname)

   # Obtém o IP externo da sua rede através da Amazon Web Services (AWS)
   reqServer = requests.get('https://checkip.amazonaws.com')

   # Verifica se a requisição não foi bem sucedida
   if reqServer.status_code != 200:
      sys.exit(f'ERRO: Erro ao obter o IP externo\n{reqServer.status_code}')

   # Obtém o IP externo da sua rede
   ip_externo = reqServer.text.strip()

   # Exibe as informações obtidas
   print('\n' + '-' * 80)
   print(f'Hostname ..: {hostname}')
   print(f'IP Interno : {ip_interno}')
   print(f'IP Externo : {ip_externo}')
   print('-' * 80 + '\n')

# --------------------------------------------------------------------------------
# Chama a função principal
if __name__ == "__main__":
    main()