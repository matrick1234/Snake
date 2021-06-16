import pygame
import random 
import sys

pygame.init()

clock = pygame.time.Clock()
speed = 5 
score =0 
AppleSprite = pygame.sprite.Group()

class Snake():
    def __init__(self):
        self.direction = "East" 
        self.position = (300,200)
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
        if pygame.sprite.spritecollideany(snake, AppleSprite):
        #self.position == applePos:
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

        
    def getHeadPos(self):
        return self.position

    def getBody(self):
        return self.head

class Apple(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load("C:\Users\Patri\OneDrive\Desktop\Computer Science\Snake\Bruh.png"),(40,40))
        self.image_init = self.image
        self.rect = self.image.get_rect()
        self.rect.centerx = random.randint(50,450)
        self.rect.centery=random.randint(50,450)
        self.position = (self.rect.centerx,self.rect.centery)
        self.AppleOnScreen = True

    def spawnApple(self):
        if self.AppleOnScreen == False:
            (self.rect.centerx,self.rect.centery) = [random.randint(10,490), random.randint(10,490)]
            self.AppleOnScreen = True
        return (self.rect.centerx,self.rect.centery)

    def setAppleOnScreen(self,b):  
        self.AppleOnScreen = b

res = (500,500)
screen = pygame.display.set_mode(res)
snake = Snake()
Apple = Apple()

def Lose():
    pygame.quit()
    sys.exit()

AppleSprite.add(Apple)
#all_sprites_list.add(Apple)

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

    for pos in snake.getBody():
        pygame.draw.rect(screen, pygame.Color(0,255,0),pygame.Rect(pos[0], pos[1], 30, 30))
    
    if(snake.move(Apple.SpawnApple)==1):
        score += 1
        Apple.setAppleOnScreen(False)

    screen.fill(pygame.Color(255,255,255))

    AppleSprite.update()
    AppleSprite.draw(screen)
    pygame.display.flip()

    if (snake.Death()==1):#
        Lose()
    pygame.display.set_caption("Snake. Score: " + str(score))
    pygame.display.update()
    clock.tick(30)