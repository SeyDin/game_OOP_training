import pygame

from entities.figures.square import Square
from entities.looks.square_look import SquareLook
from entities.movers import DiagonalMover

WIDTH = 720
HEIGHT = 480
FPS = 30

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (0, 255, 255)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
screen.fill(BLACK)

sl = SquareLook(50, YELLOW, screen)
sq = Square(50, 50, sl)
sq.draw()

pygame.display.update()

dm = DiagonalMover(sq)

running = True
while running:
    screen.fill(BLACK)

    dm.move()

    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()

pygame.quit()
