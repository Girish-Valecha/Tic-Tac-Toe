import tkinter as tk
import random

# Constants
WIDTH = 300
HEIGHT = 300
CELL_SIZE = 100
X_CHAR = "X"
O_CHAR = "O"

class TicTacToe:
    def __init__(self, canvas):
        self.canvas = canvas
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = X_CHAR
        self.game_over = False
        self.winner = None

        self.draw_grid()

    def draw_grid(self):
        for i in range(1, 3):
            self.canvas.create_line(i * CELL_SIZE, 0, i * CELL_SIZE, HEIGHT, fill="black")
            self.canvas.create_line(0, i * CELL_SIZE, WIDTH, i * CELL_SIZE, fill="black")

    def make_move(self, row, col):
        if self.game_over or self.board[row][col] is not None:
            return
        self.board[row][col] = self.current_player
        self.draw_symbol(row, col, self.current_player)
        self.check_winner()
        self.switch_player()

    def draw_symbol(self, row, col, symbol):
        x1 = col * CELL_SIZE + CELL_SIZE // 4
        y1 = row * CELL_SIZE + CELL_SIZE // 4
        x2 = (col + 1) * CELL_SIZE - CELL_SIZE // 4
        y2 = (row + 1) * CELL_SIZE - CELL_SIZE // 4
        if symbol == X_CHAR:
            self.canvas.create_line(x1, y1, x2, y2, fill="blue", width=5)
            self.canvas.create_line(x1, y2, x2, y1, fill="blue", width=5)
        elif symbol == O_CHAR:
            self.canvas.create_oval(x1, y1, x2, y2, fill="red", width=5)

    def check_winner(self):
        # Check rows
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != None:
                self.winner = self.board[row][0]
                self.game_over = True
                return

        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != None:
                self.winner = self.board[0][col]
                self.game_over = True
                return

        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != None:
            self.winner = self.board[0][0]
            self.game_over = True
            return
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != None:
            self.winner = self.board[0][2]
            self.game_over = True
            return

        # Check for tie
        for row in range(3):
            for col in range(3):
                if self.board[row][col] is None:
                    return
        self.game_over = True

    def switch_player(self):
        if self.current_player == X_CHAR:
            self.current_player = O_CHAR
        else:
            self.current_player = X_CHAR

    def reset(self):
        self.board = [[None for _ in range(3)] for _ in range(3)]
        self.current_player = X_CHAR
        self.game_over = False
        self.winner = None
        self.canvas.delete("all")
        self.draw_grid()

def on_click(event):
    col = int(event.x // CELL_SIZE)
    row = int(event.y // CELL_SIZE)
    tic_tac_toe.make_move(row, col)

# Create the main window
window = tk.Tk()
window.title("Tic-Tac-Toe")
window.geometry(f"{WIDTH}x{HEIGHT}")

# Create the canvas
canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()

# Create the Tic-Tac-Toe game
tic_tac_toe = TicTacToe(canvas)

# Bind the click event
canvas.bind("<Button-1>", on_click)

# Create the restart button
restart_button = tk.Button(window, text="Restart", command=tic_tac_toe.reset)
restart_button.pack(pady=10)

# Run the main loop
window.mainloop()