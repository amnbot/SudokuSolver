from collections import defaultdict


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

def is_valid(board, row, col, box) -> bool:
    

    for i in range(9):
        for j in range(9):
            num = board[i][j]

            if num == '.':
                continue

            b = (i//3)*3 + (j//3)
            
            if num in row[i] or num in col[j] or num in box[b]:
                return False

            row[i].add(num)
            col[j].add(num)
            box[b].add(num)

    return True


def solve(board, i, j, row, col, box, digit):
    num = board[i][j]
    b = (i//3)*3 + (j//3)

    if digit in row[i] or digit in col[j] or digit in box[b]:
        return
    else:
        board[i][j] = digit

    for i in range(9):
        for j in range(9):
            if num == '.':
                solve(board, i, j, row, col, box, i)


print(is_valid(board, row, col, box))

solve(board, 0, 2, row, col, box, 1)

for i in range(9):
    row = ""
    for j in range(9):
        row += str(board[i][j])
    print(row)