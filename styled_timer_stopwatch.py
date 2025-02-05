import time
from rich.console import Console
from rich.prompt import Prompt
from rich.text import Text

console = Console()


def timer(seconds):
    console.print(f"[bold blue]Таймер запущен на {seconds} секунд.[/bold blue]")
    for remaining in range(seconds, 0, -1):
        console.print(f"[bold yellow]Осталось времени: {remaining} секунд.[/bold yellow]")
        time.sleep(1)
    console.print("[bold red]Время вышло![/bold red]")


def stopwatch():
    console.print("[bold green]Секундомер запущен. Нажмите 'Enter' для остановки.[/bold green]")
    start_time = time.time()
    input()  # Ожидаем нажатия клавиши Enter
    elapsed_time = time.time() - start_time
    console.print(f"[bold magenta]Прошло времени: {elapsed_time:.2f} секунд.[/bold magenta]")


def main():
    while True:
        console.print("\n[bold cyan]Выберите действие:[/bold cyan]")
        console.print("[green]1.[/green] Запустить таймер")
        console.print("[green]2.[/green] Запустить секундомер")
        console.print("[green]3.[/green] Выход")

        choice = Prompt.ask("Введите номер действия")

        if choice == '1':
            seconds = Prompt.ask("Введите количество секунд", default="10")
            timer(int(seconds))
        elif choice == '2':
            stopwatch()
        elif choice == '3':
            console.print("[bold red]Выход из программы.[/bold red]")
            break
        else:
            console.print("[bold red]Неверный выбор. Пожалуйста, попробуйте снова.[/bold red]")


if __name__ == "__main__":
    main()
