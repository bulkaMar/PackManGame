import pygame

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


def get_targets(blink_x, blink_y, ink_x, ink_y, pink_x, pink_y, clyd_x, clyd_y, player_x, player_y, powerup, blinky, inky, pinky, clyde, eaten_ghost, HEIGHT, WIDTH):
    '''
    The function defines all target positions for ghosts in different situations, related to pacman's actions
    '''
    if player_x < 450: # pacman x coordinate
        runaway_x = 900 # target positions for ghosts when the player has a powerup
    else:
        runaway_x = 0 # analogically (ghosts running to the oposite side of pacman)
    if player_y < 450: # analogically for y coordinates
        runaway_y = 900
    else:
        runaway_y = 0
    return_target = (380, 400) # target position ghosts return to when they are “dead”
    if powerup: # when pacman ate a powerup, ghosts’ target positions are set based on whether they are dead or have been eaten
        # if a ghost isn't dead wasn't eaten, its target position is runaway_x; runaway_y
        # if a ghost isn't dead but was eaten, its target position is either (400, 100) or pacman's position
        # if a ghost is dead, its target position is return_target, meaning the center of the map
        if not blinky.dead and not eaten_ghost[0]:
            blink_target = (runaway_x, runaway_y)
        elif not blinky.dead and eaten_ghost[0]:
            if 340 < blink_x < 560 and 340 < blink_y < 500: # if the range for ghosts position applies
                blink_target = (400, 100) # target position when pacman has a powerup activated
            else:
                blink_target = (player_x, player_y) # start pursuing the player again
        else:
            blink_target = return_target
        if not inky.dead and not eaten_ghost[1]:
            ink_target = (runaway_x, player_y)
        elif not inky.dead and eaten_ghost[1]:
            if 340 < ink_x < 560 and 340 < ink_y < 500:
                ink_target = (400, 100)
            else:
                ink_target = (player_x, player_y)
        else:
            ink_target = return_target
        if not pinky.dead:
            pink_target = (player_x, runaway_y)
        elif not pinky.dead and eaten_ghost[2]:
            if 340 < pink_x < 560 and 340 < pink_y < 500:
                pink_target = (400, 100)
            else:
                pink_target = (player_x, player_y)
        else:
            pink_target = return_target
        if not clyde.dead and not eaten_ghost[3]:
            clyd_target = (450, 450)
        elif not clyde.dead and eaten_ghost[3]:
            if 340 < clyd_x < 560 and 340 < clyd_y < 500:
                clyd_target = (400, 100)
            else:
                clyd_target = (player_x, player_y)
        else:
            clyd_target = return_target
    else: # if pacman has no powerup
        if not blinky.dead: # analogically
            if 340 < blink_x < 560 and 340 < blink_y < 500:
                blink_target = (400, 100)
            else:
                blink_target = (player_x, player_y)
        else:
            blink_target = return_target
        if not inky.dead:
            if 340 < ink_x < 560 and 340 < ink_y < 500:
                ink_target = (400, 100)
            else:
                ink_target = (player_x, player_y)
        else:
            ink_target = return_target
        if not pinky.dead:
            if 340 < pink_x < 560 and 340 < pink_y < 500:
                pink_target = (400, 100)
            else:
                pink_target = (player_x, player_y)
        else:
            pink_target = return_target
        if not clyde.dead:
            if 340 < clyd_x < 560 and 340 < clyd_y < 500:
                clyd_target = (400, 100)
            else:
                clyd_target = (player_x, player_y)
        else:
            clyd_target = return_target
    return [blink_target, ink_target, pink_target, clyd_target] # returning target positions for every ghost


def check_position(centerx, centery, direction, HEIGHT, WIDTH, level):
    '''
    Processing all available moves for pacman in particular positions on the map
    '''
    turns = [False, False, False, False] # tracking pacman's directions he can go
    num1 = (HEIGHT - 50) // 32
    num2 = (WIDTH // 30)
    num3 = 15 # fudge number to adjust the precision of collision detection
    # check collisions based on center x and center y of player +/- fudge number
    if centerx // 30 < 29: # if pacman is within these map bounds
        if direction == 0: # right
            if level[centery // num1][(centerx - num3) // num2] < 3: # checking direction and the value of the cell in array in the directions
                turns[1] = True # can turn this direction (< 3 because empty spaces)
        if direction == 1: # left
            if level[centery // num1][(centerx + num3) // num2] < 3:
                turns[0] = True # analogically
        if direction == 2: # up
            if level[(centery + num3) // num1][centerx // num2] < 3:
                turns[3] = True # analogically
        if direction == 3: # down
            if level[(centery - num3) // num1][centerx // num2] < 3:
                turns[2] = True # analogically

        if direction == 2 or direction == 3: # up or down
            if 12 <= centerx % num2 <= 18: # the horizontal position of the player within the current cell
                if level[(centery + num3) // num1][centerx // num2] < 3: # analogically
                    turns[3] = True
                if level[(centery - num3) // num1][centerx // num2] < 3:
                    turns[2] = True
            if 12 <= centery % num1 <= 18:
                if level[centery // num1][(centerx - num2) // num2] < 3:
                    turns[1] = True
                if level[centery // num1][(centerx + num2) // num2] < 3:
                    turns[0] = True
        if direction == 0 or direction == 1: # right or left
            if 12 <= centerx % num2 <= 18:
                if level[(centery + num1) // num1][centerx // num2] < 3:
                    turns[3] = True
                if level[(centery - num1) // num1][centerx // num2] < 3:
                    turns[2] = True
            if 12 <= centery % num1 <= 18:
                if level[centery // num1][(centerx - num3) // num2] < 3:
                    turns[1] = True
                if level[centery // num1][(centerx + num3) // num2] < 3:
                    turns[0] = True
    else:
        turns[0] = True # left
        turns[1] = True # right

    return turns


def move_player(play_x, play_y, direction, turns_allowed, player_speed):
    '''
    Rules of moving pacman around
    '''
    if direction == 0 and turns_allowed[0]: # right
        play_x += player_speed # moves pacman to the right by increasing the x-coordinate of pacman
    elif direction == 1 and turns_allowed[1]: # left
        play_x -= player_speed # analogically
    if direction == 2 and turns_allowed[2]: # up
        play_y -= player_speed
    elif direction == 3 and turns_allowed[3]: # down
        play_y += player_speed
    return play_x, play_y


def move_player(play_x, play_y, direction, turns_allowed, player_speed):
    '''
    Rules of moving pacman around
    '''
    if direction == 0 and turns_allowed[0]: # right
        play_x += player_speed # moves pacman to the right by increasing the x-coordinate of pacman
    elif direction == 1 and turns_allowed[1]: # left
        play_x -= player_speed # analogically
    if direction == 2 and turns_allowed[2]: # up
        play_y -= player_speed
    elif direction == 3 and turns_allowed[3]: # down
        play_y += player_speed
    return play_x, play_y


def check_collisions(score, power, power_count, eaten_ghosts, HEIGHT, WIDTH, player_x, center_y, center_x, level):
    '''
    Checking collision of pacman with spheres, powerups and ghosts. Updating values according to actions
    '''
    num1 = (HEIGHT - 50) // 32 # number of cells vertically
    num2 = WIDTH // 30 # horizontally, we need them to convert coordinates of pacman into indeces of our array
    if 0 < player_x < 870:
        if level[center_y // num1][center_x // num2] == 1: # indeces with value 1 (referring to spheres)
            level[center_y // num1][center_x // num2] = 0 # turn into 0 (referring to nothingness, indicating it's eaten)
            score += 10 # adding to the score when pacman eats a sphere
        if level[center_y // num1][center_x // num2] == 2: # indeces with value 2 (referring to powerups)
            level[center_y // num1][center_x // num2] = 0 # turn into 0 (referring to nothingness, indicating it's eaten)
            score += 50 # adding to the score when powerup is eaten
            power = True # toggle powerup mode on
            power_count = 0
            eaten_ghosts = [False, False, False, False] # initial array of ghosts, which arent eaten
    return score, power, power_count, eaten_ghosts