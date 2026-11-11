"""Задание 8: Диалог выбора файла."""

import os
import tkinter as tk
from tkinter import filedialog, ttk


class FileSelectorLogic:
    @staticmethod
    def process_selected_path(filepath: str) -> str:
        if not filepath:
            return "Файл не выбран"
        filename = os.path.basename(filepath)
        return f"Выбран файл: {filename}"


class FileSelectorApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Выбор файла")
        self.logic = FileSelectorLogic()

        self.btn = ttk.Button(root, text="Открыть файл", command=self.choose_file)
        self.btn.pack(padx=20, pady=10)

        self.result_label = ttk.Label(root, text="Файл не выбран")
        self.result_label.pack(padx=20, pady=10)

    def choose_file(self):
        path = filedialog.askopenfilename()
        message = self.logic.process_selected_path(path)
        self.result_label.config(text=message)


if __name__ == "__main__":
    root = tk.Tk()
    app = FileSelectorApp(root)
    root.mainloop()
