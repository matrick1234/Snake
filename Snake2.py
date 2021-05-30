from FakeSnake import gameOver
import pygame
import random
import sys 
pygame.init()

clock = pygame.time.Clock()
speed = 5
score = 0

class Snake():
    def __init__(self):
        self.direction = "East"
        self.position = (300,200)
        #self.head = [[300,200],30,30]
        self.head = [[100,50],[90,50],[80,50]]
        self.Turning = self.direction

    def Turning(self,turn):
        if turn == "East" and not self.direction == "West":
            self.direction = "East" 
        if turn == "West" and not self.direction == "East":
            self.direction = "West" 
        if turn == "North" and not self.direction == "South":
            self.direction = "North" 
        if turn == "South" and not self.direction == "North":
            self.direction = "South"   
   

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
        if self.position == applePos:
            return 1 
        else:
            self.head.pop()
            return 0

    def Death(self):
        if self.position[0] > 490 or self.position[0] < 0:
            return 1 
        elif self.position[1] > 490 or self.position[1] <0:
            return 1 
        for snakeBody in self.head[1:]:
            if self.position == snakeBody:
                return 1
        return 0

    def getBody(self):
        return self.head

    def getHeadPos(self):
        return self.position



class Apple(pygame.sprite.Sprite): 
    def __init__(self):
        self.position = [random.randrange(1,50)*10, random.randrange(1,50)*10]
        self.AppleOnScreen = True

#Possible, change randint to different variation
    def spawnApple(self):
        if self.AppleOnScreen == False:
            self.position = [random.randrange(1,50)*10, random.randrange(1,50)*10]
            self.AppleOnScreen = True
        return self.position

    def setFoodOnScreen(self,b):
        self.AppleOnScreen = b

res = (500,500)
screen = pygame.display.set_mode(res) 
snake = Snake()
Apple = Apple()

def Lose():
    pygame.quit()
    sys.exit()

#fps = 24

   

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Lose()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                snake.Turning("North")
            if event.key == pygame.K_DOWN:
                snake.Turning("South")
            if event.key == pygame.K_RIGHT:
                snake.Turning("East")
            if event.key == pygame.K_LEFT:
                snake.Turning("West")
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
    
    applePos = Apple.spawnApple()

    if (snake.position==applePos):
        score += 1
        Apple.setFoodOnScreen(False)
    
    screen.fill(pygame.Color(225,225,225))
    for pos in snake.getBody():
        pygame.draw.rect(screen, pygame.Color(0,255,0),pygame.Rect(pos[0], pos[1], 50, 50))
    pygame.draw.rect(screen, pygame.Color(255,0,0),pygame.Rect(applePos[0], applePos[1],40,40))
    if (snake.Death()==1):
        Lose()
    pygame.display.set_caption("Snake. Score: " + str(score))
    pygame.display.update()
    clock.tick(30)