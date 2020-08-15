from typing import Any, Union

import pygame
import random


class ENEMY:

    def __init__(self):
        img = "Enemy.png"
        self.enemyimg = pygame.image.load(img)
        self.enemyx = random.randint(84, 500)
        self.enemyy = random.randint(20, 200)
        if self.enemyx < 733:
            self.enemy_change = True
        else:
            self.enemy_change = False


