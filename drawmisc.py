import pygame
#Функція для відмалювання різних текстів
def draw_misc(score, game_over, game_won, screen, font, lives, player_images):
    #Вивід на екран поточної к-сті очок
    score_text = font.render(f'К-сть очок: {score}', True, 'white')
    screen.blit(score_text, (10, 920))
    #Вивід на екран поточної к-сті життів
    for i in range(lives):
        screen.blit(pygame.transform.scale(player_images[0], (30, 30)), (650 + i * 40, 915))
    #Вивід на екран повідомлення після поразки в грі
    if game_over:
        pygame.draw.rect(screen, 'white', [50, 200, 800, 300],0, 10)
        pygame.draw.rect(screen, 'dark gray', [70, 220, 760, 260], 0, 10)
        gameover_text = font.render('Кінець гри! Натисніть Space, щоб почати нову гру', True, 'red')
        screen.blit(gameover_text, (100, 300))
    # Вивід на екран повідомлення після перемоги в грі
    if game_won:
        pygame.draw.rect(screen, 'white', [50, 200, 800, 300],0, 10)
        pygame.draw.rect(screen, 'dark gray', [70, 220, 760, 260], 0, 10)
        gameover_text = font.render('Гра пройдена! Натисніть Space, щоб почати нову гру', True, 'green')
        screen.blit(gameover_text, (100, 300))