import tkinter as tk
SIZE = 75

othello = tk.Tk()
othello.title("Othello : tour du Joueur 1")

"""Règles de l'Othello : https://www.ffothello.org/othello/regles-du-jeu/"""


# Convertit l'endroit où l'utilisateur clique en une case du tableau board
def convertir(x, y):
    row = y // SIZE
    col = x // SIZE
    return int(row), int(col)


# Vérifie si on peut retourner les pièces ou non
def can_flip(row,col):
    for i in range(-1,2):
        for j in range(-1,2):
            if(i == 0) and (j == 0):
                continue
            r, c = row + i, col + j
            while((0 <= r < 8 and 0 <= c < 8) and (board[r][c] != 0 and board[r][c] != player_turn)):
                r+=i
                c+=j
                if not (0 <= r < 8 and 0 <= c < 8):
                    break
                if board[r][c] == 0:
                    break
                if board[r][c] == player_turn:
                    return False
    return True


def flip(row, col):
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:  # Ignorer la direction centrale
                continue

            r, c = row + i, col + j
            pieces_to_flip = []  # Stocke les pièces à retourner temporairement

            # Parcourir dans une direction donnée
            while 0 <= r < 8 and 0 <= c < 8:
                if board[r][c] == 0:  # Case vide : direction invalide
                    break
                elif board[r][c] == player_turn:  # Pièce du joueur actuel
                    # Séquence valide, retourner les pièces collectées
                    for rr, cc in pieces_to_flip:
                        board[rr][cc] = player_turn
                        color = "black" if player_turn == 1 else "white"
                        canvas.create_oval(
                            cc * SIZE + 5, rr * SIZE + 5,
                            (cc + 1) * SIZE - 5, (rr + 1) * SIZE - 5,
                            fill=color
                        )
                    break
                else:  # Pièce adverse
                    pieces_to_flip.append((r, c))  # Ajouter la pièce à la liste
                r += i
                c += j


def change_player_turn():
    global player_turn
    if(player_turn == 1):
        othello.title("Othello : tour du Joueur 2")
        player_turn = 2
    else:
        othello.title("Othello : tour du Joueur 1")
        player_turn = 1


def count():
    a = 1
    for i in range(8):
        for j in range(8):
            if board[i][j] == 0:
                return False
            if(can_flip(i,j)):
                a = 0
    if(a):
        return True
    return True


def who_win():
    sb=0;sn=0
    for i in range(8):
        for j in range(8):
            if(board[i][j] == 1):
                sn+=1
            else:
                sb+=1
        if sn > sb:
            othello.title("Le Joueur 1 a gagné !")
        if sb > sn:
            othello.title("Le Joueur 2 a gagné !")
        else:
            othello.title("Egalité")


#Quand on clique sur la case, on vérifie si on peut bien poser la tuile et on pose une tuile de la couleur du joueur correspondant.
def on_click(event):
    global board, player_turn
    if player_turn == None:
        player_turn = 1
    row, col = convertir(event.x, event.y)
    if(board[row][col] == 0 and (can_flip(row,col))):
        return
    if board[row][col] == 0:
        if player_turn == 1:
            board[row][col] = 1
            canvas.create_oval(col * SIZE + 5, row * SIZE + 5,(col + 1) * SIZE - 5, (row + 1) * SIZE - 5, fill="black")
            flip(row,col)
            change_player_turn()
        else:
            board[row][col] = 2
            canvas.create_oval(col * SIZE + 5, row * SIZE + 5,(col + 1) * SIZE - 5, (row + 1) * SIZE - 5, fill="white")
            flip(row,col)
            change_player_turn()
        if(count()):
            who_win()


# Les 4 tuiles du milieu de plateau
def initialiser():
    board[3][3] = 2
    board[3][4] = 1     
    board[4][3] = 1
    board[4][4] = 2

    canvas.create_oval(3 * SIZE + 5, 3 * SIZE + 5, (3 + 1) * SIZE - 5, (3 + 1) * SIZE - 5 , fill="white")
    canvas.create_oval(3 * SIZE + 5, 4 * SIZE + 5, (3 + 1) * SIZE - 5, (4 + 1) * SIZE - 5 , fill="black")
    canvas.create_oval(4 * SIZE + 5, 3 * SIZE + 5, (4 + 1) * SIZE - 5, (3 + 1) * SIZE - 5 , fill="black")
    canvas.create_oval(4 * SIZE + 5, 4 * SIZE + 5, (4 + 1) * SIZE - 5, (4 + 1) * SIZE - 5 , fill="white")


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