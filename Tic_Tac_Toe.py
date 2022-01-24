import pygame, random
import math
import numpy as np
import sys
from tkinter import *

white = (255, 255, 255)
Red = (255, 0, 0)
Yellow = (255, 255, 0)
Black = (0, 0, 0)
Green = (0, 255, 0)
row_count = 3
column_count = 3

withdraw = False

box = 100

ply1 = ""
ply2 = ""

root = Tk()
root.title('Dialog Box')
root.geometry("400x200")

def create_board():
    board = np.zeros((row_count, column_count))
    return board

def draw_board(board):
    for c in range(column_count):
        for r in range(row_count):
            pygame.draw.aaline(screen, white, (0, 100), (300, 100))
            pygame.draw.aaline(screen, white, (0, 200), (300, 200))
            pygame.draw.aaline(screen, white, (0, 300), (300, 300))
            pygame.draw.aaline(screen, white, (0, 400), (300, 400))
            pygame.draw.aaline(screen, white, (0, 100), (0, 400))
            pygame.draw.aaline(screen, white, (100, 100), (100, 400))
            pygame.draw.aaline(screen, white, (200, 100), (200, 400))
            pygame.draw.aaline(screen, white, (299, 100), (299, 400))

    pygame.display.update()

def drop_piece(board, piece, row, column):
    if board[row][column] == 0:
        board[row][column] = piece

    row_w = (column*100) + 35
    column_h = (row*100) + 125

    if board[row][column] == 1:
        font = pygame.font.SysFont("monospace", 50)
        img = font.render("X", 1, Red)
        screen.blit(img, (int(row_w), int(column_h)))
    elif board[row][column] == 2:
        font = pygame.font.SysFont("monospace", 50)
        img = font.render("O", 1, Yellow)
        screen.blit(img, (int(row_w), int(column_h)))

def winning_move(board, piece):
    #Loop for Checking winning condition horizontally
    for row in range(row_count):
        if (board[row][0] == piece) and (board[row][1] == piece) and (board[row][2] == piece):
            return True

    #Loop for Checking winning condition vertically
    for column in range(column_count):
        if (board[0][column] == piece) and (board[1][column] == piece) and (board[2][column] == piece):
            return True
        
    #Loop for Checking winning condition in positive slope
    if (board[2][0] == piece) and (board[1][1] == piece) and (board[0][2] == piece):
            return True

    #Loop for Checking winning condition in negative slope
    if (board[0][0] == piece) and (board[1][1] == piece) and (board[2][2] == piece):
            return True

def is_draw(board, row, col):
    if board.min()!=0:
        return True

def ask_quit_or_playagain(piece, withdraw):
    if withdraw == 1:
        if piece == 1:
            my_label = Label(root, text="Player 1 wins!!! Do you want to play again?")
            my_label.grid(row=0, column=0, pady=30, padx=10, sticky="wens")
            button_1 = Button(root, text="Quit", command=quit_)
            button_1.grid(row=1, column=1, padx=10, pady=10)
            button_2 = Button(root, text="Play again", command=play_again)
            button_2.grid(row=1, column=2, padx=10, pady=10)
            root.deiconify()
            root.mainloop()

        elif piece == 2:
            my_label = Label(root, text="Player 2 wins!!! Do you want to play again?")
            my_label.grid(row=0, column=0, pady=30, padx=10, sticky="wens")
            button_1 = Button(root, text="Quit", command=quit_)
            button_1.grid(row=1, column=1, padx=10, pady=10)
            button_2 = Button(root, text="Play again", command=play_again)
            button_2.grid(row=1, column=2, padx=10, pady=10)
            root.deiconify()
            root.mainloop()

        else:
            my_label = Label(root, text="It's a draw!!! Do you want to play again?")
            my_label.grid(row=0, column=0, pady=30, padx=10, sticky="wens")
            button_1 = Button(root, text="Quit", command=quit_)
            button_1.grid(row=1, column=1, padx=10, pady=10)
            button_2 = Button(root, text="Play again", command=play_again)
            button_2.grid(row=1, column=2, padx=10, pady=10)
            root.deiconify()
            root.mainloop()
    else:
        
        if piece == 1:
            my_label = Label(root, text="Player 1 wins!!! Do you want to play again?")
            my_label.grid(row=0, column=0, pady=30, padx=10, sticky="wens")
            button_1 = Button(root, text="Quit", command=quit_)
            button_1.grid(row=1, column=1, padx=10, pady=10)
            button_2 = Button(root, text="Play again", command=play_again)
            button_2.grid(row=1, column=2, padx=10, pady=10)
            root.mainloop()

        elif piece == 2:
            my_label = Label(root, text="Player 2 wins!!! Do you want to play again?")
            my_label.grid(row=0, column=0, pady=30, padx=10, sticky="wens")
            button_1 = Button(root, text="Quit", command=quit_)
            button_1.grid(row=1, column=1, padx=10, pady=10)
            button_2 = Button(root, text="Play again", command=play_again)
            button_2.grid(row=1, column=2, padx=10, pady=10)
            root.mainloop()

        else:
            my_label = Label(root, text="It's a draw!!! Do you want to play again?")
            my_label.grid(row=0, column=0, pady=30, padx=10, sticky="wens")
            button_1 = Button(root, text="Quit", command=quit_)
            button_1.grid(row=1, column=1, padx=10, pady=10)
            button_2 = Button(root, text="Play again", command=play_again)
            button_2.grid(row=1, column=2, padx=10, pady=10)
            root.mainloop()

def quit_():
    gameover = True
    play_again_ = 0
    root.destroy()
    pygame.display.quit()
    sys.exit()

def play_again():
    root.withdraw()
    withdraw = True

    pygame.init()
    pygame.display.set_caption('Tic Tac Toe V0.1')

    width = 300
    height = 401
    size = (width, height)
    screen = pygame.display.set_mode(size)

    board = create_board()
    print(board)
    draw_board(board)

    gameover = False
    turn = random.randint(0,1)
    myfont = pygame.font.SysFont("monospace", 25)

    while not gameover:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            pos = pygame.mouse.get_pos()
            
            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, Black, (0, 0, 300, 100))
                if turn == 0:
                    label = myfont.render("Player 1's turn!!", 1, Red)
                    screen.blit(label, (5, 10))
                                
                else:
                    label = myfont.render("Player 2's turn!!", 1, Red)
                    screen.blit(label, (5, 10))
            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                posx = event.pos[0]
                posy = event.pos[1]

                if posy>100 and posy<400:
                    posx = event.pos[0]
                    posy = event.pos[1]
                    col = int(math.floor(posx/100))
                    row = int(math.floor(posy/100)) - 1
                
                    if turn == 0:
                        drop_piece(board, 1, row, col)
                        print(board)

                        if winning_move(board, 1):
                            pygame.draw.rect(screen, Black, (0, 0, 300, 100))
                            label = myfont.render("Player 1 wins!!", 1, Red)
                            screen.blit(label, (5, 10))
                            draw_board(board)
                            ask_quit_or_playagain(1, withdraw)

                        if is_valid_move(board, row, col, 1):
                            turn+=1
                            turn%=2
                        
                    elif turn == 1:
                        drop_piece(board, 2, row, col)
                        print(board)

                        if winning_move(board, 2):
                            pygame.draw.rect(screen, Black, (0, 0, 300, 100))
                            label = myfont.render("Player 2 wins!!", 1, Red)
                            screen.blit(label, (5, 10))
                            draw_board(board)
                            ask_quit_or_playagain(2, withdraw)

                        if is_valid_move(board, row, col, 2):
                            turn+=1
                            turn%=2
                    draw_board(board)

                    if is_draw(board, row, col):
                        pygame.draw.rect(screen, Black, (0, 0, 300, 100))
                        label = myfont.render("It's a draw!!", 1, Red)
                        screen.blit(label, (5, 10))
                        ask_quit_or_playagain(0, withdraw)
            pygame.display.update()
    
def is_valid_move(board, row, column, piece):
    if board[row][column] == piece:
        return True


def game(turn):
    while not gameover:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()
            pos = pygame.mouse.get_pos()
            
            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, Black, (0, 0, 300, 100))

                if turn == 0:
                    label = myfont.render("Player 1's turn!!", 1, Red)
                    screen.blit(label, (5, 10))
                else:
                    label = myfont.render("Player 2's turn!!", 1, Red)
                    screen.blit(label, (5, 10))
            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                posx = event.pos[0]
                posy = event.pos[1]

                if posy>100 and posy<400:                        
                    posx = event.pos[0]
                    posy = event.pos[1]
                    col = int(math.floor(posx/100))
                    row = int(math.floor(posy/100)) - 1
                
                    if turn == 0:
                        drop_piece(board, 1, row, col)
                        print(board)

                        if winning_move(board, 1):
                            pygame.draw.rect(screen, Black, (0, 0, 300, 100))
                            label = myfont.render("Player 1 wins!!", 1, Red)
                            screen.blit(label, (5, 10))
                            draw_board(board)
                            ask_quit_or_playagain(1, withdraw)

                        if is_valid_move(board, row, col, 1):
                            turn+=1
                            turn%=2

                    elif turn == 1:
                        drop_piece(board, 2, row, col)
                        print(board)

                        if winning_move(board, 2):
                            pygame.draw.rect(screen, Black, (0, 0, 300, 100))
                            label = myfont.render("Player 2 wins!!", 1, Red)
                            screen.blit(label, (5, 10))
                            draw_board(board)
                            ask_quit_or_playagain(2, withdraw)

                        if is_valid_move(board, row, col, 2):
                            turn+=1
                            turn%=2
                    draw_board(board)
                    
                    if is_draw(board, row, col):
                        pygame.draw.rect(screen, Black, (0, 0, 300, 100))
                        label = myfont.render("It's a draw!!", 1, Red)
                        screen.blit(label, (5, 10))
                        ask_quit_or_playagain(0, withdraw)
            pygame.display.update()

pygame.init()
pygame.display.set_caption('Tic Tac Toe V0.2')

width = 300
height = 401
size = (width, height)
screen = pygame.display.set_mode(size)

board = create_board()
print(board)
draw_board(board)

gameover = False
turn = 0
myfont = pygame.font.SysFont("monospace", 25)
pygame.display.update()

game(random.randint(0,1))