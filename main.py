import pygame
pygame.init()
res = (600,400)
fps = 60
screen = pygame.display.set_mode(res)
pygame.display.set_caption("Snake")
running = True 
clock = pygame.time.Clock()
speed = 10

direction = ()
snakePos = [300,200]
North = snakePos[1] += speed


while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                
            if event.key == pygame.K_UP:
                North
            if event.key == pygame.K_DOWN:
                snakePos[1] += 10
            if event.key == pygame.K_RIGHT:
                snakePos[0] += 10
            if event.key == pygame.K_LEFT:
                snakePos[0] -= 10
            if event.key == pygame.K_ESCAPE:
                running = False

    testRect = pygame.Rect(snakePos[0],snakePos[1],50,50)

    screen.fill((255,0,0))

    pygame.draw.rect(screen,(0,255,0),testRect)

    pygame.display.update()
    clock.tick(fps)

