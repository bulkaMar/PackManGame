import pygame
import pytest
from main import Ghost

# Fixture to initialize Pygame and create a screen surface
@pytest.fixture(scope="module")
def screen():
    pygame.init()
    return pygame.display.set_mode((800, 600))

# Fixture to create a Ghost instance for testing
@pytest.fixture
def ghost_instance(screen):
    img_path = pygame.image.load("assets/ghost_images/blue.png")
    img = img_path
    target = (100, 100)  # Приклад значення цілі
    return Ghost(x_coord=0, y_coord=0, target=target, speed=1, img=img, direct=None, dead=False, box=False, id=1)

@pytest.fixture
def event_loop(screen):
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        pygame.display.update()  

# Test cases
@pytest.mark.parametrize("x_pos, y_pos, expected_in_box", [
    (400, 400, True),  # Ghost inside the box
    (200, 200, False),  # Ghost outside the box
])
def test_check_collisions(ghost_instance, x_pos, y_pos, expected_in_box):
    ghost_instance.x_pos = x_pos
    ghost_instance.y_pos = y_pos

    turns, in_box = ghost_instance.check_collisions()

    assert in_box == expected_in_box

@pytest.mark.parametrize("initial_direction, target, turns, x_pos, y_pos, speed, expected_x, expected_y, expected_direction", [
    (0, (100, 100), [True, True, True, True], 50, 50, 5, 55, 50, 0),  # Initial direction right, no change expected
    (3, (100, 100), [True, True, True, True], 50, 50, 5, 50, 55, 3),  # Initial direction down, move down expected
])
def test_move_clyde(ghost_instance, initial_direction, target, turns, x_pos, y_pos, speed, expected_x, expected_y, expected_direction):
    ghost_instance.direction = initial_direction
    ghost_instance.target = target
    ghost_instance.turns = turns
    ghost_instance.x_pos = x_pos
    ghost_instance.y_pos = y_pos
    ghost_instance.speed = speed

    new_x, new_y, new_direction = ghost_instance.move_clyde()

    assert new_x == expected_x
    assert new_y == expected_y
    assert new_direction == expected_direction
    
    
# Parameterization for different movement directions
@pytest.mark.parametrize("initial_direction, expected_x, expected_y, expected_direction", [
    (0, 105, 100, 0),  # Right
    (1, 95, 100, 1),   # Left
])
def test_move_ghost_direction(ghost_instance, initial_direction, expected_x, expected_y, expected_direction):
    # Set the initial movement direction
    ghost_instance.direction = initial_direction
    ghost_instance.x_pos = 100
    ghost_instance.y_pos = 100
    ghost_instance.speed = 5

    # Call the movement method
    new_x, new_y, new_direction = ghost_instance.move_clyde()

    # Check if the ghost has moved correctly
    assert new_x == expected_x
    assert new_y == expected_y
    assert new_direction == expected_direction

# Fixture to quit Pygame after all tests are done
@pytest.fixture(scope="module", autouse=True)
def cleanup():
    yield
    pygame.quit()
    
    
