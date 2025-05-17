import pygame
import fon as fn

pygame.init()
screen = pygame.display.set_mode((fn.width, fn.dlin))

pygame.display.set_caption("Tokiyskaya Chaika")

pygame.display.set_icon(pygame.image.load("car1.png"))
fon = fn.fon()
car = pygame.image.load('car2.png')
car = pygame.transform.scale(car, (110, 100))



ca = 20
co = 383
hi = 200
gi = 390
ti = 100
yi = 50
speed = 120
to_left = False
to_right = False
to_up = False
to_down = False

clock = pygame.time.Clock()

run = True
while run:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
            if event.key == pygame.K_DOWN:
                to_down = True
            if event.key == pygame.K_UP:
                to_up = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
            if event.key == pygame.K_DOWN:
                to_down = False
            if event.key == pygame.K_UP:
                to_up = False

        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if to_right:
        ca += speed
        to_right = False
    if to_left:
        ca -= speed
        to_left = False
    if to_down:
        co += speed
        to_down = False
    if to_up:
        co -= speed
        to_up = False
    fon.update()
    fon.render(screen)
    screen.blit(car, (ca, co))
    pygame.display.update()
