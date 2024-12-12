import tkinter as tk

class GameWindow(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Game Window")
        self.geometry("400x300")

        # Labels
        self.label = tk.Label(self, text="Game is in progress...")
        self.label.pack(pady=10)

        # Buttons
        self.pause_button = tk.Button(self, text="Pause", command=self.pause_game)
        self.pause_button.pack(pady=5)

        self.quit_button = tk.Button(self, text="Quit", command=self.quit_game)
        self.quit_button.pack(pady=5)

    def pause_game(self):
        # Pause game logic here
        pass

    def quit_game(self):
        self.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    game_window = GameWindow(root)
    game_window.mainloop()
