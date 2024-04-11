import pygame
import datetime


x = 1000
y = 800
pygame.init()
screen = pygame.display.set_mode((x, y))
done = False
FPS = 50

mickey = pygame.image.load("C:/Users/PROCOM/Desktop/PP24/lab7/images/no_hand.png").convert_alpha()
mickey = pygame.transform.smoothscale(mickey, (1000, 800))

right_arm = pygame.image.load("C:/Users/PROCOM/Desktop/PP24/lab7/images/rightarm.png").convert_alpha()
right_arm = pygame.transform.smoothscale(right_arm, (200, 300))
left_arm = pygame.image.load("C:/Users/PROCOM/Desktop/PP24/lab7/images/leftarm.png").convert_alpha()
left_arm = pygame.transform.smoothscale(left_arm, (50, 500))

clock = pygame.time.Clock()

def blitRotateCenter(surf, image, topleft, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=image.get_rect(topleft=topleft).center)

    surf.blit(rotated_image, new_rect)

def rotate_on_pivot(image, angle, pivot, origin):

    surf = pygame.transform.rotate(image, angle)
    offset = pivot + (origin - pivot).rotate(-angle)
    rect = surf.get_rect(center=offset)
    return surf, rect


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((69, 69, 69))

    current_time = datetime.datetime.now()
    minute = current_time.minute
    second = current_time.second

    angle_seconds = 0
    angle_seconds += second*6

    angle_minutes = 0
    angle_minutes += angle_seconds/60

    screen.blit(mickey, ((x/2)-500, (y/2)-400))
    screen.blit(right_arm, ((x/2)-60, (y/2)-230))
    screen.blit(left_arm, ((x/2)-25, (y/2)-250))

    #minute - right_hand
    R1 = 200
    theta1 = minute
    #second - left_hand
    R2 = 250
    theta2 = second

    blitRotateCenter(screen, left_arm, ((x/2)-25, (y/2)-250), -angle_seconds)
    blitRotateCenter(screen, right_arm, ((x/2)-60, (y/2)-230), -angle_minutes)

    pygame.display.flip()
    clock.tick(FPS)

