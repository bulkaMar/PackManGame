# from main import powerup, eaten_ghost, screen, spooked_img, dead_img, HEIGHT, WIDTH, level
# import pygame
# class Ghost:
#    def __init__(self, x_coord, y_coord, target, speed, img, direct, dead, box, id):
#         """
#         Ініціалізує об'єкт Ghost з вказаними параметрами.

#         Параметри:
#         - x_coord: Координата X положення Ghost.
#         - y_coord: Координата Y положення Ghost.
#         - target: Ціль, до якої прямує Ghost.
#         - speed: Швидкість Ghost.
#         - img: Зображення Ghost.
#         - direct: Напрямок руху Ghost.
#         - dead: Прапорець, що вказує, чи мертвий Ghost.
#         - box: Прапорець, що вказує, чи знаходиться Ghost в коробці.
#         - id: Ідентифікатор Ghost.
#         """
#         self.x_pos = x_coord
#         self.y_pos = y_coord
#         self.center_x = self.x_pos + 22
#         self.center_y = self.y_pos + 22
#         self.target = target
#         self.speed = speed
#         self.img = img
#         self.direction = direct
#         self.dead = dead
#         self.in_box = box
#         self.id = id
#         self.turns, self.in_box = self.check_collisions()
#         self.rect = self.draw()
        
        
#    def draw(self):
#       """
#       Малює привид на екрані залежно від його поточного стану.

#       Параметри:
#       - self: Екземпляр класу привида.
    
#       Що робить:
#       Функція відповідає за малювання зображення привида на екрані відповідно до його поточного стану. 
#       Залежно від наявності активного powerup та стану привида (живий, мертвий, в стані паніки), 
#       вона вибирає відповідне зображення для малювання.

#       Що повертає:
#       Повертає прямокутник, який обмежує область, де знаходиться привид на екрані. Це може бути
#       корисно для подальшої обробки зіткнень або інших операцій гри. Якщо привид не малюється
#       на екрані у поточному стані, повертається None.
#       """
#       if (not powerup and not self.dead) or (eaten_ghost[self.id] and powerup and not self.dead):
#          screen.blit(self.img, (self.x_pos, self.y_pos))
#       elif powerup and not self.dead and not eaten_ghost[self.id]:
#          screen.blit(spooked_img, (self.x_pos, self.y_pos))
#       else:
#          screen.blit(dead_img, (self.x_pos, self.y_pos))
#          ghost_rect = pygame.rect.Rect((self.center_x - 18, self.center_y - 18), (36, 36))
#       return ghost_rect

        
        
        
#    def check_collisions(self):
#       """
#       Перевіряє зіткнення привида зі стінами та іншими об'єктами на карті гри.

#       Що робить:
#       Функція визначає можливі напрямки руху привида та перевіряє його розташування
#       відносно стін та інших об'єктів на карті. Залежно від цього встановлюються
#       булеві значення, які вказують, в яких напрямках привид може здійснити обертання.

#       Що повертає:
#       Повертає кортеж з двома елементами:
#     - Список булевих значень `turns`, який вказує, в яких напрямках можливі обертання.
#       Елемент з індексом 0 відповідає напрямку вліво, елемент з індексом 1 - вправо,
#       елемент з індексом 2 - вверх, елемент з індексом 3 - вниз.
#     - Булеве значення `in_box`, яке вказує, чи знаходиться привид у спеціальній області "в коробці".
#       True, якщо привид знаходиться у коробці, False - в протилежному випадку.
#       """
      
#       # Right, Left, Up, Down
#       num1 = ((HEIGHT - 50) // 32)
#       num2 = (WIDTH // 30)
#       num3 = 15
#       self.turns = [False, False, False, False]
#       if 0 < self.center_x // 30 < 29:
#             if level[(self.center_y - num3) // num1][self.center_x // num2] == 9:
#                 self.turns[2] = True
#             if level[self.center_y // num1][(self.center_x - num3) // num2] < 3 \
#                     or (level[self.center_y // num1][(self.center_x - num3) // num2] == 9 and (
#                     self.in_box or self.dead)):
#                 self.turns[1] = True
#             if level[self.center_y // num1][(self.center_x + num3) // num2] < 3 \
#                     or (level[self.center_y // num1][(self.center_x + num3) // num2] == 9 and (
#                     self.in_box or self.dead)):
#                 self.turns[0] = True
#             if level[(self.center_y + num3) // num1][self.center_x // num2] < 3 \
#                     or (level[(self.center_y + num3) // num1][self.center_x // num2] == 9 and (
#                     self.in_box or self.dead)):
#                 self.turns[3] = True
#             if level[(self.center_y - num3) // num1][self.center_x // num2] < 3 \
#                     or (level[(self.center_y - num3) // num1][self.center_x // num2] == 9 and (
#                     self.in_box or self.dead)):
#                 self.turns[2] = True

#             if self.direction == 2 or self.direction == 3:
#                 if 12 <= self.center_x % num2 <= 18:
#                     if level[(self.center_y + num3) // num1][self.center_x // num2] < 3 \
#                             or (level[(self.center_y + num3) // num1][self.center_x // num2] == 9 and (
#                             self.in_box or self.dead)):
#                         self.turns[3] = True
#                     if level[(self.center_y - num3) // num1][self.center_x // num2] < 3 \
#                             or (level[(self.center_y - num3) // num1][self.center_x // num2] == 9 and (
#                             self.in_box or self.dead)):
#                         self.turns[2] = True
#                 if 12 <= self.center_y % num1 <= 18:
#                     if level[self.center_y // num1][(self.center_x - num2) // num2] < 3 \
#                             or (level[self.center_y // num1][(self.center_x - num2) // num2] == 9 and (
#                             self.in_box or self.dead)):
#                         self.turns[1] = True
#                     if level[self.center_y // num1][(self.center_x + num2) // num2] < 3 \
#                             or (level[self.center_y // num1][(self.center_x + num2) // num2] == 9 and (
#                             self.in_box or self.dead)):
#                         self.turns[0] = True

#             if self.direction == 0 or self.direction == 1:
#                 if 12 <= self.center_x % num2 <= 18:
#                     if level[(self.center_y + num3) // num1][self.center_x // num2] < 3 \
#                             or (level[(self.center_y + num3) // num1][self.center_x // num2] == 9 and (
#                             self.in_box or self.dead)):
#                         self.turns[3] = True
#                     if level[(self.center_y - num3) // num1][self.center_x // num2] < 3 \
#                             or (level[(self.center_y - num3) // num1][self.center_x // num2] == 9 and (
#                             self.in_box or self.dead)):
#                         self.turns[2] = True
#                 if 12 <= self.center_y % num1 <= 18:
#                     if level[self.center_y // num1][(self.center_x - num3) // num2] < 3 \
#                             or (level[self.center_y // num1][(self.center_x - num3) // num2] == 9 and (
#                             self.in_box or self.dead)):
#                         self.turns[1] = True
#                     if level[self.center_y // num1][(self.center_x + num3) // num2] < 3 \
#                             or (level[self.center_y // num1][(self.center_x + num3) // num2] == 9 and (
#                             self.in_box or self.dead)):
#                         self.turns[0] = True
#       else:
#             self.turns[0] = True
#             self.turns[1] = True
#       if 350 < self.x_pos < 550 and 370 < self.y_pos < 480:
#             self.in_box = True
#       else:
#             self.in_box = False
#       return self.turns, self.in_box
   
   
#    def move_clyde(self):
#         """
#         Рухає привида Clyde відповідно до його цілей та обмежень на карті гри.

#         Що робить:
#         Функція керує рухом привида Clyde залежно від його поточного напрямку та цілей.
#         Привид буде намагатися підтримувати напрямок до цілі, однак при виявленні перешкод
#         або інших обставин, він зможе обрати інший напрямок, який є доцільним.

#         Що повертає:
#         Повертає кортеж з трьома елементами:
#         - Нове значення `x_pos`, яке відповідає новому положенню привида по осі X.
#         - Нове значення `y_pos`, яке відповідає новому положенню привида по осі Y.
#         - Нове значення `direction`, яке відповідає новому напрямку руху привида.
#         """  
#       # right, left, up, down
#       #Клайд повертатиме, коли буде вигідно для того щоб переслідувати гравця
#         if self.direction == 0:
#             if self.target[0] > self.x_pos and self.turns[0]:
#                 self.x_pos += self.speed
#             elif not self.turns[0]:
#                 if self.target[1] > self.y_pos and self.turns[3]:
#                     self.direction = 3
#                     self.y_pos += self.speed
#                 elif self.target[1] < self.y_pos and self.turns[2]:
#                     self.direction = 2
#                     self.y_pos -= self.speed
#                 elif self.target[0] < self.x_pos and self.turns[1]:
#                     self.direction = 1
#                     self.x_pos -= self.speed
#                 elif self.turns[3]:
#                     self.direction = 3
#                     self.y_pos += self.speed
#                 elif self.turns[2]:
#                     self.direction = 2
#                     self.y_pos -= self.speed
#                 elif self.turns[1]:
#                     self.direction = 1
#                     self.x_pos -= self.speed
#             elif self.turns[0]:
#                 if self.target[1] > self.y_pos and self.turns[3]:
#                     self.direction = 3
#                     self.y_pos += self.speed
#                 if self.target[1] < self.y_pos and self.turns[2]:
#                     self.direction = 2
#                     self.y_pos -= self.speed
#                 else:
#                     self.x_pos += self.speed
#         elif self.direction == 1:
#             if self.target[1] > self.y_pos and self.turns[3]:
#                 self.direction = 3
#             elif self.target[0] < self.x_pos and self.turns[1]:
#                 self.x_pos -= self.speed
#             elif not self.turns[1]:
#                 if self.target[1] > self.y_pos and self.turns[3]:
#                     self.direction = 3
#                     self.y_pos += self.speed
#                 elif self.target[1] < self.y_pos and self.turns[2]:
#                     self.direction = 2
#                     self.y_pos -= self.speed
#                 elif self.target[0] > self.x_pos and self.turns[0]:
#                     self.direction = 0
#                     self.x_pos += self.speed
#                 elif self.turns[3]:
#                     self.direction = 3
#                     self.y_pos += self.speed
#                 elif self.turns[2]:
#                     self.direction = 2
#                     self.y_pos -= self.speed
#                 elif self.turns[0]:
#                     self.direction = 0
#                     self.x_pos += self.speed
#             elif self.turns[1]:
#                 if self.target[1] > self.y_pos and self.turns[3]:
#                     self.direction = 3
#                     self.y_pos += self.speed
#                 if self.target[1] < self.y_pos and self.turns[2]:
#                     self.direction = 2
#                     self.y_pos -= self.speed
#                 else:
#                     self.x_pos -= self.speed
#         elif self.direction == 2:
#             if self.target[0] < self.x_pos and self.turns[1]:
#                 self.direction = 1
#                 self.x_pos -= self.speed
#             elif self.target[1] < self.y_pos and self.turns[2]:
#                 self.direction = 2
#                 self.y_pos -= self.speed
#             elif not self.turns[2]:
#                 if self.target[0] > self.x_pos and self.turns[0]:
#                     self.direction = 0
#                     self.x_pos += self.speed
#                 elif self.target[0] < self.x_pos and self.turns[1]:
#                     self.direction = 1
#                     self.x_pos -= self.speed
#                 elif self.target[1] > self.y_pos and self.turns[3]:
#                     self.direction = 3
#                     self.y_pos += self.speed
#                 elif self.turns[1]:
#                     self.direction = 1
#                     self.x_pos -= self.speed
#                 elif self.turns[3]:
#                     self.direction = 3
#                     self.y_pos += self.speed
#                 elif self.turns[0]:
#                     self.direction = 0
#                     self.x_pos += self.speed
#             elif self.turns[2]:
#                 if self.target[0] > self.x_pos and self.turns[0]:
#                     self.direction = 0
#                     self.x_pos += self.speed
#                 elif self.target[0] < self.x_pos and self.turns[1]:
#                     self.direction = 1
#                     self.x_pos -= self.speed
#                 else:
#                     self.y_pos -= self.speed
#         elif self.direction == 3:
#             if self.target[1] > self.y_pos and self.turns[3]:
#                 self.y_pos += self.speed
#             elif not self.turns[3]:
#                 if self.target[0] > self.x_pos and self.turns[0]:
#                     self.direction = 0
#                     self.x_pos += self.speed
#                 elif self.target[0] < self.x_pos and self.turns[1]:
#                     self.direction = 1
#                     self.x_pos -= self.speed
#                 elif self.target[1] < self.y_pos and self.turns[2]:
#                     self.direction = 2
#                     self.y_pos -= self.speed
#                 elif self.turns[2]:
#                     self.direction = 2
#                     self.y_pos -= self.speed
#                 elif self.turns[1]:
#                     self.direction = 1
#                     self.x_pos -= self.speed
#                 elif self.turns[0]:
#                     self.direction = 0
#                     self.x_pos += self.speed
#             elif self.turns[3]:
#                 if self.target[0] > self.x_pos and self.turns[0]:
#                     self.direction = 0
#                     self.x_pos += self.speed
#                 elif self.target[0] < self.x_pos and self.turns[1]:
#                     self.direction = 1
#                     self.x_pos -= self.speed
#                 else:
#                     self.y_pos += self.speed
#         if self.x_pos < -30:
#             self.x_pos = 900
#         elif self.x_pos > 900:
#             self.x_pos - 30
#         return self.x_pos, self.y_pos, self.direction
     
     