import pygame
import sys 
import random 
import time 

class Snake():
    def __init__(self):
        self.position = [100,50]
        self.bdy = [[100,50],[90,50],[80,50]]
        self.direction = "Right"
        self.changeDirectionTo = self.direction

    def changeDirTo(self,dir):
        if dir == "Right" and not self.direction == "Left":
            self.direction = "Right" 
        if dir == "Left" and not self.direction == "Right":
            self.direction = "Left" 
        if dir == "Up" and not self.direction == "Down":
            self.direction = "Up" 
        if dir == "Down" and not self.direction == "Up":
            self.direction = "Down"    

    def move(self,foodPos):
        if self.direction =="Right":
            self.position[0] += 5
        if self.direction =="Left":
            self.position[0] -= 5
        if self.direction =="Up":
            self.position[1] -= 5
        if self.direction =="Down":
            self.position[1] += 5 
        self.body.insert(0,list(self.position))
        if self.position == foodPos:
            return 1
        else: 
            self.body.pop()
            return 0 
    
    def checkCollision(self):
        if self.position[0] > 490 or self.position[0] < 0:
            return 1 
        elif self.position[1] > 490 or self.position[1] < 0: 
            return 1
        for bodyPart in self.body[1:]:
            if self.position == bodyPart:
                return 1 
        return 0

    def getHeadPos(self):
        return self.position
    
    def getBody(self):
        return self.body

class FoodSpawner(): 
    def __init__(self):
        self.position = [random.randrange(1,50)*10,random.randrange(1,50)*10]
        self.isFoodOnScreen =True 

    def spawnFood(self):
        if self.isFoodOnScreen == False:
            self.position = [random.randrange(1,50)*10,random.randrange(1,50)*10]
            self.isFoodOnScreen = True
        return self.position

    def setFoodOnScreen(self,b): 
        self.isFoodOnScreen = b

window = pygame.display.set_mode((500,500))
pygame.display.set_caption("WoW Snake")
fps = pygame.time.Clock()

score = 0 

snake = Snake()
FoodSpawner = FoodSpawner()

def gameOver():
    pygame.quit()
    sys.exit()

while True: 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            gameOver();
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT: 
                snake.changeDirTo("Right")
            if event.key == pygame.K_LEFT: 
                snake.changeDirTo("Left")
            if event.key == pygame.K_DOWN: 
                snake.changeDirTo("Down")
            if event.key == pygame.K_UP: 
                snake.changeDirTo("Up")
    foodPos = FoodSpawner.spawnFood()
    if(snake.move(foodPos)==1):
        score += 1 
        FoodSpawner.setFoodOnScreen(False)

    window.fill(pygame.Color(225, 225, 225))
    for pos in snake.getBody():
        pygame.draw.rect(window, pygame.Color(0,225,0),pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(window, pygame.Color(225,0,0),pygame.Rect(foodPos[0], foodPos[1], 10, 10))
    if(snake.checkCollision()==1):
        gameOver()  
    pygame.display.set_caption('wow Snake. Score: ' + str(score) )
    pygame.display.update()
    fps.tick(24)


