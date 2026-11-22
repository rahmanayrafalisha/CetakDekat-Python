"""
Program utama aplikasi CetakDekat.
Menjalankan aplikasi menggunakan Tkinter.
"""

import tkinter as tk
from ui import CetakDekatApp


def main():
    """Menjalankan aplikasi CetakDekat."""

    root = tk.Tk()
    aplikasi = CetakDekatApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()