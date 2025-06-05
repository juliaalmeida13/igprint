import os
import configparser


def get_config():
    # Define o caminho para o arquivo de configuração no diretório home do usuário
    config_path = os.path.expanduser("~/.igprint_config.ini")
    config = configparser.ConfigParser()

    user = os.getlogin()

    # Se o arquivo existir, lê as configurações; se não, cria com valores padrões
    if os.path.exists(config_path):
        config.read(config_path)
    else:
        # Cria um arquivo de configuração com valores padrão
        config['DEFAULT'] = {
            'edge_path': r'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',
            'user_data_dir': f'C:/Users/{user}/AppData/Local/Microsoft/Edge/User Data/Default',
        }
        with open(config_path, 'w') as configfile:
            config.write(configfile)

    # Retorna os valores de configuração
    return config['DEFAULT']['edge_path'], config['DEFAULT']['user_data_dir']
