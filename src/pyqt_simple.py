"""Задание 10: Простейший GUI (демонстрация структуры PyQt/Tkinter)."""

import sys


def get_gui_info() -> str:
    return "PyQt5/Tkinter Base GUI Application"


def run_pyqt():  # pragma: no cover
    try:
        from PyQt5.QtWidgets import QApplication, QLabel, QWidget

        app = QApplication(sys.argv)
        window = QWidget()
        window.setWindowTitle("Простейший PyQt5")
        label = QLabel("Привет из PyQt5!", parent=window)
        label.move(50, 50)
        window.resize(250, 150)
        window.show()
        sys.exit(app.exec_())
    except ImportError:
        import tkinter as tk

        root = tk.Tk()
        root.title("Простейший GUI")
        lbl = tk.Label(root, text="Базовый GUI-виджет")
        lbl.pack(padx=30, pady=30)
        root.mainloop()


if __name__ == "__main__":
    run_pyqt()
