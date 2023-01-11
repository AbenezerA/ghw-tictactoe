import numpy as np
import random

def print_board(board):
    print("    ", end="")
    for i in range(len(board[0])):
        print(str(i) + "   ", end="")
    print("")
    for i in range(len(board)):
        print(chr(i + ord("a")) + " |", end="")
        for j in range(len(board[i])):
            if board[i][j] == 0:   
                print(" - |", end="")
            elif board[i][j] == 1:
                print(" O |", end="")
            else:
                print(" X |", end="")
        print("")

def check_board(board):
    if np.all(np.diag(board) == 1) or np.all(np.diag(board) == 2):
        return True
    
    if np.all(np.flipud(board).diagonal() == 1) or np.all(np.flipud(board).diagonal() == 2):
        return True
    
    for i in range(len(board)):
        if np.all(board[i] == 1) or np.all(board[i] == 2):
            return True

    for i in range(len(board[0])):
        if np.all(board[:, i] == 1) or np.all(board[:, i] == 2):
            return True
    
    return False

def play_game():
    board = np.zeros((3, 3))
    cells = []
    for i in range(3):
        for j in range(3):
            cells.append((i, j))

    print("Welcome to Tic-Tac-Toe! Here's your board: ")

    print_board(board)

    while(True):
        move = input("Input your cell number as [row][col] (Eg: b2): ")
        if (len(move) != 2):
            print("Incorrect response/format!")
            continue

        move_row = int(ord(move[0]) - ord("a"))
        move_col = int(move[1])
        if (move_row, move_col) in cells:
            board[move_row][move_col] = 2
            cells.remove((move_row, move_col))
        else:
            print("Incorrect reponse/format!")
            continue

        print_board(board)

        if check_board(board):
            print("You Win!")
            break
        else:
            ai_move = cells[random.randint(0, len(cells)-1)]
            print("AI move: " + chr(ai_move[0] + ord("a")) + str(ai_move[1]))
            board[ai_move[0], ai_move[1]] = 1
            print_board(board)
            cells.remove(ai_move)
            if check_board(board):
                print("You Lose!")
                break
            else:
                continue

play_game()