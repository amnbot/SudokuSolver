import pygame
import time
from threading import Thread

from pygame.time import get_ticks

board = [["5","3",".",".","7",".",".",".","."]
        ,["6",".",".","1","9","5",".",".","."]
        ,[".","9","8",".",".",".",".","6","."]
        ,["8",".",".",".","6",".",".",".","3"]
        ,["4",".",".","8",".","3",".",".","1"]
        ,["7",".",".",".","2",".",".",".","6"]
        ,[".","6",".",".",".",".","2","8","."]
        ,[".",".",".","4","1","9",".",".","5"]
        ,[".",".",".",".","8",".",".","7","9"]]

board = [["3",".","6","5",".","8","4",".","."]
        ,["5","2",".",".",".",".",".",".","."]
        ,[".","8","7",".",".",".",".","3","1"]
        ,[".",".","3",".","1",".",".","8","."]
        ,["9",".",".","8","6","3",".",".","5"]
        ,[".","5",".",".","9",".","6",".","."]
        ,["1","3",".",".",".",".","2","5","."]
        ,[".",".",".",".",".",".",".","7","4"]
        ,[".",".","5","2",".","6","3",".","."]]

pygame.font.init()

WIN_WIDTH = 450
WIN_HEIGHT = 450

BOARD_WIDTH = 9
BOARD_HEIGHT = 9

black = (0,0,0)
gray = (100,100,100)
white = (255,255,255)
screen = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
screen.fill(white)
font = pygame.font.SysFont("Arial", 25)

pygame.display.flip()

def draw_grid():
    block_size = 50

    for y in range(BOARD_WIDTH):
        for x in range(BOARD_HEIGHT):
            rect = pygame.Rect(x*block_size, y*block_size, block_size, block_size)
            bold = 2
            pygame.draw.rect(screen, gray, rect, bold)
            if (x*block_size) % 3 == 0:
                pygame.draw.line(screen, black, (x*block_size, y*block_size), (x*block_size, BOARD_HEIGHT*block_size), 7)
        if (y*block_size) % 3 == 0:
            pygame.draw.line(screen, black, (0, y*block_size), (BOARD_WIDTH*block_size, y*block_size), 7)
    pygame.draw.line(screen, black, (0, BOARD_HEIGHT*block_size), (BOARD_WIDTH*block_size, BOARD_HEIGHT*block_size), 7)

def draw_nums(board):
    block_size = 50

    for y in range(BOARD_WIDTH):
        for x in range(BOARD_HEIGHT):
            draw_num(board, y, x, block_size)
            #screen.blit(font.render(board[y][x], False, black), (x*block_size+20, y*block_size+10))

def draw_num(board, row, col, block_size):
    num = board[row][col]
    if num == ".":
        return
    text = font.render(num, False, black)
    pygame.draw.circle(screen, white, (col*block_size+25, row*block_size+25), 20)
    screen.blit(text, (col*block_size + 20, row*block_size + 10))
    #clock.tick(30)
    pygame.display.update()


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
                time.sleep(0.001)
                draw_num(board, row, col, block_size=50)
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

clock = pygame.time.Clock()
running = True
while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            quit()

    draw_grid()
    draw_nums(board)
    solve(board, 0,0)

    