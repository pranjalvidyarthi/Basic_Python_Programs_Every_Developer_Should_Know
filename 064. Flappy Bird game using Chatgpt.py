import pygame
import random

# Initialize pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 400, 600
BLOCK_SIZE = 30
GRAVITY = 0.5
JUMP_STRENGTH = -5
PIPE_WIDTH = 60
PIPE_GAP = 150
PIPE_SPEED = 3
FONT = pygame.font.Font(None, 36)

# Colors
GREEN = (0, 200, 0)
WHITE = (255, 255, 255)
RED = (200, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Block")

# Block class
class Block:
    def __init__(self):
        self.x = 100
        self.y = HEIGHT // 2
        self.velocity = 0

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity
        if self.y > HEIGHT - BLOCK_SIZE:
            self.y = HEIGHT - BLOCK_SIZE
            self.velocity = 0

    def jump(self):
        self.velocity = JUMP_STRENGTH

    def draw(self):
        pygame.draw.rect(screen, WHITE, (self.x, self.y, BLOCK_SIZE, BLOCK_SIZE))

# Pipe class
class Pipe:
    def __init__(self, x):
        self.x = x
        self.height = random.randint(100, 400)

    def update(self):
        self.x -= PIPE_SPEED
        if self.x < -PIPE_WIDTH:
            self.x = WIDTH
            self.height = random.randint(100, 400)

    def draw(self):
        pygame.draw.rect(screen, WHITE, (self.x, 0, PIPE_WIDTH, self.height))
        pygame.draw.rect(screen, WHITE, (self.x, self.height + PIPE_GAP, PIPE_WIDTH, HEIGHT))

# Game loop
running = True
clock = pygame.time.Clock()

def start_screen():
    screen.fill(GREEN)
    text = FONT.render("Press SPACE to Start", True, WHITE)
    screen.blit(text, (WIDTH//2 - 100, HEIGHT//2))
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                waiting = False

def end_screen():
    screen.fill(GREEN)
    text = FONT.render("Game Over! Press R to Restart", True, WHITE)
    screen.blit(text, (WIDTH//2 - 150, HEIGHT//2))
    pygame.display.flip()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                waiting = False

while running:
    start_screen()
    block = Block()
    pipes = [Pipe(WIDTH + i * 200) for i in range(3)]
    
    playing = True
    while playing:
        screen.fill(GREEN)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    block.jump()
        
        block.update()
        for pipe in pipes:
            pipe.update()
            if block.x < pipe.x + PIPE_WIDTH and block.x + BLOCK_SIZE > pipe.x:
                if block.y < pipe.height or block.y + BLOCK_SIZE > pipe.height + PIPE_GAP:
                    playing = False
            pipe.draw()
        
        block.draw()
        pygame.display.flip()
        clock.tick(30)
    
    end_screen()
072.