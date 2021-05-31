<<<<<<< HEAD
import pygame
import random
import sys 
pygame.init()
all_sprites_list = pygame.sprite.Group()
clock = pygame.time.Clock()
speed = 5
score = 0
#AppleImg = 

class Snake():
    def __init__(self):
        self.direction = "East"
        self.position = [300,200]
        self.head = [[self.position[0],self.position[1]],30,30]
        #self.head = [[self.position[0],self.position[1]],[self.position[0]-10,self.position[1]],[self.position[0]-20,self.position[1]]]
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
    
    
   
    def move(self):
        if self.direction == "North":
            self.position[1] -= speed
        if self.direction == "South":
            self.position[1] += speed
        if self.direction == "East":
            self.position[0] += speed
        if self.direction == "West":
            self.position[0] -= speed
        self.head.insert(0, list(self.position))
        if self.position == Apple.position:
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
        pygame.sprite.Sprite.__init__(self)
        
        self.AppleOnScreen = True
        self.image = pygame.transform.scale(pygame.image.load("Apple.png"),(40,40))
        self.rect = self.image.get_rect()
        #self.image.fill(255, 255, 255)
        #self.image.set_colorkey(255, 255, 255)
        
        #self.width=width
        #self.height=height
        #self.color = color
        self.rect.centerx = random.randint(50,450)
        self.rect.centery=random.randint(50,450)
        self.position = (self.rect.centerx,self.rect.centery)
        #self.width = self.image.get_width()
        #self.height = self.image.get_height()

#Possible, change randint to different variation
    def spawnApple(self):
        if self.AppleOnScreen == False:
            (self.rect.centerx,self.rect.centery) = [random.randint(10,490), random.randint(10,490)]
            self.AppleOnScreen = True
        return (self.rect.centerx,self.rect.centery)

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

all_sprites_list.add(Apple)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Lose()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Lose()
    keysPressed=pygame.key.get_pressed()
    if keysPressed[ord('w')]:
        snake.direction="North"
    if keysPressed[ord('s')]:
        snake.direction="South"
    if keysPressed[ord('d')]:
        snake.direction="East"
    if keysPressed[ord('a')]:
        snake.direction="West"
    applePos = Apple.spawnApple()

    
    
    screen.fill(pygame.Color(225,225,225))
    for pos in snake.getBody():
        bodyPiece=pygame.draw.rect(screen, pygame.Color(0,255,0),pygame.Rect(pos[0], pos[1], 20, 20))
        if pygame.Rect.colliderect(bodyPiece,Apple.rect) == True:
            score += 1
            Apple.setFoodOnScreen(False)
            snake.head.append([snake.position[0]-10,snake.position[1]])
            #len(snake.head)*10
            #
    #pygame.draw.rect(screen, pygame.Color(255,0,0),pygame.Rect(applePos[0], applePos[1],40,40))
    #pygame.draw.rect(screen, Apple.color, pygame.Rect(applePos[0],applePos[1],Apple.width, Apple.height))
    snake.move()
    all_sprites_list.update()
    all_sprites_list.draw(screen)
    pygame.display.flip()
    #pygame.draw.rect(screen, color, [applepos[0], applepos[1], width, height])
    if (snake.Death()==1):
        Lose()
    pygame.display.set_caption("Snake. Score: " + str(score))
    #pygame.display.update()
=======from FakeSnake import gameOver
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
>>>>>>> 50ecc376be924da692b2b9be5fa567ae66fff4ac
    clock.tick(30)