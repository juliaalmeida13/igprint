import argparse
import asyncio
from .core import capturar_instagram
from rich.console import Console
from .core import RichArgParser
from .config import get_config  # supondo que você coloque o get_config em um módulo, por exemplo, config.py

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
            "O script abrirá o Edge (com as configurações definidas) e realizará a rolagem para \n"
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

    # Argumentos opcionais para sobrescrever as configurações se desejado.
    parser.add_argument(
        '--edge-path',
        type=str,
        default=None,
        help="(Opcional) Caminho para o executável do Edge."
    )
    parser.add_argument(
        '--user-data-dir',
        type=str,
        default=None,
        help="(Opcional) Caminho para o diretório de dados do usuário do Edge (perfil que já possui o Instagram autenticado)."
    )
    args = parser.parse_args()

    # Recupera as configurações do arquivo de configuração
    default_edge_path, default_user_data_dir = get_config()

    # Se o usuário passar os argumentos via linha de comando, eles sobrescrevem os defaults
    edge_path = args.edge_path if args.edge_path is not None else default_edge_path
    user_data_dir = args.user_data_dir if args.user_data_dir is not None else default_user_data_dir

    target_url = f"https://www.instagram.com/{args.profile}/reels/"
    asyncio.get_event_loop().run_until_complete(capturar_instagram(target_url, args.profile, edge_path, user_data_dir))


if __name__ == '__main__':
    main()
