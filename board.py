import pygame
pygame.init()

screenWidth = 1000
screenLength = 800
color = (250,250,250)
screen = pygame.display.set_mode((screenWidth, screenLength))


run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    screen.fill(color)
    pygame.display.flip()
pygame.quit()
