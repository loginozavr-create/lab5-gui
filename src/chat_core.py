"""Задание 10 повышенной сложности: Программа локального чата."""

from typing import List


class LocalChat:
    def __init__(self):
        self._history: List[str] = []

    def send_message(self, author: str, text: str) -> str:
        author = author.strip() or "Аноним"
        text = text.strip()
        if not text:
            raise ValueError("Сообщение не может быть пустым.")

        formatted = f"[{author}]: {text}"
        self._history.append(formatted)
        return formatted

    def get_history(self) -> List[str]:
        return list(self._history)
