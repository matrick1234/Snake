
import pygame
import random
import sys
pygame.init()


#running = True 
clock = pygame.time.Clock()
speed = 5
score = 0


#snakePos = [300,200]
#applePos = [500,200]
#applePos = [random.randint(10, 590), random.randint(10, 390)]

#def EatRect(applePos, snakePos):
    #if applePos[0] <= snakePos[0]:
        #running = False #applePos[0] >= snakePos[0] and applePos[0] <= snakePos[0] + 30:
#player = Snake()        


snake = Snake()
Apple = Apple()

res = (500,500)
fps = 24

screen = pygame.display.set_mode(res)    

while True:
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
                pygame.quit()
    
    applePos = Apple.spawnApple()

    if (snake.position==applePos):
        score += 1
        Apple.setFoodOnScreen(False)
    
    screen.fill(pygame.Color(225,225,225))
    for pos in snake.getBody():
        pygame.draw.rect(screen, pygame.Color(0,255,0),pygame.Rect(pos[0], pos[1], 30, 30))
    pygame.draw.rect(screen, pygame.Color(255,0,0),pygame.Rect(applePos[0], applePos[1],20,20))
    if (snake.Death()==1):
        pygame.quit()
        quit()
    pygame.display.set_caption("Snake. Score: " + str(score))

    pygame.display.update()
    
    clock.tick.tick_busy_loop(30)
    #fps.tick(24)




            
            
    #if not appleOnScreen:

pygame.quit()


class Snake(pygame.sprite.Sprite):
    def __init__(self):
        #pygame.sprite.Sprite.__init__(self)
        self.score = 0
        self.direction = "East"
        self.position = (300,200)
        #self.x = 300
        #self.y = 200
        self.head = [[100,50],[90,50],[80,50]]
        self.move = self.direction
        #self.image = pygame.transform.scale(pygame.image.load("snake.png"),(30,30))
        #self.image_init = self.image
        #self.rect = self.image.get_rect()
    
    
    def move(self, applePos):
        if self.direction == "North":
            self.position[1] -= speed
        if self.direction == "South":
            self.position[1] += speed
        if self.direction == "East":
            self.position[0] += speed
        if self.direction == "West":
            self.position[0] -= speed
        self.head.insert(0, list(self.position))
        #self.head.insert(0,self.position)
        if self.position == applePos:
            return 1 
        else:
            self.head.pop()
            return 0

    def Death(self):
        if self.position[0] > 590 or self.position[0] < 0:
            return 1 
        elif self.position[1] > 390 or self.position[1] <0:
            return 1 
        for snakeBody in self.head[1:]:
            if self.position == snakeBody:
                return 1
        return 0

    def getBody(self):
        return self.head

    def getHeadPos(self):
        return self.position
    
    #def SnakeHead(self):
        
    #def draw():
        




class Apple: 
    def __init__(self):
        self.position = [random.randint(10, 490), random.randint(10, 490)]
        self.AppleOnScreen = True
    



    #def draw(self):
        
        #pygame.draw.rect(screen,(0,0,255),appleRect)
    

    def spawnApple(self):
        if self.AppleOnScreen == False:
            self.position = [random.randint(10,490), random.randint(10,490)]
            self.AppleOnScreen = True
        return self.position

    def setFoodOnScreen(self,b):
        self.AppleOnScreen = b
            
#class Game: 
    
    #def AppleEat(self, applePos[1], applePos[0], snakePos[1], snakePos[0]):
        #if snakePos[0] >= applePos[0] and snakePos[0] <= applePos[0] + 30:
            #if snakePos[1] >= applePos[1] and snakePos[1] >= snakePos[1] +30:
                #return True    
        #return False 