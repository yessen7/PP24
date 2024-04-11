import pygame
import random

pygame.init()
screen = pygame.display.set_mode((500, 400))
done = False
clock = pygame.time.Clock()

KEY_PLAY_PAUSE = pygame.K_SPACE
KEY_NEXT = pygame.K_RIGHT
KEY_PREV = pygame.K_LEFT
KEY_QUIT = pygame.K_ESCAPE
num = 0

songs = ["C:/Users/PROCOM/Desktop/PP24/lab7/sounds/hey_jude.mp3", "C:/Users/PROCOM/Desktop/PP24/lab7/sounds/cowboys.mp3", "C:/Users/PROCOM/Desktop/PP24/lab7/sounds/kaitadan.mp3"]
currently_playing_song = None


def play_pause():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()

def load_song(num):
    song = songs[num]
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()

def next_song():
    global num
    num = num + 1
    if num > len(songs)-1:
        num = num - 1
    song = songs[num]
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()


def prev_song():
    global num
    num = num - 1
    if num < 0:
        num = num + 1
    song = songs[num]
    pygame.mixer.music.load(song)
    pygame.mixer.music.play()

def play_a_different_song():
    global currently_playing_song, songs
    next_song = random.choice(songs)
    while next_song == currently_playing_song:
        next_song = random.choice(songs)
    _currently_playing_song = next_song
    pygame.mixer.music.load(next_song)
    pygame.mixer.music.play()


load_song(0)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == KEY_PLAY_PAUSE:
                play_pause()
            elif event.key == KEY_NEXT:
                next_song()
            elif event.key == KEY_PREV:
                prev_song()

    screen.fill((55, 90, 255))

    pygame.display.flip()
    clock.tick(60)












