from collections import defaultdict
import os
import time

board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

row = defaultdict(set)
col = defaultdict(set)
box = defaultdict(set)

print("Visualize the algorithm?\nYes/No : ")
visualize = False
value = input()
if value.lower() == 'yes':
    visualize = True

def validate_initial_board(board, row, col, box) -> bool:

    for y in range(9):
        for x in range(9):
            num = str(board[y][x])
            
            if num == ".":
                continue
            
            b = (y//3)*3 + (x//3)

            if num in row[y] or num in col[x] or num in box[b]:
                return False

            row[y].add(num)
            col[x].add(num)
            box[b].add(num)

    return True

def valid_placement(board, row, col) -> bool:
    num = board[row][col]

    box = (row//3)*3 + (col//3)

    for x in range(9):
        if board[row][x] == num and x != col:
            return False
    
    for y in range(9):
        if board[y][col] == num and y != row:
            return False
    
    for y in range(9):
        for x in range(9):
            if (y//3)*3 + (x//3) == box:
                if board[y][x] == num and y != row and x != col:
                    return False

    return True
    

def solve(board, row, col) -> bool:
    if(col == len(board[row])):
        col = 0
        row += 1
    if row == len(board):
        return True

    if(board[row][col] == "."):
        for i in range(1,10):
            board[row][col] = str(i)
            #print_board(board)

            if(valid_placement(board, row, col)):
                if visualize:
                    clear()
                    print_board(board)
                if(solve(board, row, col + 1)):
                    return True

            board[row][col] = "."
    else:
       if (solve(board, row, col + 1)):
           return True

clear = lambda: os.system('cls')

def print_board(board):
    line = "-"*25
    for y in range(9):
        row = ""
        if y%3 == 0:
            print(line)
        for x in range(9):
            if (x)%3 == 0:
                row += "| "
            row += str(board[y][x]) + " "
            if x == 8:
                row += "| "
        print(row)
    print(line)

print_board(board)


solve(board, 0, 0)

print_board(board)

input()

print(validate_initial_board(board, row, col, box))