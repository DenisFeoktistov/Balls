import pygame


from Border import Border


class Field:
    def __init__(self, window, x, y, width, height, line_width):
        self.window = window

        self.add_borders(x, y, width, height, line_width)

    def add_borders(self, x, y, width, height, line_width):
        self.horizontal_borders = pygame.sprite.Group()
        self.vertical_borders = pygame.sprite.Group()

        self.vertical_borders.add(Border(x, y, x + line_width, y + height))
        self.vertical_borders.add(Border(x + width, y, x + width + line_width, y + height))
        self.horizontal_borders.add(Border(x, y, x + width, y + line_width))
        self.horizontal_borders.add(Border(x, y + height, x + width, y + height + line_width))

    def handle(self, event):
        pass

    def update(self):
        pass

    def draw(self):
        self.horizontal_borders.draw(self.window.screen)
        self.vertical_borders.draw(self.window.screen)
