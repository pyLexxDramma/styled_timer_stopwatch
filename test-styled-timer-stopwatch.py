import unittest
import tkinter as tk
from unittest.mock import patch
from io import StringIO
from contextlib import redirect_stdout
from tkinter import messagebox
from tkinter import ttk
from unittest.mock import MagicMock
import time

# Импортируем класс TimerApp из вашего основного файла
from styled_timer_stopwatch import TimerApp

class TestTimerApp(unittest.TestCase):

    def setUp(self):
        """Создаем экземпляр приложения перед каждым тестом."""
        self.app = TimerApp()
        self.root = self.app.root  # Сохраняем ссылку на tk.Tk()

    def tearDown(self):
        """Уничтожаем окно после каждого теста."""
        try:
             self.root.destroy()
        except tk.TclError:
            pass # Уже уничтожено

    def test_start_timer_valid_input(self):
        """Тест запуска таймера с корректным вводом."""
        self.app.timer_entry.insert(0, "5")  # Вводим 5 секунд
        self.app.start_timer()
        self.app.root.update()
        time.sleep(1.1)  # Ждем немного больше 1 секунды
        self.assertLess(self.app.remaining_time, 5)  # Проверяем, что remaining_time уменьшилось
        self.assertEqual(str(self.app.start_timer_button["state"]), str(tk.DISABLED))
        self.assertEqual(str(self.app.stop_timer_button["state"]), str(tk.NORMAL))
        self.assertEqual(str(self.app.timer_entry["state"]), str(tk.DISABLED))

    def test_start_timer_invalid_input(self):
        """Тест запуска таймера с некорректным вводом (не число)."""
        self.app.timer_entry.insert(0, "abc")  # Вводим текст
        with patch("tkinter.messagebox.showerror") as mock_showerror:  # Перехватываем messagebox
            self.app.start_timer()
            mock_showerror.assert_called_once() # Убеждаемся, что showerror был вызван
        self.assertFalse(self.app.timer_running)
        # Проверяем что entry все еще доступен
        self.assertEqual(str(self.app.timer_entry["state"]), str(tk.NORMAL))

    def test_start_timer_zero_input(self):
        """Тест запуска таймера с нулевым вводом."""
        self.app.timer_entry.insert(0, "0")  # Вводим 0 секунд
        with patch("tkinter.messagebox.showerror") as mock_showerror: # Перехватываем messagebox
            self.app.start_timer()
            mock_showerror.assert_called_once()
        self.assertFalse(self.app.timer_running)
        # Проверяем что entry все еще доступен
        self.assertEqual(str(self.app.timer_entry["state"]), str(tk.NORMAL))

    def test_stop_timer(self):
        """Тест остановки таймера."""
        self.app.timer_entry.insert(0, "5")
        self.app.start_timer()
        self.app.stop_timer()
        self.assertFalse(self.app.timer_running)
        self.assertEqual(str(self.app.start_timer_button["state"]), str(tk.NORMAL))
        self.assertEqual(str(self.app.stop_timer_button["state"]), str(tk.DISABLED))
        self.assertEqual(str(self.app.timer_entry["state"]), str(tk.NORMAL))

    @patch('time.time')
    def test_start_stopwatch(self, mock_time):
        """Тест запуска секундомера."""
        mock_time.return_value = 100 # Задаем начальное время
        self.app.start_stopwatch()
        self.assertTrue(self.app.stopwatch_running)
        self.assertEqual(str(self.app.start_stopwatch_button["state"]), str(tk.DISABLED))
        self.assertEqual(str(self.app.stop_stopwatch_button["state"]), str(tk.NORMAL))

    @patch('time.time')
    def test_stop_stopwatch(self, mock_time):
         """Тест остановки секундомера."""
         mock_time.return_value = 100
         self.app.start_stopwatch()
         self.app.stop_stopwatch()
         self.assertFalse(self.app.stopwatch_running)
         self.assertEqual(str(self.app.start_stopwatch_button["state"]), str(tk.NORMAL))
         self.assertEqual(str(self.app.stop_stopwatch_button["state"]), str(tk.DISABLED))


if __name__ == '__main__':
    unittest.main()