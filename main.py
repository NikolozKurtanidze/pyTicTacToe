from this import d
from time import sleep
from turtle import color, pos, screensize
import pygame, os

pygame.init()

white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 0, 128)

font = pygame.font.Font('freesansbold.ttf', 100)
x_wins = font.render('X Wins!', True, green, blue)
o_wins = font.render('O Wins!', True, green, blue)
draw_end = font.render('Draw!', True, green, blue)

move = 1
WIDTH, HEIGHT = 601, 601
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('pyTicTacToe')
pygame.display.set_icon(pygame.image.load(os.path.join('Assets', 'o.png')))
X = pygame.image.load(os.path.join('Assets', 'o.png'))
O = pygame.image.load(os.path.join('Assets', 'x.png'))

def draw(board):
    WIN.blit(pygame.image.load(os.path.join('Assets', 'background.png')), (0, 0))
    if board[0] == 0:
        WIN.blit(O, (20, 20))
    if board[0] == 1:
        WIN.blit(X, (20, 20))
    if board[1] == 0:
        WIN.blit(O, (210, 20))
    if board[1] == 1:
        WIN.blit(X, (210, 20))
    if board[2] == 0:
        WIN.blit(O, (400, 20))
    if board[2] == 1:
        WIN.blit(X, (400, 20))
    if board[3] == 0:
        WIN.blit(O, (20, 210))
    if board[3] == 1:
        WIN.blit(X, (20, 210))
    if board[4] == 0:
        WIN.blit(O, (210, 210))
    if board[4] == 1:
        WIN.blit(X, (210, 210))
    if board[5] == 0:
        WIN.blit(O, (400, 210))
    if board[5] == 1:
        WIN.blit(X, (400, 210))
    if board[6] == 0:
        WIN.blit(O, (20,400))
    if board[6] == 1:
        WIN.blit(X, (20,400))
    if board[7] == 0:
        WIN.blit(O, (210, 400))
    if board[7] == 1:
        WIN.blit(X, (210, 400))
    if board[8] == 0:
        WIN.blit(O, (400, 400))
    if board[8] == 1:
        WIN.blit(X, (400, 400))
    pygame.display.update()

def check_if_win(board, x):
    if board[0] == x and board[1] == x and board[2] == x:
        return True
    if board[0] == x and board[3] == x and board[6] == x:
        return True
    if board[0] == x and board[4] == x and board[8] == x:
        return True
    if board[2] == x and board[4] == x and board[6] == x:
        return True
    if board[3] == x and board[4] == x and board[5] == x:
        return True
    if board[6] == x and board[7] == x and board[8] == x:
        return True
    if board[1] == x and board[4] == x and board[7] == x:
        return True
    if board[2] == x and board[5] == x and board[8] == x:
        return True
def switch():
    global move
    if move == 1:
        move = 0
        return    
    elif move == 0:
        move = 1
        return

def end(x):
    while True:
        WIN.fill(white)
        if x == 0:
            WIN.blit(x_wins, x_wins.get_rect())
        elif x == 1:
            WIN.blit(o_wins, o_wins.get_rect())
        elif x == -1:
            WIN.blit(draw_end, draw_end.get_rect())
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                main()

def main():
    run = True
    mouse_pos = pygame.mouse.get_pos
    board = [-1, -1, -1,
             -1, -1, -1,
             -1, -1, -1]
    while run:
        for event in pygame.event.get():
            draw(board)
            if check_if_win(board, 0):
                end(0)
            if check_if_win(board, 1):
                end(1)
            if -1 not in board:
                end(-1)
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos_x = pygame.mouse.get_pos()[0]
                pos_y = pygame.mouse.get_pos()[1]
                if pos_x in range(210) and pos_y in range(210) and board[0] == -1:
                    board[0] = move
                    switch()
                elif pos_x in range(210, 390) and pos_y in range(210) and board[1] == -1:
                    board[1] = move
                    switch()
                elif pos_x in range(390, 610) and pos_y in range(210) and board[2] == -1:
                    board[2] = move
                    switch()
                elif pos_x in range(210) and pos_y in range(205, 390) and board[3] == -1:
                    board[3] = move
                    switch()
                elif pos_x in range(205, 390) and pos_y in range(205, 390) and board[4] == -1:
                    board[4] = move
                    switch()
                elif pos_x in range(390, 601) and pos_y in range(205, 390) and board[5] == -1:
                    board[5] = move
                    switch()
                elif pos_x in range(205) and pos_y in range(390, 601) and board[6] == -1:
                    board[6] = move
                    switch()
                elif pos_x in range(205, 390) and pos_y in range(390, 601) and board[7] == -1:
                    board[7] = move
                    switch()
                elif pos_x in range(390, 601) and pos_y in range(390, 601) and board[8] == -1:
                    board[8] = move
                    switch()

                


if __name__ == "__main__":
    main()