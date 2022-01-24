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
    #Loop for Checking winning condition in row
    for row in range(row_count):
        if (board[row][0] == piece) and (board[row][1] == piece) and (board[row][2] == piece):
            return True

    #Loop for Checking winning condition in column
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

# class button():
#     def __init__(self, color, x,y,width,height, text=''):
#         self.color = color
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#         self.text = text

#     def draw(self,win,outline=None):
#         #Call this method to draw the button on the screen
#         if outline:
#             pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
#         pygame.draw.rect(win, self.color, (self.x,self.y,self.width,self.height),0)
        
#         if self.text != '':
#             font = pygame.font.SysFont('monospace', 15)
#             text = font.render(self.text, 1, (0,0,0))
#             win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

#     def isOver(self, pos):
#         #Pos is the mouse position or a tuple of (x,y) coordinates
#         if pos[0] > self.x and pos[0] < self.x + self.width:
#             if pos[1] > self.y and pos[1] < self.y + self.height:
#                 return True
            
#         return False

# def player_name():
#     if withdraw==1:
#         # for widgets in root.winfo_children():
#         #     widgets.destroy()
#         root.title("Player Names")
#         p1_label = Label(root, text="Player 1")
#         p1_label.grid(row=0, column=0, padx=20, pady=20)
#         p2_label = Label(root, text="Player 2")
#         p2_label.grid(row=1, column=0)

#         p1_name = Entry(root, width=30)
#         p1_name.grid(row=0, column=1, padx=20, pady=20)
#         p1_name.focus_set()
#         p2_name = Entry(root, width=30)
#         p2_name.grid(row=1, column=1)

#         save = Button(root,text = "Save Changes", command=lambda: save_names(p1_name.get(), p2_name.get()))
#         save.grid(row = 2, column = 1, padx=20, pady=20)
#         back = Button(root,text = "Back", command=lambda: save_names(p1_name.get(), p2_name.get()))
#         back.grid(row = 2, column = 2, pady=20)
#         root.deiconify()
#         root.mainloop()

#     else:
#         # for widgets in root.winfo_children():
#         #     widgets.destroy()
#         root.title("Player Names")

#         p1_label = Label(root, text="Player 1")
#         p1_label.grid(row=0, column=0, padx=20, pady=20)

#         p2_label = Label(root, text="Player 2")
#         p2_label.grid(row=1, column=0)

#         p1_name = Entry(root, width=30)
#         p1_name.grid(row=0, column=1, padx=20, pady=20)
#         p1_name.focus_set()

#         p2_name = Entry(root, width=30)
#         p2_name.grid(row=1, column=1)

#         save = Button(root,text = "Save Changes", command=lambda: save_names(p1_name.get(), p2_name.get()))
#         save.grid(row = 2, column = 1, padx=20, pady=20)
#         back = Button(root,text = "Back", command=lambda: save_names(p1_name.get(), p2_name.get()))
#         back.grid(row = 2, column = 2, pady=20)
#         root.deiconify()
#         root.mainloop()

# def save_names(p1, p2):
#     global ply1, ply2
#     ply1 = p1
#     ply2 = p2
#     root.withdraw()
#     game(random.randint(0,1))
#     withdraw = True
#     return

def ask_quit_or_playagain(piece, withdraw):
    if withdraw == 1:
        if piece == 1:
            # for widgets in root.winfo_children():
            #     widgets.destroy()
            # if ply1=="":
            my_label = Label(root, text="Player 1 wins!!! Do you want to play again?")
            # else:
            #     my_label = Label(root, text=str(ply1) + "wins!!! Do you want to play again?")
            my_label.grid(row=0, column=0, pady=30, padx=10, sticky="wens")
            button_1 = Button(root, text="Quit", command=quit_)
            button_1.grid(row=1, column=1, padx=10, pady=10)
            button_2 = Button(root, text="Play again", command=play_again)
            button_2.grid(row=1, column=2, padx=10, pady=10)
            root.deiconify()
            root.mainloop()

        elif piece == 2:
            # for widgets in root.winfo_children():
            #     widgets.destroy()
            # if ply2=="":
            my_label = Label(root, text="Player 2 wins!!! Do you want to play again?")
            # else:
            #     my_label = Label(root, text=str(ply2) + "wins!!! Do you want to play again?")
            my_label.grid(row=0, column=0, pady=30, padx=10, sticky="wens")
            button_1 = Button(root, text="Quit", command=quit_)
            button_1.grid(row=1, column=1, padx=10, pady=10)
            button_2 = Button(root, text="Play again", command=play_again)
            button_2.grid(row=1, column=2, padx=10, pady=10)
            root.deiconify()
            root.mainloop()

        else:
            # for widgets in root.winfo_children():
            #     widgets.destroy()
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
            # for widgets in root.winfo_children():
            #     widgets.destroy()
            # if ply1=="":
            my_label = Label(root, text="Player 1 wins!!! Do you want to play again?")
            # else:
            #     my_label = Label(root, text=str(ply1) + "wins!!! Do you want to play again?")
            my_label.grid(row=0, column=0, pady=30, padx=10, sticky="wens")
            button_1 = Button(root, text="Quit", command=quit_)
            button_1.grid(row=1, column=1, padx=10, pady=10)
            button_2 = Button(root, text="Play again", command=play_again)
            button_2.grid(row=1, column=2, padx=10, pady=10)
            root.mainloop()

        elif piece == 2:
            # for widgets in root.winfo_children():
            #     widgets.destroy()
            # if ply2=="":
            my_label = Label(root, text="Player 2 wins!!! Do you want to play again?")
            # else:
                # my_label = Label(root, text=str(ply2) + "wins!!! Do you want to play again?")
            my_label.grid(row=0, column=0, pady=30, padx=10, sticky="wens")
            button_1 = Button(root, text="Quit", command=quit_)
            button_1.grid(row=1, column=1, padx=10, pady=10)
            button_2 = Button(root, text="Play again", command=play_again)
            button_2.grid(row=1, column=2, padx=10, pady=10)
            root.mainloop()

        else:
            # for widgets in root.winfo_children():
            #     widgets.destroy()
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

    # change_name = button((0,255,0), 15, 415, 125, 25, 'Player names')
    # change_name.draw(screen, white)

    # change_theme = button((0,255,0), 155, 415, 125, 25, 'Change Theme')
    # change_theme.draw(screen, white)

    while not gameover:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            pos = pygame.mouse.get_pos()
            
            if event.type == pygame.MOUSEMOTION:
                # if change_name.isOver(pos):
                #     change_name.color = (255, 0, 0)
                #     change_name.draw(screen)
                # else: 
                #     change_name.color = (0, 255, 0)
                #     change_name.draw(screen)
                # if change_theme.isOver(pos):
                #     change_theme.color = (255, 0, 0)
                #     change_theme.draw(screen)
                # else: 
                #     change_theme.color = (0, 255, 0)
                #     change_theme.draw(screen)
                pygame.draw.rect(screen, Black, (0, 0, 300, 100))
                if turn == 0:
                    # if ply1=="":
                    label = myfont.render("Player 1's turn!!", 1, Red)
                    # else:
                    #     label = myfont.render(ply1 + "'s turn!!", 1, Red)
                    screen.blit(label, (5, 10))
                                
                else:
                    # if ply2=="":
                    label = myfont.render("Player 2's turn!!", 1, Red)
                    # else:
                    #     label = myfont.render(ply2 + "'s turn!!", 1, Red)
                    screen.blit(label, (5, 10))
            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                posx = event.pos[0]
                posy = event.pos[1]
                # if change_name.isOver(pos):
                #         player_name()
                # if change_theme.isOver(pos):
                #         print("Button was clicked")
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
                            # if ply2=="":
                            label = myfont.render("Player 1 wins!!", 1, Red)
                            # else:
                            #     label = myfont.render(ply1 + " wins!!", 1, Red)
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
                            # if ply2=="":
                            label = myfont.render("Player 2 wins!!", 1, Red)
                            # else:
                            #     label = myfont.render(ply2 + " wins!!", 1, Red)
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
                # if change_name.isOver(pos):
                #     change_name.color = (255, 0, 0)
                #     change_name.draw(screen)
                # else: 
                #     change_name.color = (0, 255, 0)
                #     change_name.draw(screen)
                # if change_theme.isOver(pos):
                #     change_theme.color = (255, 0, 0)
                #     change_theme.draw(screen)
                # else: 
                #     change_theme.color = (0, 255, 0)
                #     change_theme.draw(screen)
                pygame.draw.rect(screen, Black, (0, 0, 300, 100))
                if turn == 0:
                    # if ply1=="":
                    label = myfont.render("Player 1's turn!!", 1, Red)
                    # else:
                    #     label = myfont.render(ply1 + "'s turn!!", 1, Red)
                    screen.blit(label, (5, 10))
                                
                else:
                    # if ply2=="":
                    label = myfont.render("Player 2's turn!!", 1, Red)
                    # else:
                    #     label = myfont.render(ply2 + "'s turn!!", 1, Red)
                    screen.blit(label, (5, 10))
            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                posx = event.pos[0]
                posy = event.pos[1]
                # if change_name.isOver(pos):
                #         player_name()
                # if change_theme.isOver(pos):
                #         print("Button was clicked")
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
                            # if ply1=="":
                            label = myfont.render("Player 1 wins!!", 1, Red)
                            # else:
                            #     label = myfont.render(ply1 + " wins!!", 1, Red)
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
                            # if ply2=="":
                            label = myfont.render("Player 2 wins!!", 1, Red)
                            # else:
                            #     label = myfont.render(ply2 + " wins!!", 1, Red)
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

# change_name = button((0, 255, 0), 15, 415, 125, 25, 'Player names')
# change_name.draw(screen, white)

# change_theme = button((0, 255, 0), 155, 415, 125, 25, 'Change theme')
# change_theme.draw(screen, white)

game(random.randint(0,1))