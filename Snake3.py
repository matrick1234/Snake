import pygame
import random 
import sys
import time
pygame.init()

#Snake is the player controlled entity
class Snake():
    def __init__(self):
        self.direction = "East" 
        self.position = [300,200]
        self.head = [[100,50],[90,50],[80,50]]
        self.Turning = self.direction
        self.r = (random.randint(0,255))
        self.g = (random.randint(0,255))
        self.b = (random.randint(0,255))

    #This is to stop the player from being able to turn 180 degrees
    def Turning(self,turn):
        if turn == "East" and not self.direction == "West":
            self.direction = "East" 
        if turn == "West" and not self.direction == "East":
            self.direction = "West" 
        if turn == "North" and not self.direction == "South":
            self.direction = "North" 
        if turn == "South" and not self.direction == "North":
            self.direction = "South"   
   
    #This type of movement so the snake is moving constantly and the user only controls when to turn
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
        
    #I made the outer bounds that the snake can travel 10 less then the actual border so it works better with the snake hitbox
    def Death(self):
        if self.position[0] > 490 or self.position[0] < 0:
            return 1 
        elif self.position[1] > 490 or self.position[1] <0:
            return 1 
        for snakeBody in self.head[1:]:
            if self.position == snakeBody:
                return 1
        return 0

    #So the snakes body can be called upon
    def getHead(self):
        return self.head

#Apple is the "Food" that the player collects to get longer and to add score
class Apple():
    def __init__(self):
        self.position = [random.randint(50,450), random.randint(50,450)]
        self.AppleOnScreen = True

    #This is so the Apple reapears after the player hits it
    def spawnApple(self):
        if self.AppleOnScreen == False:
            self.position = [random.randint(10,490), random.randint(10,490)]
            self.AppleOnScreen = True
        return self.position

    #This is needed so after a collision to cause the above code to spawn another Apple
    def setAppleOnScreen(self):  
        self.AppleOnScreen = False

#These are the Variables that need to be defined     
speed = 5
score = 0 
res = (500,500)
screen = pygame.display.set_mode(res)
fps = pygame.time.Clock()
#This is to make the classes variables to be called upon
snake = Snake()
Apple = Apple()

#A definition to call upon which will close the game
def Lose():
    pygame.quit()
    sys.exit()


#The Loop which runs the game 
while True: 
    #So the game can be closed with the ESCAPE button and so it closes completely 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Lose()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Lose()

    #This defines pygame.key.get_pressed so the user can control the Snake
    keysPressed=pygame.key.get_pressed()
    
    #This allows the user to use the WASD keys in order to steer the snake
    if keysPressed[ord('w')]:
        snake.direction="North"
    if keysPressed[ord('s')]:
        snake.direction="South"
    if keysPressed[ord('d')]:
        snake.direction="East"
    if keysPressed[ord('a')]:
        snake.direction="West"
    
    #This is used to be able to call upon a new Apple being created
    ApplePos = Apple.spawnApple()
    
    #When the snake collides with an apple the score will be incresead, the apple will appear in a new random location and the snake will change to a new random color
    if(snake.move(ApplePos)==1):
        score += 1
        Apple.setAppleOnScreen()
        snake.r = (random.randint(0,255))
        snake.g = (random.randint(0,255))
        snake.b = (random.randint(0,255))

        
    #Fills the screen with a white background
    screen.fill(pygame.Color(255,255,255))
    
    #Draws the snake
    for pos in snake.getHead():
        pygame.draw.rect(screen, pygame.Color(snake.r,snake.g,snake.b),pygame.Rect(pos[0], pos[1], 10, 10))
    
    #Draws the Apple
    pygame.draw.rect(screen, pygame.Color(255,0,0), pygame.Rect(ApplePos[0],ApplePos[1],10,10))

    #Causes the game to stop if the Snake collides with the walls or itself
    if (snake.Death()==1):
        Lose()
    
    #Adds the caption "Snake" along with the players score
    pygame.display.set_caption("Snake. Score: " + str(score))
    
    #Refreshes the screen
    pygame.display.update()
    
    #Sets the frames per second to 24
    fps.tick(24)