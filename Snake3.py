import pygame
import random 
import sys
import time
pygame.init()
#SnakeColour = (random.randint(0,255),(random.randint(0,255),(random.randint(0,255))))
#r = (random.randint(0,255))
#g = (random.randint(0,255))
#b = (random.randint(0,255))

clock = pygame.time.Clock()
speed = 5
score = 0 

class Snake():
    def __init__(self):
        self.direction = "East" 
        self.position = [300,200]
        self.head = [[100,50],[90,50],[80,50]]
        self.Turning = self.direction
        self.r = (random.randint(0,255))
        self.g = (random.randint(0,255))
        self.b = (random.randint(0,255))

    def Turning(self,turn):
        if turn == "East" and not self.direction == "West":
            self.direction = "East" 
        if turn == "West" and not self.direction == "East":
            self.direction = "West" 
        if turn == "North" and not self.direction == "South":
            self.direction = "North" 
        if turn == "South" and not self.direction == "North":
            self.direction = "South"   
   

    def move(self, ApplePos):
        if self.direction == "North":
            self.position[1] -= speed
        if self.direction == "South":
            self.position[1] += speed
        if self.direction == "East":
            self.position[0] += speed
        if self.direction == "West":
            self.position[0] -= speed
        self.head.insert(0,list(self.position))
        if self.position[0] < int(Apple.position[0]) + 10 and self.position[0] > int(Apple.position[0]) -10 and self.position[1] < int(Apple.position[1]) + 10 and self.position[1] > int(Apple.position[1]) - 10:
            return 1 

        else:
            self.head.pop()
            return 0
        
    #def Colour(self,r,g,b):
        #self.r = (random.randint(0,255))
        #self.g = (random.randint(0,255))
        #self.b = (random.randint(0,255))

    def Death(self):
        if self.position[0] > 490 or self.position[0] < 0:
            return 1 
        elif self.position[1] > 490 or self.position[1] <0:
            return 1 
        for snakeBody in self.head[1:]:
            if self.position == snakeBody:
                return 1
        return 0

        
    def getHeadPos(self):
        return self.position

    def getBody(self):
        return self.head

class Apple():
    def __init__(self):
        #pygame.sprite.Sprite.__init__(self)
        #self.image = pygame.transform.scale(pygame.image.load("Bruh.png"),(20,20))
        #self.x = random.randint(50,450)
        #self.y = random.randint(50,450)
        #self.position = [self.x,self.y]
        #self.image_init = self.image
        #self.rect = self.image.get_rect()
        #self.rect.centerx = random.randint(50,450)
        #self.rect.centery=random.randint(50,450)
        #self.position = (self.rect.centerx,self.rect.centery)
        self.position = [random.randint(50,450), random.randint(50,450)]
        self.AppleOnScreen = True

    def spawnApple(self):
        if self.AppleOnScreen == False:
            self.position = [random.randint(10,490), random.randint(10,490)]
            self.AppleOnScreen = True
        return self.position

    def setAppleOnScreen(self):  
        self.AppleOnScreen = False
    
#all_sprites.add(Apple)
res = (500,500)
screen = pygame.display.set_mode(res)
snake = Snake()
Apple = Apple()
fps = pygame.time.Clock()

def Lose():
    pygame.quit()
    sys.exit()


#all_sprites_list.add(Apple)

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Lose()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Lose()
    
    #print(Apple.position, snake.position)
    
    keysPressed=pygame.key.get_pressed()
    
    if keysPressed[ord('w')]:
        snake.direction="North"
    if keysPressed[ord('s')]:
        snake.direction="South"
    if keysPressed[ord('d')]:
        snake.direction="East"
    if keysPressed[ord('a')]:
        snake.direction="West"
    #if keysPressed[ord('e')]:
        #print(Apple.position, snake.position)

    ApplePos = Apple.spawnApple()
    if(snake.move(ApplePos)==1):
        score += 1
        Apple.setAppleOnScreen()
        snake.r = (random.randint(0,255))
        snake.g = (random.randint(0,255))
        snake.b = (random.randint(0,255))

        

    screen.fill(pygame.Color(255,255,255))
    
    for pos in snake.getBody():
        pygame.draw.rect(screen, pygame.Color(snake.r,snake.g,snake.b),pygame.Rect(pos[0], pos[1], 10, 10))
    
    pygame.draw.rect(screen, pygame.Color(255,0,0), pygame.Rect(ApplePos[0],ApplePos[1],10,10))


    if (snake.Death()==1):
        Lose()
    pygame.display.set_caption("Snake. Score: " + str(score))
    pygame.display.update()
    fps.tick(24)