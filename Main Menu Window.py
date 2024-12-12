import tkinter as tk
from tkinter import messagebox

class MainMenu(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Green Team of Captain Game")
        self.geometry("400x300")

        # Labels
        self.label = tk.Label(self, text="Welcome to the Green Team of Captain Game!")
        self.label.pack(pady=10)

        # Buttons
        self.start_button = tk.Button(self, text="Start Game", command=self.start_game)
        self.start_button.pack(pady=5)

        self.instructions_button = tk.Button(self, text="Instructions", command=self.show_instructions)
        self.instructions_button.pack(pady=5)

        self.exit_button = tk.Button(self, text="Exit", command=self.quit)
        self.exit_button.pack(pady=5)

    def start_game(self):
        messagebox.showinfo("Start Game", "Game is starting...")

    def show_instructions(self):
        messagebox.showinfo("Instructions", "Here are the game instructions...")

if __name__ == "__main__":
    app = MainMenu()
    app.mainloop()
