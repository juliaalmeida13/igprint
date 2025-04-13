import os
import configparser

def get_config():
    # Define o caminho para o arquivo de configuração no diretório home do usuário
    config_path = os.path.expanduser("~/.igprint_config.ini")
    config = configparser.ConfigParser()
    
    # Se o arquivo existir, lê as configurações; se não, cria com valores padrões
    if os.path.exists(config_path):
        config.read(config_path)
    else:
        # Cria um arquivo de configuração com valores padrão
        config['DEFAULT'] = {
            'chrome_path': r'C:/Program Files/Google/Chrome/Application/chrome.exe',
            'user_data_dir': r'C:/Users/<user>/AppData/Local/Google/Chrome/User Data'
        }
        with open(config_path, 'w') as configfile:
            config.write(configfile)
    
    # Retorna os valores de configuração
    return config['DEFAULT']['chrome_path'], config['DEFAULT']['user_data_dir']
