"""Модульные тесты для логики компонентов GUI (TDD)."""

import unittest
from src.text_display import TextDisplayLogic
from src.file_selector import FileSelectorLogic
from src.clicker_game import ClickerLogic
from src.chat_core import LocalChat


class TestGuiLogic(unittest.TestCase):
    # --- Задание 2: Текстовое поле и кнопка вывода ---
    def test_text_display_logic(self):
        logic = TextDisplayLogic()
        self.assertEqual(logic.format_output("Привет, мир!"), "Вы ввели: Привет, мир!")
        self.assertEqual(logic.format_output(""), "Поле ввода пусто!")

    # --- Задание 8: Логика выбора файла ---
    def test_file_selector_logic(self):
        logic = FileSelectorLogic()
        self.assertEqual(logic.process_selected_path("C:/data/test.txt"), "Выбран файл: test.txt")
        self.assertEqual(logic.process_selected_path(""), "Файл не выбран")

    # --- Повышенная сложность, Задание 3: Кликер ---
    def test_clicker_game_logic(self):
        game = ClickerLogic(points_per_click=1)
        self.assertEqual(game.click(), 1)
        self.assertEqual(game.click(), 2)
        # Покупка улучшения
        self.assertFalse(game.buy_upgrade(cost=10, bonus=2))
        for _ in range(8):
            game.click()
        self.assertEqual(game.score, 10)
        self.assertTrue(game.buy_upgrade(cost=10, bonus=2))
        self.assertEqual(game.score, 0)
        self.assertEqual(game.click(), 3)

    # --- Повышенная сложность, Задание 10: Локальный чат ---
    def test_local_chat_history(self):
        chat = LocalChat()
        chat.send_message("Степан", "Всем привет!")
        chat.send_message("Алексей", "Привет, Степан!")
        history = chat.get_history()
        self.assertEqual(len(history), 2)
        self.assertEqual(history[0], "[Степан]: Всем привет!")
        self.assertEqual(history[1], "[Алексей]: Привет, Степан!")

    def test_empty_chat_message(self):
        chat = LocalChat()
        with self.assertRaises(ValueError):
            chat.send_message("Степан", "   ")


if __name__ == "__main__":
    unittest.main()
