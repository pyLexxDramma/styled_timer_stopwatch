import time
import tkinter as tk
from tkinter import ttk, messagebox
from rich.console import Console

console = Console()


class TimerApp:
    """Приложение таймера и секундомера с графическим интерфейсом."""

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Таймер и Секундомер")
        self.root.geometry("300x250")  # Задаем размер окна

        # === Таймер ===
        self.timer_running = False
        self.timer_id = None
        self.remaining_time = 0

        # === Секундомер ===
        self.stopwatch_running = False
        self.stopwatch_start_time = 0
        self.stopwatch_elapsed_time = 0
        self.stopwatch_id = None

        self.create_widgets()

    def create_widgets(self):
        """Создает виджеты графического интерфейса."""

        # === Таймер ===
        ttk.Label(self.root, text="Таймер (секунды):").pack(pady=5)
        self.timer_entry = ttk.Entry(self.root)
        self.timer_entry.pack(pady=5)

        self.start_timer_button = ttk.Button(self.root, text="Запустить таймер", command=self.start_timer)
        self.start_timer_button.pack(pady=5)

        self.stop_timer_button = ttk.Button(self.root, text="Остановить таймер", command=self.stop_timer, state=tk.DISABLED)
        self.stop_timer_button.pack(pady=5)

        self.timer_label = ttk.Label(self.root, text="Оставшееся время: 0")
        self.timer_label.pack(pady=5)

        # === Секундомер ===
        self.stopwatch_label = ttk.Label(self.root, text="Время секундомера: 0.00")
        self.stopwatch_label.pack(pady=5)

        self.start_stopwatch_button = ttk.Button(self.root, text="Запустить секундомер", command=self.start_stopwatch)
        self.start_stopwatch_button.pack(pady=5)

        self.stop_stopwatch_button = ttk.Button(self.root, text="Остановить секундомер", command=self.stop_stopwatch, state=tk.DISABLED)
        self.stop_stopwatch_button.pack(pady=5)

    def start_timer(self):
        """Запускает таймер."""
        try:
            seconds = int(self.timer_entry.get())
            if seconds <= 0:
                messagebox.showerror("Ошибка", "Введите положительное число секунд.")
                return

            self.remaining_time = seconds
            self.timer_running = True
            self.start_timer_button["state"] = tk.DISABLED
            self.stop_timer_button["state"] = tk.NORMAL
            self.timer_entry["state"] = tk.DISABLED
            self.update_timer_display() # Обновляем отображение сразу
            self.update_timer()
        except ValueError:
            messagebox.showerror("Ошибка", "Введите целое число секунд.")

    def stop_timer(self):
        """Останавливает таймер."""
        self.timer_running = False
        self.start_timer_button["state"] = tk.NORMAL
        self.stop_timer_button["state"] = tk.DISABLED
        self.timer_entry["state"] = tk.NORMAL
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
        console.print("[bold red]Таймер остановлен.[/bold red]")

    def update_timer(self):
        """Обновляет таймер каждую секунду."""
        if self.timer_running and self.remaining_time > 0:
            self.remaining_time -= 1
            self.update_timer_display()
            self.timer_id = self.root.after(1000, self.update_timer)
        elif self.timer_running:
            self.update_timer_display() # Обновляем отображение перед уведомлением
            messagebox.showinfo("Таймер", "Время вышло!")
            self.stop_timer()
            console.print("[bold red]Время вышло![/bold red]")

    def update_timer_display(self):
        """Обновляет текст метки таймера."""
        self.timer_label.config(text=f"Оставшееся время: {self.remaining_time}")

    def start_stopwatch(self):
        """Запускает секундомер."""
        self.stopwatch_running = True
        self.stopwatch_start_time = time.time()
        self.start_stopwatch_button["state"] = tk.DISABLED
        self.stop_stopwatch_button["state"] = tk.NORMAL
        self.update_stopwatch()

    def stop_stopwatch(self):
        """Останавливает секундомер."""
        self.stopwatch_running = False
        self.start_stopwatch_button["state"] = tk.NORMAL
        self.stop_stopwatch_button["state"] = tk.DISABLED
        if self.stopwatch_id:
            self.root.after_cancel(self.stopwatch_id)

    def update_stopwatch(self):
        """Обновляет секундомер каждую миллисекунду."""
        if self.stopwatch_running:
            elapsed_time = time.time() - self.stopwatch_start_time
            self.stopwatch_elapsed_time = elapsed_time
            self.stopwatch_label.config(text=f"Время секундомера: {elapsed_time:.2f}")
            self.stopwatch_id = self.root.after(10, self.update_stopwatch)  # Обновляем каждые 10 миллисекунд (для более плавной анимации)

    def run(self):
        """Запускает главный цикл приложения."""
        self.root.mainloop()


if __name__ == "__main__":
    app = TimerApp()
    app.run()