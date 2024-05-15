import manager
from rich.console import Console
# from rich.padding import Padding
def firstpage_menu():
    console = Console()
    console.print("TRELLOMIZE", justify="center", style = "bold italic white")
    introduction = "Transform your project management experience with our innovative platform,\noffering streamlined coordination, real-time updates, and effective task management."
    console.print(introduction, justify="center", style="grey70")

firstpage_menu()