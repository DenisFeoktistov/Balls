import pygame


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, vx, vy, radius, field):
        self.field = field

        super().__init__()
        self.image = pygame.Surface((2 * radius, 2 * radius),
                                    pygame.SRCALPHA, 32)
        pygame.draw.circle(self.image, pygame.Color("red"),
                           (radius, radius), radius)
        self.rect = pygame.Rect(x, y, 2 * radius, 2 * radius)
        self.vx = vx
        self.vy = vy

    def update(self):
        self.rect = self.rect.move(self.vx, self.vy)

        if pygame.sprite.spritecollideany(self, self.field.horizontal_borders):
            self.vy = -self.vy
        if pygame.sprite.spritecollideany(self, self.field.vertical_borders):
            self.vx = -self.vx
