from main import powerup, eaten_ghost, screen, spooked_img, dead_img
import pygame
class Ghost:
   def __init__(self, x_coord, y_coord, target, speed, img, direct, dead, box, id):
        """
        Ініціалізує об'єкт Ghost з вказаними параметрами.

        Параметри:
        - x_coord: Координата X положення Ghost.
        - y_coord: Координата Y положення Ghost.
        - target: Ціль, до якої прямує Ghost.
        - speed: Швидкість Ghost.
        - img: Зображення Ghost.
        - direct: Напрямок руху Ghost.
        - dead: Прапорець, що вказує, чи мертвий Ghost.
        - box: Прапорець, що вказує, чи знаходиться Ghost в коробці.
        - id: Ідентифікатор Ghost.
        """
        self.x_pos = x_coord
        self.y_pos = y_coord
        self.center_x = self.x_pos + 22
        self.center_y = self.y_pos + 22
        self.target = target
        self.speed = speed
        self.img = img
        self.direction = direct
        self.dead = dead
        self.in_box = box
        self.id = id
        self.turns, self.in_box = self.check_collisions()
        self.rect = self.draw()
        
        
   def draw(self):
      """
      Малює привид на екрані залежно від його поточного стану.

      Параметри:
      - self: Екземпляр класу привида.
    
      Що робить:
      Функція відповідає за малювання зображення привида на екрані відповідно до його поточного стану. 
      Залежно від наявності активного powerup та стану привида (живий, мертвий, в стані паніки), 
      вона вибирає відповідне зображення для малювання.

      Що повертає:
      Повертає прямокутник, який обмежує область, де знаходиться привид на екрані. Це може бути
      корисно для подальшої обробки зіткнень або інших операцій гри. Якщо привид не малюється
      на екрані у поточному стані, повертається None.
      """
      if (not powerup and not self.dead) or (eaten_ghost[self.id] and powerup and not self.dead):
         screen.blit(self.img, (self.x_pos, self.y_pos))
      elif powerup and not self.dead and not eaten_ghost[self.id]:
         screen.blit(spooked_img, (self.x_pos, self.y_pos))
      else:
         screen.blit(dead_img, (self.x_pos, self.y_pos))
         ghost_rect = pygame.rect.Rect((self.center_x - 18, self.center_y - 18), (36, 36))
      return ghost_rect

        
        
       