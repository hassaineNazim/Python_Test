import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Pygame test")
clock = pygame.time.Clock()
test_font = pygame.font.Font(None, 50)

skySurface = pygame.image.load("graphic/sky.jpg")
herbeSurface = pygame.image.load("graphic/backgrounds.png")
textSurface = test_font.render("Hello World", False, "red")



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(skySurface, (0, 0))
    screen.blit(herbeSurface, (0, 300))
    screen.blit(textSurface, (100, 100))
    
    pygame.display.update()
    clock.tick(60)


