import os
import configparser

def get_config():
    # Define o caminho para o arquivo de configuração no diretório home do usuário
    config_path = os.path.expanduser("~/.igprint_config.ini")
    config = configparser.ConfigParser()

    # Caminhos padrão usando USERPROFILE (mais confiável no Windows)
    user_profile = os.environ['USERPROFILE']
    default_chrome_path = r"C:/Program Files/Google/Chrome/Application/chrome.exe"
    default_user_data_dir = os.path.join(user_profile, "AppData", "Local", "Google", "Chrome", "User Data")

    # Se o arquivo existir, lê as configurações; se não, cria com valores padrões
    if os.path.exists(config_path):
        config.read(config_path)
    else:
        config['DEFAULT'] = {
            'path': default_chrome_path,
            'user_data_dir': default_user_data_dir,
        }
        with open(config_path, 'w') as configfile:
            config.write(configfile)

    # Retorna os valores de configuração
    return config['DEFAULT']['path'], config['DEFAULT']['user_data_dir']
