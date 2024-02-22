import pygame
#Функція для відмалювання різних текстів
def draw_misc(screen, font, score, lives, player_images, game_over, game_won):
    '''
    This function renders different elements of the game, including score,
    powerups, lives, messages if player lost or won.
    '''
    #Вивід на екран поточної к-сті очок
    score_text = font.render(f'К-сть очок: {score}', True, 'white')
    screen.blit(score_text, (10, 920))
    #Вивід на екран поточної к-сті життів
    for i in range(lives):
        screen.blit(pygame.transform.scale(player_images[0], (30, 30)), (650 + i * 40, 915))
    #Вивід на екран повідомлення після поразки в грі
    if game_over:
        font_big = pygame.font.Font(None, 72) # fonts for different messages
        font_small = pygame.font.Font(None, 36)
        gameover_text = font_big.render('Кінець гри!', True, 'yellow')
        restart_text = font_small.render('Натисніть Space, щоб почати нову гру', True, 'yellow')
        gameover_rect = gameover_text.get_rect(center=(screen.get_width()/2, screen.get_height()/2 - 50)) # placing in the center
        restart_rect = restart_text.get_rect(center=(screen.get_width()/2, screen.get_height()/2 + 50))
        screen.blit(gameover_text, gameover_rect)
        screen.blit(restart_text, restart_rect)
    # Вивід на екран повідомлення після перемоги в грі
    if game_won:
        font_big = pygame.font.Font(None, 72)
        font_small = pygame.font.Font(None, 36)
        gameover_text = font_big.render('Гра пройдена!', True, 'yellow')
        restart_text = font_small.render('Натисніть Space, щоб почати нову гру', True, 'yellow')
        gameover_rect = gameover_text.get_rect(center=(screen.get_width()/2, screen.get_height()/2 - 50))
        restart_rect = restart_text.get_rect(center=(screen.get_width()/2, screen.get_height()/2 + 50))
        screen.blit(gameover_text, gameover_rect)
        screen.blit(restart_text, restart_rect)