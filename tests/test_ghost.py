import pytest
import pygame
from unittest.mock import MagicMock
from main import Ghost

def setup_module(module):
    pygame.init()

@pytest.fixture
def mock_screen():
    return MagicMock()

@pytest.fixture
def ghost_attributes():
    return {
        "x_coord": 100,
        "y_coord": 200,
        "target": (300, 400),
        "speed": 5,
        "img": pygame.surface.Surface((32, 32)),  # Пустий об'єкт pygame.surface.Surface
        "direct": "right",
        "dead": False,
        "box": True,
        "id": 1
    }

def test_ghost_draw(mock_screen, ghost_attributes):
    ghost = Ghost(**ghost_attributes)
    powerup = False
    eaten_ghost = {1: False}
    spooked_img = pygame.surface.Surface((32, 32))  # Теж створюємо пустий об'єкт pygame.surface.Surface
    dead_img = pygame.surface.Surface((32, 32))  # Теж створюємо пустий об'єкт pygame.surface.Surface

    ghost_rect = ghost.draw(mock_screen, powerup, eaten_ghost, spooked_img, dead_img)

    assert ghost_rect  # Перевірка, що метод повертає прямокутник
    assert mock_screen.blit.called  # Перевірка, що метод blit викликаний для екрану


def test_ghost_check_collisions(ghost_attributes):
    ghost = Ghost(**ghost_attributes)
    turns, in_box = ghost.check_collisions()

    assert isinstance(turns, tuple)
    assert isinstance(in_box, bool)
    assert len(turns) == 4
    for turn in turns:
        assert isinstance(turn, bool)

    assert isinstance(in_box, bool)
    
    
def test_ghost_move_clyde(ghost_attributes):
    ghost = Ghost(**ghost_attributes)

    ghost.turns = [True, True, True, True]

    new_x, new_y, new_direction = ghost.move_clyde()
  
    assert isinstance(new_x, int)
    assert isinstance(new_y, int)

    assert isinstance(new_direction, int)

    assert 0 <= new_x <= 900
    assert 0 <= new_y <= 600
    assert new_direction in [0, 1, 2, 3]