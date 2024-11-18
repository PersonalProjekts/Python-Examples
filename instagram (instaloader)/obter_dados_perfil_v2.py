'''
    Este exemplo exibe a quantidade de perfis seguidores, a quantidades de perfis que 
    são seguidos, a quantidade de postagens e a URL da foto do perfil de um determinado
    perfil do Instagram.

    Trata a exceção de autenticação de 2 fatores.

    Necessário instalar a biblioteca INSTALOADER
        pip install instaloader

    Documentação
        https://pypi.org/project/instaloader/
        https://instaloader.github.io/
'''

import getpass, sys
from instaloader import BadCredentialsException, Instaloader, Profile, exceptions

# Solicitando usuário e senha para efetuar login no Instagram
# Só é necessário para acessar dados de contas não públicas
user = input('\nInforme seu Login do Instagram .: ')
pwd  = getpass.getpass('Informe sua senha do Instagram .: ')

erro = True

try:
    # Instancia um objeto com base no usuário logado
    logged_profile = Instaloader()
    logged_profile.login(user, pwd)
except exceptions.BadCredentialsException:
    print('\nERRO: Credenciais Inválidas...')    
except exceptions.InvalidArgumentException:
    print('\nERRO: Argumentos Inválidos...')    
except exceptions.ConnectionException:
    print('\nERRO: Erro de Conexão...')    
except exceptions.TwoFactorAuthRequiredException:
    print('\nAutenticação em 2 Fatores exigida...')
    two_factor_code = input('Informe o Código de Autenticação: ')
    try:
        logged_profile.two_factor_login(two_factor_code)
    except exceptions.InvalidArgumentException:
        print(f'\nERRO: Argumentos Inválidos...')
    except exceptions.BadCredentialsException:
        print(f'\nERRO: Falha na Autenticação de 2 Fatores...')
    else:
        erro = False
except:
    print(f'\nERRO: {sys.exc_info()[0]}')
else:
    erro = False
finally:
    if erro: sys.exit()
    # Solicita o perfil alvo
    target_profile = input('\nInforme o perfil alvo do Instagram .: ')
    try:
        # Objeto contendo os metadados do perfil alvo
        print('\n' + '-'*80)
        print(f'Obtendo dados do perfil @{target_profile}\n')
        profile = Profile.from_username(logged_profile.context, target_profile)
    except exceptions.ProfileNotExistsException:     
        print(f'\nERRO: Perfil @{target_profile} não existe...')    
    except:
        print(f'\nERRO: {sys.exc_info()[0]}')
    else:
        print(f'Seguidores .: {profile.get_followers().count}')
        print(f'Seguindo ...: {profile.get_followees().count}')
        print(f'Postagens ..: {profile.get_posts().count}')
        print(f'\nURL da foto do perfil:\n{profile.get_profile_pic_url()}')
        print('-'*80)
    logged_profile.close()
