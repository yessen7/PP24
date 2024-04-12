import pygame

pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
done = False
is_blue = True
x = 30
y = 30
clock = pygame.time.Clock()

def drawStyleRect(surface):
    pygame.draw.rect(surface, (0,0,255), (x,y,150,150), 0)
    for i in range(4):
        pygame.draw.rect(surface, (0,0,0), (x-i,y-i,155,155), 1)


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue

    pressed = pygame.key.get_pressed()
    drawStyleRect(screen)

    if pressed[pygame.K_w] and y > 35:
        y -= 10
    if pressed[pygame.K_s] and y < HEIGHT-35:
        y += 10
    if pressed[pygame.K_a] and x > 35:
        x -= 10
    if pressed[pygame.K_d] and x < WIDTH-35:
        x += 10


    screen.fill((255, 255, 255))
    if is_blue:
        color = (0, 128, 255)
    else:
        color = (255, 0, 0)

    pygame.draw.line(screen, (0, 255, 0), (0, 0), (0, HEIGHT), 5)
    pygame.draw.line(screen, (0, 255, 0), (0, HEIGHT), (WIDTH, HEIGHT), 7)
    pygame.draw.line(screen, (0, 255, 0), (WIDTH, HEIGHT), (WIDTH, 0), 7)
    pygame.draw.line(screen, (0, 255, 0), (WIDTH, 0), (0, 0), 5)

    pygame.draw.circle(screen, color, (x, y), 30)
    pygame.display.update()
    clock.tick(60)

