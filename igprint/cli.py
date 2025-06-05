import argparse
import asyncio
from .core import capturar_instagram
from rich.console import Console
from .core import RichArgParser
from .config import get_config  # Lê o config ajustado com USERPROFILE

console = Console()

def main():
    parser = RichArgParser(
        prog='igprint',
        description=(
            "Captura screenshots do feed do Instagram de um perfil específico, \n"
            "rolando a página até carregar ao menos 42 imagens."
        ),
        epilog=(
            "Exemplo de uso:\n"
            "  [bold italic cyan] igprint --profile kaarpage\n\n [/bold italic cyan]"
            "O script abrirá o Chrome (com as configurações definidas) e realizará a rolagem para \n"
            "carregar as imagens, gerando um arquivo <profile>.png."
        ),
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument(
        '--profile',
        type=str,
        default='kaarpage',
        help="Nome do usuário do Instagram (ex.: kaarpage)."
    )

    parser.add_argument(
        '--chrome-path',
        type=str,
        default=None,
        help="(Opcional) Caminho para o executável do Chrome."
    )
    parser.add_argument(
        '--user-data-dir',
        type=str,
        default=None,
        help="(Opcional) Caminho para o diretório de dados do usuário do Chrome (perfil que já possui o Instagram autenticado)."
    )

    args = parser.parse_args()

    # Carrega as configurações padrão do config.ini
    default_chrome_path, default_user_data_dir = get_config()

    # Prioriza argumentos de linha de comando, se fornecidos
    chrome_path = args.chrome_path if args.chrome_path is not None else default_chrome_path
    user_data_dir = args.user_data_dir if args.user_data_dir is not None else default_user_data_dir

    target_url = f"https://www.instagram.com/{args.profile}"

    # Usa asyncio.run() para Python 3.7+
    asyncio.run(
        capturar_instagram(target_url, args.profile, chrome_path, user_data_dir)
    )

if __name__ == '__main__':
    main()
