import pygame

# pygame setup
pygame.init()
pygame.font.init()
screenx = 1080
screeny = 720
screen = pygame.display.set_mode((screenx, screeny))
clock = pygame.time.Clock()
running = True
dt = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or keys[pygame.K_e]:
            running = False
          
    # Put all code here
  
    dt = clock.tick(240) / 1000

pygame.quit()
