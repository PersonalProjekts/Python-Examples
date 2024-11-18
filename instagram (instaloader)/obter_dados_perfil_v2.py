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

try:
    # Instancia um objeto com base no usuário logado
    logged_profile = Instaloader()
    logged_profile.login(user, pwd)
except exceptions.BadCredentialsException:
    sys.exit('\nERRO: Credenciais Inválidas...')    
except exceptions.InvalidArgumentException:
    sys.exit('\nERRO: Argumentos Inválidos...')    
except exceptions.ConnectionException:
    sys.exit('\nERRO: Erro de Conexão...')    
except exceptions.TwoFactorAuthRequiredException:
    sys.exit('\nAutenticação em 2 Fatores exigida...')
    two_factor_code = input('Informe o Código de Autenticação: ')
    try:
        logged_profile.two_factor_login(two_factor_code)
    except exceptions.InvalidArgumentException:
        sys.exit(f'\nERRO: Argumentos Inválidos...')
    except exceptions.BadCredentialsException:
        sys.exit(f'\nERRO: Falha na Autenticação de 2 Fatores...')
except:
    sys.exit(f'\nERRO: {sys.exc_info()[0]}')
else:
    # Solicita o perfil alvo
    target_profile = input('\nInforme o perfil alvo do Instagram .: ')
    try:
        # Objeto contendo os metadados do perfil alvo
        print('\n' + '-'*80)
        print(f'Obtendo dados do perfil @{target_profile}\n')
        profile = Profile.from_username(logged_profile.context, target_profile)
    except exceptions.ProfileNotExistsException:     
        sys.exit(f'\nERRO: Perfil @{target_profile} não existe...')    
    except:
        sys.exit(f'\nERRO: {sys.exc_info()[0]}')
    else:
        sys.exit(f'Seguidores .: {profile.get_followers().count}')
        sys.exit(f'Seguindo ...: {profile.get_followees().count}')
        sys.exit(f'Postagens ..: {profile.get_posts().count}')
        sys.exit(f'\nURL da foto do perfil:\n{profile.get_profile_pic_url()}')
        sys.exit('-'*80)
        logged_profile.close()
