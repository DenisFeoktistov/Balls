import pygame
from random import randint

from MainWindow.MainWindowClasses.Field.FieldClasses.Border import Border
from MainWindow.MainWindowClasses.Field.FieldClasses.Ball import Ball


class Field:
    def __init__(self, window, x, y, width, height, line_width, count_of_balls):
        self.window = window

        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.line_width = line_width
        self.count_of_balls = count_of_balls

        self.generate_components()

    def restart(self):
        self.generate_components()

    def generate_components(self):
        self.add_borders()
        self.add_balls()

    def add_borders(self):
        self.horizontal_borders = pygame.sprite.Group()
        self.vertical_borders = pygame.sprite.Group()

        self.vertical_borders.add(Border(self.x, self.y, self.x + self.line_width, self.y + self.height))
        self.vertical_borders.add(
            Border(self.x + self.width, self.y, self.x + self.width + self.line_width, self.y + self.height))
        self.horizontal_borders.add(Border(self.x, self.y, self.x + self.width, self.y + self.line_width))
        self.horizontal_borders.add(
            Border(self.x, self.y + self.height, self.x + self.width, self.y + self.height + self.line_width))

    def add_balls(self):
        self.balls = pygame.sprite.Group()

        for _ in range(self.count_of_balls):
            radius = randint(15, 30)
            x = randint(self.x + 1, self.x + self.width - 2 * radius - 1)
            y = randint(self.y + 1, self.y + self.height - 2 * radius - 1)
            vx = randint(-5, 5)
            vy = randint(-5, 5)
            self.balls.add(Ball(x, y, vx, vy, radius, self))

    def handle(self, event):
        pass

    def update(self):
        self.balls.update()

    def draw(self):
        self.horizontal_borders.draw(self.window.screen)
        self.vertical_borders.draw(self.window.screen)
        self.balls.draw(self.window.screen)
