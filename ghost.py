import main
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
        
        
       