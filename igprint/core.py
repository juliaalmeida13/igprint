import sys
import asyncio
import argparse
from pyppeteer import launch
from rich.console import Console
from rich.panel import Panel
from rich.progress import Progress, BarColumn, TextColumn

console = Console()

class RichArgParser(argparse.ArgumentParser):
    """
    Parser customizado que utiliza Rich para imprimir o help dentro de um Panel
    e preserva as quebras de linha na description/epilog via RawTextHelpFormatter.
    """
    def __init__(self, *args, **kwargs):
        # Força a formatação raw para preservar as quebras de linha
        if 'formatter_class' not in kwargs:
            kwargs['formatter_class'] = argparse.RawTextHelpFormatter
        super().__init__(*args, **kwargs)

    def print_help(self, file=None):
        if file is None:
            file = sys.stdout
        rich_console = Console(file=file)
        rich_console.print(self._make_rich_help())

    def _make_rich_help(self):
        help_text = super().format_help()
        return Panel(
            help_text, 
            title="[bold green]Ajuda do Script[/bold green]", 
            expand=False
        )

async def wait_for_images_to_load(page):
    await page.evaluate('''() => {
        return new Promise((resolve) => {
            const imgs = Array.from(document.getElementsByTagName('img'));
            let loadedCount = 0;
            const total = imgs.length;

            const checkIfDone = () => {
                if (loadedCount === total) {
                    resolve(true);
                }
            };

            imgs.forEach((img) => {
                if (img.complete) {
                    loadedCount++;
                    checkIfDone();
                } else {
                    img.addEventListener('load', () => {
                        loadedCount++;
                        checkIfDone();
                    });
                    img.addEventListener('error', () => {
                        loadedCount++;
                        checkIfDone();
                    });
                }
            });

            if (total === 0) {
                resolve(true);
            }
        });
    }''')

async def capturar_instagram(url, username, edge_path, user_data_dir, max_scroll_attempts=10, min_images=42, scroll_pause=1):
  
    browser = await launch(
        headless=False,
        executablePath=edge_path,
        args=[
            "--no-sandbox",
            "--disable-setuid-sandbox",
            f"--user-data-dir={user_data_dir}",
            "--profile-directory=Default"
        ]
    )
    page = await browser.newPage()
    await page.setViewport({'width': 420, 'height': 1080})
    page.setDefaultNavigationTimeout(60000)

    console.print(f"\n[bold blue]Navegando para:[/bold blue] {url}")
    try:
        await page.goto(url, {'waitUntil': 'networkidle2', 'timeout': 60000})
    except Exception as e:
        console.print(f"[bold red]Erro durante a navegação:[/bold red] {e}")
        await browser.close()
        return

    console.print("[bold blue]Esperando página carregar inicialmente...[/bold blue]")
    await asyncio.sleep(1)

    console.print(f"[bold blue]Iniciando rolagem para carregar ao mínimo {min_images} imagens...[/bold blue]")
    
    with Progress(
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        TextColumn("[bold]{task.completed}/{task.total}"),
        console=console,
        transient=True
    ) as progress:
        scroll_task = progress.add_task(
            description="Rolagem da página | Imagens carregadas: 0", 
            total=max_scroll_attempts
        )
        
        while True:
            images_count = await page.evaluate("document.getElementsByTagName('img').length")
            progress.update(
                scroll_task,
                description=f"Rolagem da página | Imagens carregadas: {images_count}"
            )

            if images_count >= min_images:
                console.print("[bold green]Número mínimo de imagens atingido.[/bold green]")
                break

            if progress.tasks[0].completed >= max_scroll_attempts:
                console.print("[bold red]Limite máximo de rolagens atingido.[/bold red]")
                break

            await page.evaluate('window.scrollTo(0, document.body.scrollHeight);')
            progress.update(scroll_task, advance=1)
            console.print(
                f"Rolagem {progress.tasks[0].completed}/{max_scroll_attempts} realizada. "
                f"[cyan]({images_count} imagens atualmente)[/cyan]"
            )

            await asyncio.sleep(scroll_pause)

    console.print("\n[bold blue]Aguardando todas as imagens carregarem...[/bold blue]")
    await wait_for_images_to_load(page)

    console.print("[bold blue]Capturando screenshot da página completa...[/bold blue]")
    try:
        await page.screenshot({'path': f'{username}.png', 'fullPage': True})
        console.print(f"\n[bold green]✅ Screenshot salvo como {username}.png[/bold green]")
    except Exception as e:
        console.print(f"[bold red]Erro ao capturar a screenshot:[/bold red] {e}")

    await browser.close()
