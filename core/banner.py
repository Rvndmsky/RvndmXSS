from rich.console import Console
from rich.panel import Panel
console=Console()
def show_banner(target=None):
    console.print()
    console.print(Panel.fit('[bold red]RvndmXSS[/bold red] | [bold cyan]Enggan Ngoding Nyuruh AI saja[/bold cyan]\n[white]LinkedIn: linkedin.com/in/ravenskadm[/white]', border_style='bold red'))
    if target:
        console.print(f"[bold yellow]Cari XSS dibantu AI :[/bold yellow] [bold white]{target}[/bold white]\n")
