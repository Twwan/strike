from images import *


class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed_x = 8
        self.speed_x2 = -8
        self.speed_y = 0

    def move(self):
        self.x += self.speed_x
        if self.x <= display_width:
            display.blit(bullet_img, (self.x, self.y))
            return True
        else:
            return False

    def move2(self):
        self.x -= self.speed_x
        if self.x >= 0:
            display.blit(bullet_img2, (self.x, self.y))
            return True
        else:
            return False
