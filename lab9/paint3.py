import pygame
import math
pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
base_layer = pygame.Surface((WIDTH, HEIGHT))
colorWHITE = (255, 255, 255)
colorGRAY = (200, 200, 200)
colorBLACK = (0, 0, 0)
colorRED = (255, 0, 0)
colorGREEN = (0, 255, 0)
colorBLUE = (0, 0, 255)
colorYELLOW = (255, 255, 0)
clock = pygame.time.Clock()
LMBpressed = False
RMBpressed = False
THICKNESS = 5
currX = 0
currY = 0
prevX = 0
prevY = 0


def erase_figure(position):
    pygame.draw.circle(screen, colorBLACK, position, 25)


def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))


def calculate_center(x1, y1, x2, y2):
    return (abs(x2-x1)), abs((y2-y1))


def calculate_right_triangle(x1, y1, x2, y2):
    if x2 >= x1:
        zx = min(x1, x2)
    elif x2 < x1:
        zx = max(x1, x2)
    if y2 >= y1:
        zy = max(y1, y2)
    elif y2 < y1:
        zy = min(y1, y2)
    return (x1, y1), (x2, y2), (zx, zy)


def calculate_square(x1, y1, x2, y2):
    if x2-x1 > y2-y1:
        return pygame.Rect(min(x1, x2), min(y1, y2), abs(y1 - y2), abs(y1 - y2))
    else:
        return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(x1 - x2))


def calculate_equ_triangle(x1, y1, x2, y2):
    if x2 >= x1:
        zx = x1 + (abs(x2-x1))/2
    elif x2 < x1:
        zx = x1 - (abs(x2-x1))/2
    return (x2, y2), (x1, y2), (zx, y1)


def calculate_rhombus(x1, y1, x2, y2):
    if x2 >= x1:
        zx = x1 + (abs(x2-x1))/2
    elif x2 < x1:
        zx = x1 - (abs(x2-x1))/2
    if y2 >= y1:
        zy = y1 + (abs(y2 - y1))/2
    elif y2 < y1:
        zy = y1 - (abs(y2 - y1))/2
    return (zx, y1), (x1, zy), (zx, y2), (x2, zy)


desired_color = colorWHITE
desired_figure = "rect"

done = False

while not done:
    for event in pygame.event.get():
        if LMBpressed:
            screen.blit(base_layer, (0, 0))

        if RMBpressed:
            erase_figure(event.pos)


        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                desired_color = colorRED
            elif event.key == pygame.K_g:
                desired_color = colorGREEN
            elif event.key == pygame.K_b:
                desired_color = colorBLUE
            elif event.key == pygame.K_w:
                desired_color = colorWHITE

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_0:
                pygame.draw.rect(screen, colorRED, calculate_rect(prevX, prevY, currX, currY), THICKNESS)
            elif event.key == pygame.K_1:
                desired_figure = "square"
            elif event.key == pygame.K_2:
                desired_figure = "rhombus"
            elif event.key == pygame.K_3:
                desired_figure = "right_triangle"
            elif event.key == pygame.K_4:
                desired_figure = "equ_triangle"
            elif event.key == pygame.K_5:
                desired_figure = "circle"

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print("LMB pressed!")
            LMBpressed = True
            prevX = event.pos[0]
            prevY = event.pos[1]

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
            RMBpressed = True

        if event.type == pygame.MOUSEMOTION:
            print("Position of the mouse:", event.pos)
            if LMBpressed:
                currX = event.pos[0]
                currY = event.pos[1]

                match desired_figure:
                    case "rect":
                        pygame.draw.rect(screen, colorRED, calculate_rect(prevX, prevY, currX, currY), THICKNESS)
                    case "square":
                        pygame.draw.rect(screen, desired_color, calculate_square(prevX, prevY, currX, currY), THICKNESS)
                    case "rhombus":
                        pygame.draw.polygon(screen, desired_color, calculate_rhombus(prevX, prevY, currX, currY),
                                            THICKNESS)
                    case "right_triangle":
                        pygame.draw.polygon(screen, desired_color, calculate_right_triangle(prevX, prevY, currX, currY),
                                            THICKNESS)
                    case "equ_triangle":
                        pygame.draw.polygon(screen, desired_color, calculate_equ_triangle(prevX, prevY, currX, currY),
                                            THICKNESS)
                    case "circle":
                        pygame.draw.circle(screen, desired_color, calculate_center(prevX, prevY, currX, currY),
                                           abs(currX - prevX), THICKNESS)

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            print("LMB released!")
            LMBpressed = False
            currX = event.pos[0]
            currY = event.pos[1]
            RMBpressed = False

            match desired_figure:
                case "rect":
                    pygame.draw.rect(screen, colorRED, calculate_rect(prevX, prevY, currX, currY), THICKNESS)
                case "square":
                    pygame.draw.rect(screen, desired_color, calculate_square(prevX, prevY, currX, currY),
                                        THICKNESS)
                case "rhombus":
                    pygame.draw.polygon(screen, desired_color, calculate_rhombus(prevX, prevY, currX, currY),
                                        THICKNESS)
                case "right_triangle":
                    pygame.draw.polygon(screen, desired_color,
                                        calculate_right_triangle(prevX, prevY, currX, currY), THICKNESS)
                case "equ_triangle":
                    pygame.draw.polygon(screen, desired_color,
                                        calculate_equ_triangle(prevX, prevY, currX, currY), THICKNESS)
                case "circle":
                    pygame.draw.circle(screen, desired_color, calculate_center(prevX, prevY, currX, currY),
                                       abs(currX - prevX), THICKNESS)
            base_layer.blit(screen, (0, 0))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_EQUALS:
                print("increased thickness")
                THICKNESS += 1
            if event.key == pygame.K_MINUS:
                print("reduced thickness")
                THICKNESS -= 1

    pygame.display.flip()
    clock.tick(60)
