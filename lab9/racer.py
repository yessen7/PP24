import pygame
import sys
import random
import time
import math
from pygame.locals import *

# Initializing
pygame.init()

# Basic settings
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
FPS = 60
SPEED = 5
SCORE = 0
COIN_SCORE = 0

# Predefined some colors
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
PINK = (255, 192, 203)

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
font_coins = pygame.font.SysFont("Verdana", 300)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("C:/Users/PROCOM/Desktop/PP24/lab9/images/AnimatedStreet.png")

# Create a pink screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
screen.fill(PINK)
pygame.display.set_caption("Racer")

FramePerSec = pygame.time.Clock()
done = False


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:/Users/PROCOM/Desktop/PP24/lab9/images/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH-40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > 600:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)


class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:/Users/PROCOM/Desktop/PP24/lab9/images/coin.png")
        self.rect = self.image.get_rect()
        self.spawn()

    def spawn(self):
        self.rect.center = (random.randint(0, SCREEN_WIDTH), random.randint(0, 300))

    def move(self):
        self.rect.move_ip(0, 5)
        if self.rect.top > SCREEN_HEIGHT:
            self.spawn()


class Coin2(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:/Users/PROCOM/Desktop/PP24/lab9/images/diamond.png")
        self.rect = self.image.get_rect()
        self.spawn()

    def spawn(self):
        self.rect.center = (random.randint(0, SCREEN_WIDTH), random.randint(0, 300))

    def move(self):
        self.rect.move_ip(0, 5)
        if self.rect.top > SCREEN_HEIGHT:
            self.spawn()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("C:/Users/PROCOM/Desktop/PP24/lab9/images/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[pygame.K_a]:
                self.rect.move_ip(-10, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[pygame.K_d]:
                self.rect.move_ip(10, 0)
        if pressed_keys[pygame.K_w] and self.rect.top > 0:
            self.rect.move_ip(0, -10)
        if pressed_keys[pygame.K_s] and self.rect.bottom < SCREEN_HEIGHT:
            self.rect.move_ip(0, 10)


# Setting up Sprites
P1 = Player()
E1 = Enemy()
C1 = Coin()
C2 = Coin2()

# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)

all_sprites = pygame.sprite.Group()
all_sprites.add(E1)
all_sprites.add(P1)

coins = pygame.sprite.Group()
coins.add(C1)

coins2 = pygame.sprite.Group()
coins2.add(C2)

# Adding a new User event
#INC_SPEED = pygame.USEREVENT + 1
#pygame.time.set_timer(INC_SPEED, 1000)

# Game Loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            pygame.quit()
            sys.exit()

    screen.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, BLACK)
    coin_scores = font_small.render(str(COIN_SCORE), True, BLACK)
    screen.blit(scores, (10, 10))
    screen.blit(coin_scores, (360, 10))

    # Moves and Re-draws all Sprites
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    for entity in coins:
        screen.blit(entity.image, entity.rect)
        entity.move()

    for entity in coins2:
        screen.blit(entity.image, entity.rect)
        entity.move()



    #for entity in coins:
        #screen.blit(entity.image, entity.rect)
        #entity.appear()

    # To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('C:/Users/PROCOM/Desktop/PP24/lab9/sounds/crash.wav').play()
        time.sleep(0.5)

        screen.fill((255, 52, 25))
        screen.blit(game_over, (30, 250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # To be run if collision occurs between Player and Coin
    if pygame.sprite.spritecollideany(P1, coins):
        COIN_SCORE += 1

        for entity in coins:
            entity.kill()

        if not coins:
            new_coin = Coin()
            coins.add(new_coin)

    if pygame.sprite.spritecollideany(P1, coins2):
        COIN_SCORE += 2

        for entity in coins2:
            entity.kill()

        if not coins:
            new_coin2 = Coin2()
            coins2.add(new_coin2)

    if COIN_SCORE > 10:
        SPEED = 10

    FramePerSec.tick(FPS)
    pygame.display.update()
