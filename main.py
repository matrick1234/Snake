import pygame
pygame.init()
res = (600,400)
fps = 3
screen = pygame.display.set_mode(res)
pygame.display.set_caption("Snake")
running = True 
clock = pygame.time.Clock()
speed = 20
direction = "East"
snakePos = [300,200]
applePos = [500,200]

def MoveSnake(direction,speed):
    if direction == "North":
        snakePos[1] -= speed
    if direction == "South":
        snakePos[1] += speed
    if direction == "East":
        snakePos[0] += speed
    if direction == "West":
        snakePos[0] -= speed

appleRect = pygame.Rect(applePos[0],applePos[1], 20, 20)
pygame.draw.rect(screen,(0,0,0),appleRect)
    

while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                direction = "North"
            if event.key == pygame.K_DOWN:
                direction = "South"
            if event.key == pygame.K_RIGHT:
                direction = "East"
            if event.key == pygame.K_LEFT:
                direction = "West"
            if event.key == pygame.K_ESCAPE:
                running = False
            
    MoveSnake(direction,speed)
    testRect = pygame.Rect(snakePos[0],snakePos[1],30,30)

    screen.fill((255,0,0))

    pygame.draw.rect(screen,(0,255,0),testRect)

    pygame.display.update()
    clock.tick(fps)

