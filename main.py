import copy
from board import boards
import pygame
import math
import drawmisc

pygame.init()

#Налаштування параметрів екрану
WIDTH = 900
HEIGHT = 950
screen = pygame.display.set_mode([WIDTH, HEIGHT])

#Налаштування швидкодії гри
timer = pygame.time.Clock()
fps = 60
#Вибір шрифта
font = pygame.font.Font('freesansbold.ttf', 20)
#Створення рівня гри
level = copy.deepcopy(boards)
color = 'blue'
PI = math.pi

#Налаштування зображення Пакмана та привидів
player_images = []
for i in range(1, 5):
    player_images.append(pygame.transform.scale(pygame.image.load(f'assets/player_images/{i}.png'), (45, 45)))
blinky_img = pygame.transform.scale(pygame.image.load(f'assets/ghost_images/red.png'), (45, 45))
pinky_img = pygame.transform.scale(pygame.image.load(f'assets/ghost_images/pink.png'), (45, 45))
inky_img = pygame.transform.scale(pygame.image.load(f'assets/ghost_images/blue.png'), (45, 45))
clyde_img = pygame.transform.scale(pygame.image.load(f'assets/ghost_images/orange.png'), (45, 45))
spooked_img = pygame.transform.scale(pygame.image.load(f'assets/ghost_images/powerup.png'), (45, 45))
dead_img = pygame.transform.scale(pygame.image.load(f'assets/ghost_images/dead.png'), (45, 45))
#Налаштування початкового місцязнаходження та позицій Пакмана та привидів
player_x = 450
player_y = 663
direction = 0
blinky_x = 56
blinky_y = 58
blinky_direction = 0
inky_x = 440
inky_y = 388
inky_direction = 2
pinky_x = 440
pinky_y = 438
pinky_direction = 2
clyde_x = 440
clyde_y = 438
clyde_direction = 2
counter = 0
flicker = False