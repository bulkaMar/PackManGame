import pygame

def draw_elems(screen, font, score, powerup, lives, player_images, game_over, game_won):
    '''
    This function renders different elements of the game, including score,
    powerups, lives, messages if player lost or won.
    '''
    score_text = font.render(f'Score: {score}', True, 'white')
    screen.blit(score_text, (10, 920)) # positioning of score
    if powerup:
        pygame.draw.circle(screen, 'blue', (140, 930), 15) # rendering powerup circle
    for i in range(lives): # cycles through lives
        screen.blit(pygame.transform.scale(player_images[0], (30, 30)), (650 + i * 40, 915)) # rendering lives
    if game_over:
        font_big = pygame.font.Font(None, 72) # fonts for different messages
        font_small = pygame.font.Font(None, 36)
        gameover_text = font_big.render('Game over!', True, 'yellow')
        restart_text = font_small.render('Press spacebar to restart', True, 'yellow')
        gameover_rect = gameover_text.get_rect(center=(screen.get_width()/2, screen.get_height()/2 - 50)) # placing in the center
        restart_rect = restart_text.get_rect(center=(screen.get_width()/2, screen.get_height()/2 + 50))
        screen.blit(gameover_text, gameover_rect)
        screen.blit(restart_text, restart_rect)
    if game_won:
        font_big = pygame.font.Font(None, 72)
        font_small = pygame.font.Font(None, 36)
        gameover_text = font_big.render('Victory!', True, 'yellow')
        restart_text = font_small.render('Press spacebar to restart', True, 'yellow')
        gameover_rect = gameover_text.get_rect(center=(screen.get_width()/2, screen.get_height()/2 - 50))
        restart_rect = restart_text.get_rect(center=(screen.get_width()/2, screen.get_height()/2 + 50))
        screen.blit(gameover_text, gameover_rect)
        screen.blit(restart_text, restart_rect)


def draw_board(screen, color, flicker, HEIGHT, WIDTH, level, PI):
    '''
    Drawing elements of the board. Spheres, powerups and the board
    '''
    num1 = ((HEIGHT - 50) // 32)
    num2 = (WIDTH // 30)
    for i in range(len(level)):
        for j in range(len(level[i])):
            if level[i][j] == 1:
                pygame.draw.circle(screen, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 4) # adding spheres
            if level[i][j] == 2 and not flicker:
                pygame.draw.circle(screen, 'white', (j * num2 + (0.5 * num2), i * num1 + (0.5 * num1)), 10)# adding powerups
            if level[i][j] == 3:
                pygame.draw.line(screen, color, (j * num2 + (0.5 * num2), i * num1),
                                 (j * num2 + (0.5 * num2), i * num1 + num1), 3)# adding vertical lines
            if level[i][j] == 4:
                pygame.draw.line(screen, color, (j * num2, i * num1 + (0.5 * num1)), # adding horizontal
                                 (j * num2 + num2, i * num1 + (0.5 * num1)), 3)
            if level[i][j] == 5:
                pygame.draw.arc(screen, color, [(j * num2 - (num2 * 0.4)) - 2, (i * num1 + (0.5 * num1)), num2, num1],
                                0, PI / 2, 3) # adding top right corner
            if level[i][j] == 6:
                pygame.draw.arc(screen, color, # adding top left corner
                                [(j * num2 + (num2 * 0.5)), (i * num1 + (0.5 * num1)), num2, num1], PI / 2, PI, 3)
            if level[i][j] == 7:# adding bottom left corner
                pygame.draw.arc(screen, color, [(j * num2 + (num2 * 0.5)), (i * num1 - (0.4 * num1)), num2, num1], PI,
                                3 * PI / 2, 3)
            if level[i][j] == 8: # adding bottom right corner
                pygame.draw.arc(screen, color,
                                [(j * num2 - (num2 * 0.4)) - 2, (i * num1 - (0.4 * num1)), num2, num1], 3 * PI / 2,
                                2 * PI, 3)
            if level[i][j] == 9: # adding vertical line for ghost's gate
                pygame.draw.line(screen, 'white', (j * num2, i * num1 + (0.5 * num1)),
                                 (j * num2 + num2, i * num1 + (0.5 * num1)), 3)


def draw_player(screen, direction, player_images, counter, player_x, player_y):
    '''
    Drawing a pacman based on the pictures, rotating them if needed
    '''
    if direction == 0: # if pacman moves right
        screen.blit(player_images[counter // 5], (player_x, player_y)) # drawing appropriate pacman image
    elif direction == 1: # left
        screen.blit(pygame.transform.flip(player_images[counter // 5], True, False), (player_x, player_y)) # flipping the picture so it faces the opposite way
    elif direction == 2: # up
        screen.blit(pygame.transform.rotate(player_images[counter // 5], 90), (player_x, player_y)) # rotating picture accordingly
    elif direction == 3: # down
        screen.blit(pygame.transform.rotate(player_images[counter // 5], 270), (player_x, player_y))


