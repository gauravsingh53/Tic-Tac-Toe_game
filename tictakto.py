from tkinter import *

root = Tk()
root.title("Tic Tac Toe")

player = "X"
buttons = [[None for _ in range(3)] for _ in range(3)]

def check_winner():
    for i in range(3):
        if buttons[i][0]["text"] == buttons[i][1]["text"] == buttons[i][2]["text"] != "":
            return True
        if buttons[0][i]["text"] == buttons[1][i]["text"] == buttons[2][i]["text"] != "":
            return True

    if buttons[0][0]["text"] == buttons[1][1]["text"] == buttons[2][2]["text"] != "":
        return True
    if buttons[0][2]["text"] == buttons[1][1]["text"] == buttons[2][0]["text"] != "":
        return True

    return False

def click(row, col):
    global player
    if buttons[row][col]["text"] == "":
        buttons[row][col]["text"] = player

        if check_winner():
            status.config(text=f"Player {player} wins!")
            disable_buttons()
        else:
            player = "O" if player == "X" else "X"
            status.config(text=f"Player {player}'s turn")

def disable_buttons():
    for row in buttons:
        for button in row:
            button.config(state=DISABLED)

status = Label(root, text="Player X's turn", font=("Arial", 16))
status.grid(row=0, column=0, columnspan=3)

for i in range(3):
    for j in range(3):
        buttons[i][j] = Button(root, text="", font=("Arial", 40), width=5, height=2,
                               command=lambda r=i, c=j: click(r, c))
        buttons[i][j].grid(row=i+1, column=j)

root.mainloop()