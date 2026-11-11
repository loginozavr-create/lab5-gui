"""Задание 3 повышенной сложности: Игра «Кликер»."""

import tkinter as tk
from tkinter import ttk


class ClickerLogic:
    def __init__(self, points_per_click: int = 1):
        self.score = 0
        self.points_per_click = points_per_click

    def click(self) -> int:
        self.score += self.points_per_click
        return self.score

    def buy_upgrade(self, cost: int, bonus: int) -> bool:
        if self.score >= cost:
            self.score -= cost
            self.points_per_click += bonus
            return True
        return False


class ClickerApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Игра Кликер")
        self.logic = ClickerLogic()

        self.label = ttk.Label(root, text="Счёт: 0", font=("Arial", 16))
        self.label.pack(pady=10)

        self.click_btn = ttk.Button(root, text="Кликни меня!", command=self.on_click)
        self.click_btn.pack(pady=5)

        self.upgrade_btn = ttk.Button(
            root, text="Купить улучшение (+2 за 10 очков)", command=self.on_upgrade
        )
        self.upgrade_btn.pack(pady=5)

    def on_click(self):
        score = self.logic.click()
        self.label.config(text=f"Счёт: {score}")

    def on_upgrade(self):
        if self.logic.buy_upgrade(cost=10, bonus=2):
            self.label.config(text=f"Счёт: {self.logic.score}")


if __name__ == "__main__":
    root = tk.Tk()
    app = ClickerApp(root)
    root.mainloop()
