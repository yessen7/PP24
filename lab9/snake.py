import pygame, sys, time, random

# Initializing
pygame.init()

# Difficulty settings
# Easy      ->  10
# Medium    ->  25
# Hard      ->  40
# Harder    ->  60
# Impossible->  120
difficulty = 25

# Window size
SCREEN_WIDTH = 720
SCREEN_HEIGHT = 480

# Initialise game window
pygame.display.set_caption('Snake')
surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Colors (R, G, B)
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)


# FPS (frames per second) controller
FramePerSec = pygame.time.Clock()


# Game variables
snake_pos = [100, 50]
snake_body = [[100, 50], [100-10, 50], [100-(2*10), 50]]

foods = [{"weight": 1, "color": white}, {"weight": 2, "color": blue}, {"weight": 3, "color": red}]

food = random.choice(foods)
food_pos = [random.randrange(1, (SCREEN_WIDTH//10)) * 10, random.randrange(1, (SCREEN_HEIGHT//10)) * 10]
food_spawn = True
food_spawn_time = time.time()

direction = 'RIGHT'
change_to = direction

score = 0


# Game Over
def game_over():
    my_font = pygame.font.SysFont('times new roman', 90)
    game_over_surface = my_font.render('YOU DIED', True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (SCREEN_HEIGHT/2, SCREEN_WIDTH/4)
    surface.fill(black)
    surface.blit(game_over_surface, game_over_rect)
    show_score(0, red, 'times', 20)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    sys.exit()


# Score
def show_score(choice, color, font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score), True, color)
    score_rect = score_surface.get_rect()
    if choice == 1:
        score_rect.midtop = (SCREEN_WIDTH/10, 15)
    else:
        score_rect.midtop = (SCREEN_WIDTH/2, SCREEN_HEIGHT/1.25)
    surface.blit(score_surface, score_rect)
    # pygame.display.flip()


# Main logic
while True:
    current_time = time.time()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # Whenever a key is pressed down
        elif event.type == pygame.KEYDOWN:
            # W -> Up; S -> Down; A -> Left; D -> Right
            if event.key == pygame.K_UP or event.key == ord('w'):
                change_to = 'UP'
            if event.key == pygame.K_DOWN or event.key == ord('s'):
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT or event.key == ord('a'):
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT or event.key == ord('d'):
                change_to = 'RIGHT'
            # Esc -> Create event to quit the game
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))

    # Making sure the snake cannot move in the opposite direction instantaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Moving the snake
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    if direction == 'RIGHT':
        snake_pos[0] += 10

    weight = food.get("weight")
    food_color = food.get("color")


    # Snake body growing mechanism
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += weight
        food_spawn = False
    else:
        snake_body.pop()

    if current_time - food_spawn_time >= 10:
        food = random.choice(foods)
        food_pos = [random.randrange(1, (SCREEN_HEIGHT // 10)) * 10, random.randrange(1, (SCREEN_HEIGHT // 10)) * 10]
        food_spawn_time = current_time


    # Spawning food on the screen
    if not food_spawn:
        food_pos = [random.randrange(1, (SCREEN_HEIGHT//10)) * 10, random.randrange(1, (SCREEN_HEIGHT//10)) * 10]
    food_spawn = True

    # GFX
    surface.fill(black)
    for pos in snake_body:
        # Snake body
        # .draw.rect(play_surface, color, xy-coordinate)
        # xy-coordinate -> .Rect(x, y, size_x, size_y)
        pygame.draw.rect(surface, green, pygame.Rect(pos[0], pos[1], 10, 10))

    # Snake food
    pygame.draw.rect(surface, food_color, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Game Over conditions
    # Getting out of bounds
    if snake_pos[0] < 0 or snake_pos[0] > SCREEN_WIDTH-10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > SCREEN_HEIGHT-10:
        game_over()
    # Touching the snake body
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()

    show_score(1, white, 'consolas', 20)
    # Refresh game screen
    pygame.display.update()
    # Refresh rate
    FramePerSec.tick(difficulty)
