import pytest
import pygame
import math
import utils
from main import Ghost

@pytest.fixture #using fixtures for flexibility and no repetition
def screen(): #setting resolution (map size)
    pygame.init()
    return pygame.display.set_mode((800, 600))

@pytest.fixture
def level(): # displaying level
    return [[0 for _ in range(30)] for _ in range(20)]

# ------------------------- TEST 1 -------------------------
# here we define all function's parameters and test level render
def test_draw_board(screen, level): #passing fixtures to the test
    color = (255, 255, 255)
    flicker = False
    HEIGHT = 600
    WIDTH = 800
    PI = math.pi

    try:
        utils.draw_board(screen, color, flicker, HEIGHT, WIDTH, level, PI)
    except Exception as e:
        pytest.fail(f"draw_board raised an exception: {e}")

@pytest.fixture
def player_images(): # for rendering pacman pictures
    return [pygame.Surface((50, 50)) for _ in range(5)]

# ------------------------- TEST 2 -------------------------
# using player_images fixture along with already created screen
def test_draw_player(screen, player_images):
    direction = 1 # left direction
    counter = 10 # for picture
    player_x = 100
    player_y = 200

    try:
        utils.draw_player(screen, direction, player_images, counter, player_x, player_y)
    except Exception as e:
        pytest.fail(f"draw_player raised an exception: {e}")

#creating fixture for Ghost class
class Ghost:
    def __init__(self, dead):
        self.dead = dead

#using parametrization for expected positions of ghosts in different cases
@pytest.mark.parametrize("player_x, player_y, powerup, blinky_dead, inky_dead, pinky_dead, clyde_dead, eaten_ghost, expected", [
    (450, 450, False, False, False, False, False, [False, False, False, False], [(450, 450), (450, 450), (450, 450), (450, 450)]),# when no ghosts are dead and no powerup
    (450, 450, True, False, False, False, False, [False, False, False, False], [(0, 0), (0, 450), (450, 0), (450, 450)]), # when one ghost is dead and no powerup
    (450, 450, True, True, False, False, False, [True, False, False, False], [(380, 400), (0, 450), (450, 0), (450, 450)]), # when no ghosts are dead and powerup is active
])

# ------------------------- TEST 3 -------------------------
# checking whether these scenarios actually are true
def test_get_targets(player_x, player_y, powerup, blinky_dead, inky_dead, pinky_dead, clyde_dead, eaten_ghost, expected):
    blinky = Ghost(blinky_dead)
    inky = Ghost(inky_dead)
    pinky = Ghost(pinky_dead)
    clyde = Ghost(clyde_dead)
    targets = utils.get_targets(340, 340, 340, 340, 340, 340, 340, 340, player_x, player_y, powerup, blinky, inky, pinky, clyde, eaten_ghost, 800, 800)
    assert targets == expected #comparing factual positions with expected



#using parametrization for expected walls and directions of pacman
@pytest.mark.parametrize("centerx, centery, direction, HEIGHT, WIDTH, level, expected", [
    # based on the "turns" array with corresponding values, explained in the function logic
    (450, 450, 0, 600, 800, [[0]*30]*30, [False, True, False, False]),  # 0 - right when empty space at turns [1]
    (450, 450, 1, 600, 800, [[0]*30]*30, [True, False, False, False]),  # analogically 1 - left, turns [0]
    (450, 450, 2, 600, 800, [[0]*30]*30, [False, False, False, True]),  # 2 - up, turns[3]
    (450, 450, 3, 600, 800, [[0]*30]*30, [False, False, True, False]),  # 3 - down, turns[2]
    (450, 450, 0, 600, 800, [[3]*30]*30, [False, False, False, False]),  # moving right, no empty spaces
])

# ------------------------- TEST 4 -------------------------
#checking available moves for pacman based on his position
def test_check_position(centerx, centery, direction, HEIGHT, WIDTH, level, expected):
    turns = utils.check_position(centerx, centery, direction, HEIGHT, WIDTH, level)
    assert turns == expected


# using parametrization for general rules of pacman's movement
@pytest.mark.parametrize("play_x, play_y, direction, turns_allowed, player_speed, expected", [
    (0, 0, 0, [True, False, False, False], 1, (1, 0)),  # moving right
    (0, 0, 1, [False, True, False, False], 1, (-1, 0)),  # moving left
    (0, 0, 2, [False, False, True, False], 1, (0, -1)),  # moving up
    (0, 0, 3, [False, False, False, True], 1, (0, 1)),  # moving down
])

#checking whether the result of pacman's movement is correct
# ------------------------- TEST 5 -------------------------
def test_move_player(play_x, play_y, direction, turns_allowed, player_speed, expected):
    result = utils.move_player(play_x, play_y, direction, turns_allowed, player_speed)
    assert result == expected

#model of possible collisions with spheres and powerups
@pytest.mark.parametrize("score, power, power_count, eaten_ghosts, HEIGHT, WIDTH, player_x, center_y, center_x, level, expected", [
    (0, False, 0, [False, False, False, False], 600, 800, 450, 450, 450, [[0]*30]*30, (0, False, 0, [False, False, False, False])),  # no collisions, score 0
    (0, False, 0, [False, False, False, False], 600, 800, 450, 450, 450, [[1]*30]*30, (10, False, 0, [False, False, False, False])),  # collision with sphere, score 10
    (0, False, 0, [False, False, False, False], 600, 800, 450, 450, 450, [[2]*30]*30, (50, True, 0, [False, False, False, False])),  # collision with powerup, score 50, power - yes, powercount - 0, eaten ghosts - false
])

#checking collisions with spheres and powerups
# ------------------------- TEST 6 -------------------------
def test_check_collisions(score, power, power_count, eaten_ghosts, HEIGHT, WIDTH, player_x, center_y, center_x, level, expected):
    result = utils.check_collisions(score, power, power_count, eaten_ghosts, HEIGHT, WIDTH, player_x, center_y, center_x, level)
    assert result == expected