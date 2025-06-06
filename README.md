# IGPRINT 📸

**IGPRINT** é um pacote Python que automatiza a captura de screenshots do feed do Instagram para um perfil específico. O script realiza a rolagem da página até carregar um número mínimo de imagens (padrão: 42) e, em seguida, captura uma imagem completa do feed.

Além disso, o pacote utiliza a biblioteca [Rich](https://github.com/Textualize/rich) para apresentar mensagens e um progress bar bonitinhos durante o processo, tornando a execução mais informativa e agradável.

## Funcionalidades

- **Captura automatizada**: Abre o navegador com sessão autenticada (configurável) e navega até o perfil especificado.
- **Rolagem dinâmica**: Rola a página para carregar as imagens até atingir o número mínimo definido.
- **Feedback visual**: Exibe mensagens coloridas e um progress bar durante a rolagem.
- **Configuração persistente**: Configurações do caminho para o executável do Chrome e para o diretório de dados do usuário (perfil autenticado) são salvos num arquivo de configuração para que o usuário precise configurá-los apenas uma vez.

## Estrutura do Projeto
```
igprint/ 
├── igprint/ # Diretório do pacote 
│ ├── init.py 
│ ├── cli.py # Interface de linha de comando (entry point) 
│ ├── config.py # Gerenciamento do arquivo de configuração 
│ └── core.py # Lógica principal de captura e rolagem 
├── setup.py # Arquivo de instalação do pacote 
└── README.md # Este arquivo
```

## Instalação

1. Clone este repositório ou faça o download do pacote.

## precisa criar um ambiente e tbm acessar o ambiente e tbm instalar o numpy

python -m venv .igp 
.\.igp\Scripts\activate
pip install numpy


2. Navegue até a raiz do projeto (onde se encontra o `setup.py`) e instale-o em modo _editable_:

   ```bash
   pip install -e .
Essa opção permite que você faça alterações no código e veja os resultados imediatamente, sem precisar reinstalar o pacote.

## ⚠ Configuração
Na primeira execução, o pacote criará um arquivo de configuração chamado ~/.igprint_config.ini (no diretório home do usuário) com os seguintes valores padrão:

```ini  
[DEFAULT]
chrome_path = C:/Program Files/Google/Chrome/Application/chrome.exe
user_data_dir = C:/Users/<user>/AppData/Local/Google/Chrome/User Data
```
Você pode editar este arquivo manualmente para ajustar os caminhos do executável do Chrome e do diretório de dados do usuário ou ajustar diretamente dentro do código presente no arquivo `igprint/config.py`

**ESSA CONFIGURAÇÃO É INDISPENSÁVEL OU A BIBLIOTECA NÃO FUNCIONARÁ CORRETAMENTE**

## Uso
Após a instalação, o pacote disponibiliza um comando de terminal:

```bash
igprint --profile <perfil>
```

Exemplo:
```bash
igprint --profile kaarpage
```

## Argumentos Opcionais
- **--profile:** Nome do usuário do Instagram (default: kaarpage).

- **--chrome-path:** (Opcional) Caminho para o executável do Chrome. Se não for fornecido, o valor configurado no arquivo de configuração será utilizado.

- **--user-data-dir:** (Opcional) Caminho para o diretório de dados do usuário do Chrome (perfil autenticado). Se não for fornecido, o valor configurado no arquivo de configuração será utilizado.

## Como Funciona
1. O script utiliza o ```pyppeteer``` para lançar uma instância do Chrome com as configurações de perfil já autenticado.

2. Navega para o perfil especificado no Instagram.

3. Realiza a rolagem da página enquanto exibe um progress bar com informações sobre o número de rolagens e de imagens carregadas.

4. Aguarda que todas as imagens sejam carregadas.

5. Captura uma screenshot da página completa e salva o arquivo com o nome ```<perfil>.png```

### Exemplo de Execução
```bash
igprint --profile kaarpage
```

> Durante a execução, você verá mensagens e um progress bar informando o progresso da rolagem e o número de imagens carregadas.

# Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests para melhorar o pacote.

## Licença
Distribuído sob a MIT License. Consulte o arquivo LICENSE para mais informações.

> Para utilizar, basta salvar o conteúdo acima em um arquivo chamado **README.md** na raiz do seu projeto.

