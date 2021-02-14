import pygame


class Border(pygame.sprite.Sprite):
    COLOR = (0, 0, 0)

    def __init__(self, x1, y1, x2, y2):
        super().__init__()
        self.image = pygame.Surface([abs(x2 - x1), abs(y2 - y1)])
        self.rect = pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))

        self.image.fill(color=Border.COLOR)
