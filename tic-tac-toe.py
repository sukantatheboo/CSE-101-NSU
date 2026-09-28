import tkinter as tk
from tkinter import messagebox

# --- 1. Game Setup & Variables ---
root = tk.Tk()
root.title("Tic-Tac-Toe")

turn_O = True  # Tracks whose turn it is
boxes = []     # Stores the 9 button objects
move_count = 0 # Tracks total moves to check for a draw

# The 8 possible winning combinations (indices of the grid)
win_patterns = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8], # Horizontal
    [0, 3, 6], [1, 4, 7], [2, 5, 8], # Vertical
    [0, 4, 8], [2, 4, 6]             # Diagonal
]

# --- 2. Core Game Logic ---
def check_winner():
    # Check if any winning pattern is met
    for pattern in win_patterns:
        val1 = boxes[pattern[0]].cget("text")
        val2 = boxes[pattern[1]].cget("text")
        val3 = boxes[pattern[2]].cget("text")

        if val1 != "" and val1 == val2 and val2 == val3:
            messagebox.showinfo("Game Over", f"Congratulations, Winner is {val1}!")
            disable_all_boxes()
            return

    # Check for a draw if all 9 moves are made and no winner is found
    if move_count == 9:
        messagebox.showinfo("Game Over", "It's a Draw!")
        disable_all_boxes()

def box_clicked(index):
    global turn_O, move_count
    box = boxes[index]

    # Mark the box with O or X
    if turn_O:
        box.config(text="O", fg="blue")
        turn_O = False
    else:
        box.config(text="X", fg="red")
        turn_O = True

    # Disable the box so it can't be clicked again, count the move, and check for win
    box.config(state="disabled")
    move_count += 1
    check_winner()

# --- 3. Board Management ---
def disable_all_boxes():
    for box in boxes:
        box.config(state="disabled")

def reset_game():
    global turn_O, move_count
    turn_O = True
    move_count = 0
    for box in boxes:
        box.config(text="", state="normal")

# --- 4. User Interface (GUI) ---
# Generate the 3x3 grid of buttons
for i in range(9):
    # lambda i=i is used to capture the current value of 'i' for each distinct button
    btn = tk.Button(root, text="", font=('Arial', 24, 'bold'), width=5, height=2,
                    command=lambda i=i: box_clicked(i))
    
    # Calculate row and column dynamically using math (floor division and modulo)
    btn.grid(row=i//3, column=i%3, padx=5, pady=5)
    boxes.append(btn)

# Add the Reset Button at the bottom
reset_btn = tk.Button(root, text="Reset Game", font=('Arial', 14), command=reset_game)
reset_btn.grid(row=3, column=0, columnspan=3, sticky="we", pady=10)

# Run the application
root.mainloop()