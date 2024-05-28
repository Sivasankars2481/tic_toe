import tkinter as tk

# Define the Tic Tac Toe board
board = [[None, None, None],
         [None, None, None],
         [None, None, None]]

# Define the current player
current_player = "X"

# Define the function to check if there is a winner
def check_winner():
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] != None:
            return board[row][0]
        elif board[0][row] == board[1][row] == board[2][row] != None:
            return board[0][row]
        elif board[row][0] == board[1][1] == board[2][2] != None:
            return board[row][0]
        elif board[0][2] == board[1][1] == board[2][0] != None:
            return board[0][2]
    return None

# Define the function to make a move
def make_move(row, col):
    global board, current_player
    if board[row][col] is None:
        board[row][col] = current_player
        current_player = "X" if current_player == "O" else "O"

# Define the function to restart the game
def restart_game():
    global board, current_player
    board = [[None, None, None],
             [None, None, None],
             [None, None, None]]
    current_player = "X"

# Create the Tkinter window
window = tk.Tk()
window.title("Tic Tac Toe")

# Create the Tic Tac Toe board buttons
buttons = []
for row in range(3):
    for col in range(3):
        button = tk.Button(window, text="", command=lambda row=row, col=col: make_move(row, col))
        buttons.append(button)
        button.grid(row=row, column=col)

# Create the restart button
restart_button = tk.Button(window, text="Restart", command=restart_game)
restart_button.grid(row=3, column=0, columnspan=3)

# Start the Tkinter mainloop
window.mainloop()