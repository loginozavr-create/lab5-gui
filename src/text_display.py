"""Задание 2: Окно с текстовым полем и кнопкой, выводящей текст."""

import tkinter as tk
from tkinter import ttk


class TextDisplayLogic:
    @staticmethod
    def format_output(text: str) -> str:
        text = text.strip()
        if not text:
            return "Поле ввода пусто!"
        return f"Вы ввели: {text}"


class TextDisplayApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Вывод текста")
        self.logic = TextDisplayLogic()

        self.entry = ttk.Entry(root, width=30)
        self.entry.pack(padx=10, pady=5)

        self.btn = ttk.Button(root, text="Показать", command=self.on_click)
        self.btn.pack(padx=10, pady=5)

        self.label = ttk.Label(root, text="")
        self.label.pack(padx=10, pady=5)

    def on_click(self):
        result = self.logic.format_output(self.entry.get())
        self.label.config(text=result)


if __name__ == "__main__":
    root = tk.Tk()
    app = TextDisplayApp(root)
    root.mainloop()
