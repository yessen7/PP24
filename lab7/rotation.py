import math
import pygame

from pygame import Vector2

screen_size = Vector2(192, 108)
screen_center = screen_size // 2

reference_dict = {}


def rotate_on_pivot(image, angle, pivot, origin):
    surf = pygame.transform.rotate(image, angle)

    offset = pivot + (origin - pivot).rotate(-angle)
    rect = surf.get_rect(center=offset)

    return surf, rect


class SpikeBall:
    chain_length = 32

    def __init__(self, pivot, starting_angle=0):
        self.pivot = pivot
        self.angle = 0

        offset = Vector2()
        offset.from_polar((self.chain_length, -starting_angle))

        self.pos = pivot + offset

        self.image_orig = reference_dict['C:/Users/PROCOM/Desktop/PP24/lab7/images/spikeball']
        self.image = self.image_orig
        self.rect = self.image.get_rect(center=self.pos)

    def update(self, dt):
        self.angle += 120 * dt

        self.image, self.rect = rotate_on_pivot(self.image_orig, self.angle, self.pivot, self.pos)

    def draw(self, surface):
        pygame.draw.line(surface, 'darkgray', self.pivot, self.rect.center, width=3)
        pygame.draw.line(surface, 'black', self.pivot, self.rect.center)
        surface.blit(self.image, self.rect)


class Game:
    def __init__(self):
        pygame.init()

        self.clock = pygame.time.Clock()
        self.running = False

        self.screen = pygame.display.set_mode(screen_size, flags=pygame.SCALED)

        self.load_image('C:/Users/PROCOM/Desktop/PP24/lab7/images/spikeball', colorkey='white')

        self.spikeball = SpikeBall(screen_center, starting_angle=0)

    def load_image(self, image_name, colorkey=None):
        image = pygame.image.load(f'{image_name}.png').convert()

        if colorkey is not None:
            image.set_colorkey(colorkey)

        reference_dict[image_name] = image

    def update(self, dt):
        self.spikeball.update(dt)

    def draw(self, surface):

        surface.fill('black')

        pygame.draw.line(surface, 'red', (screen_center.x, 0), (screen_center.x, screen_size.y))
        pygame.draw.line(surface, 'red', (0, screen_center.y), (screen_size.x, screen_center.y))

        self.spikeball.draw(surface)

        pygame.display.flip()

    def run(self):

        self.running = True

        while self.running:

            dt = self.clock.tick() * .001
            self.fps = self.clock.get_fps()
            pygame.display.set_caption(f'FPS: {self.fps}')

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False

            self.update(dt)
            self.draw(self.screen)


if __name__ == '__main__':
    Game().run()
