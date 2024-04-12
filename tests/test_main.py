import main
import pytest
import pygame
from unittest.mock import patch

@pytest.fixture #фікстура
def screen():
    pygame.init()
    return pygame.display.set_mode((800, 600))



@pytest.mark.fps_test # тест на таймер до початку руху
@pytest.mark.parametrize("startup_counter, expected_result", [(-100, False),
                                                              (0, False),
                                                              (10, False),
                                                              (100, False),
                                                              (180, True),
                                                              (300, True),
                                                              (500, True)] )
def test_fps_moving(startup_counter, expected_result):
    test_result = main.fps_moving(startup_counter)
    assert expected_result == test_result

@pytest.mark.fps_test # тест на таймер блимань
@pytest.mark.parametrize("counter, expected_result", [(1, False),
                                                      (5, False),
                                                      (10, False),
                                                      (15, False),
                                                      (19, True),
                                                      (20, True),
                                                      (30, True),
                                                      (50, True)] )
def test_fps_counter(counter, expected_result):
    test_result = main.fps_counter(counter)
    assert expected_result == test_result


@pytest.mark.fps_test # тест на таймер дії посилювачів
@pytest.mark.parametrize("powerup, power_counter, expected_result", [(True, 0, 1),
                                                                      (True, 100, 101),
                                                                      (True, 200, 201),
                                                                      (True, 500, 501),
                                                                      (True, 599, 600),
                                                                      (True, 600, 0),
                                                                      (True, 700, 0),
                                                                     (True, 800, 0),
                                                                     (True, 900, 0)] )
def test_fps_powerup(powerup, power_counter, expected_result):
    test_result = main.fps_powerup(powerup, power_counter)
    assert expected_result == test_result


@pytest.mark.teleportation_test # тест на телепортацію пакмана на краях єкрану
@patch('main.player_x', 901)
def test_player_teleportation1():
    main.player_teleportation(main.player_x)
    assert main.player_x == -47

@pytest.mark.teleportation_test # тест на телепортацію пакмана на краях єкрану
@patch('main.player_x', -51)
def test_player_teleportation2():
    main.player_teleportation(main.player_x)
    assert main.player_x == 897

