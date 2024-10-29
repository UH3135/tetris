# 행 열 크기를 constants로 부터 불러옴
# 위 데이터를 이용하여 width와 height 계산

# 기본적인 화면 띄우기
import pygame
from board import WIDTH, HEIGHT, board
from piece import PIECE_SIZE, Piece, colors

def draw(board: board):
    for column, l in enumerate(board.board):
            for row, val in enumerate(l):
                if val != 0:
                    pygame.draw.rect(screen, colors["red"], (row*PIECE_SIZE, column*PIECE_SIZE, PIECE_SIZE, PIECE_SIZE))


# pygame 초기화
pygame.init()
screen = pygame.display.set_mode((WIDTH*PIECE_SIZE, HEIGHT*PIECE_SIZE))
clock = pygame.time.Clock()
running = True

main = board()

while running:
    piece = Piece()
    main.add_piece(piece.get_pos())

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("white")
    draw(main)

    pygame.display.flip()

    # 60FPS
    clock.tick(60) 
pygame.quit()