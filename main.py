import tkinter as tk
SIZE = 75

othello = tk.Tk()
othello.title("Othello")

"""Règles de l'Othello : https://www.ffothello.org/othello/regles-du-jeu/"""

# Convertit l'endroit où l'utilisateur clique en une case du tableau board
def convertir(x, y):
    row = y // SIZE
    col = x // SIZE
    return int(row), int(col)

# Vérifie si une des 11 cases adjacentes à la case cliqué n'est pas vide 
def adjacent(row,col):
    for i in range(-1,2):
        for j in range(-1,2):
            if (i == 0) and (j == 0):
                continue
            if (0 <= row+i < 8) and (0 <= col+j < 8): 
                if(board[row+i][col+j] != 0):
                    return False
    return True

# Vérifie si on peut retourner les pièces ou non
def can_flip(row,col):
    for i in range(-1,2):
        for j in range(-1,2):
            if(i == 0) and (j == 0):
                continue
        r, c = row + i, col + j
        if((0 <= r < 8) and (0 <= c < 8)) and (board[r][c] != player_turn) and (board[r][c] != 0):
            while (0 <= r < 8) and (0 <= c < 8):
                r+=i
                j+=i
                if not (0 <= r < 8 and 0 <= c < 8):
                    break
                if board[r][c] == 0:
                    break
                if board[r][c] == player_turn:
                    return True
    return False

#Quand on clique sur la case, on vérifie si on peut bien poser la tuile et on pose une tuile de la couleur du joueur correspondant.
def on_click(event):
    global board, player_turn
    row, col = convertir(event.x, event.y)
    if(board[row][col] == 0 and (adjacent(row,col))) and (can_flip(row,col)):
        return
    if board[row][col] == 0:
        if player_turn == 1:
            board[row][col] = 1
            canvas.create_oval(col * SIZE + 5, row * SIZE + 5,(col + 1) * SIZE - 5, (row + 1) * SIZE - 5, fill="black")
            player_turn = 2
        else:
            board[row][col] = 2
            canvas.create_oval(col * SIZE + 5, row * SIZE + 5,(col + 1) * SIZE - 5, (row + 1) * SIZE - 5, fill="white")
            player_turn = 1

# Les 4 tuiles du milieu de plateau
def initialiser():
    board[3][3] = 1
    board[3][4] = 2     
    board[4][3] = 2
    board[4][4] = 1

    canvas.create_oval(3 * SIZE + 5, 3 * SIZE + 5, (3 + 1) * SIZE - 5, (3 + 1) * SIZE - 5 , fill="black")
    canvas.create_oval(3 * SIZE + 5, 4 * SIZE + 5, (3 + 1) * SIZE - 5, (4 + 1) * SIZE - 5 , fill="white")
    canvas.create_oval(4 * SIZE + 5, 3 * SIZE + 5, (4 + 1) * SIZE - 5, (3 + 1) * SIZE - 5 , fill="white")
    canvas.create_oval(4 * SIZE + 5, 4 * SIZE + 5, (4 + 1) * SIZE - 5, (4 + 1) * SIZE - 5 , fill="black")

# Initialisation d'un tableau à deux dimensions qui va garder un compte des valeurs dans les cases
board = [[0 for _ in range(8)] for _ in range(8)]

# Création de la fenêtre de jeu
canvas = tk.Canvas(othello, width=600, height=600, bg="blue")
canvas.pack()

for i in range(9):
    canvas.create_line(0, i*75, 600, i*75, fill="black")
    canvas.create_line(i*75, 0, i*75, 600, fill="black")

initialiser()

player_turn = 1
canvas.bind("<Button-1>", on_click)

othello.mainloop()