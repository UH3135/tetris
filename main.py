# 행 열 크기를 constants로 부터 불러옴
# 위 데이터를 이용하여 width와 height 계산

# 기본적인 화면 띄우기
import pygame
from constants.board import WIDTH, HEIGHT

# pygame 초기화
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

    pygame.display.flip()

    # 60FPS
    clock.tick(60) 
pygame.quit()