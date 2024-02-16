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