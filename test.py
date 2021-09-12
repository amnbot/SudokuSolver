
board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

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
                if(solve(board, row, col + 1)):
                    return True

            board[row][col] = "."
    else:
       if (solve(board, row, col + 1)):
           return True

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

solve(board, 0,0)

print_board(board)