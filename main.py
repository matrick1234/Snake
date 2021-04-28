import pygame

res = (600,400)
fps = 60
screen = pygame.display.set_mode(res)
running = True 
clock = pygame.time.Clock()

while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    clock.tick(fps)
