import random
import numpy as np
from time import sleep

def makegrid():
    return(
        np.array([[0,0,0],
                 [0,0,0],
                 [0,0,0]]))

def emptyboard(grid):
    length=[]
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j]==0:
                length.append((i,j))

    return length


def playerloc(grid,player):
    selectfrom=emptyboard(grid)
    location=random.choice(selectfrom)
    grid[location]=player
    return grid

def row_win(grid, player):
    for row in grid:
        if all([cell == player for cell in row]):
            return True
    return False

def colwin(grid,player):
    for col in grid:
        if all([cell == player for cell in col]):
            return True
    return False


def diag_win(grid, player):
    win = True
    y = 0
    for x in range(len(grid)):
        if grid[x][x] != player:
            win = False
    if win:
        return win
    win = True
    if win:
        for x in range(len(grid)):
            y = len(grid) - 1 - x
            if grid[x][y] != player:
                win = False
    return win

def check(board):
    winner = 0

    for player in [1, 2]:
        if (row_win(board, player) or colwin(board, player) or diag_win(board, player)):
            winner = player

    if np.all(board != 0) and winner == 0:
        winner = -1
    return(winner)


def letsgo():
    board, winner, count = makegrid(), 0, 1
    print(board)
    sleep(2)
    while winner == 0:
        for player in [1, 2]:
            board = playerloc(board, player)
            print(str(count) + "round")
            print(board)
            sleep(2)
            
            count += 1
            winner = check(board)
            if winner != 0:
                break
    return(winner)

if str(letsgo())==-1:
    print("Its a tie!")

else:
    print("Yayyyy " + str(letsgo())+ " won!")





    




