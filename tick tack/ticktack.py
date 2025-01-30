import tkinter as tk
from tkinter import messagebox


# Initialize the game board (3x3 grid)
class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.current_player = "X"  # Start with player X
        self.board = [["" for _ in range(3)] for _ in range(3)]  # Empty board
        self.buttons = [[None for _ in range(3)] for _ in range(3)]  # Button references

        self.create_buttons()  # Create the 3x3 grid of buttons

    def create_buttons(self):
        """Create the 3x3 grid of buttons for the Tic-Tac-Toe game."""
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.root, text="", width=10, height=3,
                                   font=("Arial", 24), command=lambda r=row, c=col: self.on_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def on_click(self, row, col):
        """Handle the button click event."""
        if self.board[row][col] == "":  # Only allow click if the cell is empty
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)  # Update button text

            if self.check_winner():
                messagebox.showinfo("Tic-Tac-Toe", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.check_draw():
                messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"  # Switch player

    def check_winner(self):
        """Check if the current player has won the game."""
        # Check rows, columns, and diagonals
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != "":
                return True
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False

    def check_draw(self):
        """Check if the game is a draw (all cells are filled)."""
        return all(self.board[row][col] != "" for row in range(3) for col in range(3))

    def reset_game(self):
        """Reset the game for a new round."""
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text="")
        self.current_player = "X"  # Start with player X again


# Create the main application window
root = tk.Tk()

# Create an instance of the TicTacToe game
game = TicTacToe(root)

# Start the Tkinter event loop
root.mainloop()
