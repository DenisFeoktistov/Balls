import pygame
from random import randint

from Application.MainWindowClasses.Field.FieldClasses.Border import Border
from Application.MainWindowClasses.Field.FieldClasses.Ball import Ball


class Field:
    RADIUS_MIN = 5
    RADIUS_MAX = 100

    SPEED_MIN = 1
    SPEED_MAX = 30

    COUNT_MIN = 1
    COUNT_MAX = 30

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

        number_of_balls = Field.COUNT_MIN + (Field.COUNT_MAX - Field.COUNT_MIN) * \
                          self.window.settings.parameters_widgets["count"].get_value() // 100

        for _ in range(number_of_balls):
            radius_val = Field.RADIUS_MIN + (Field.RADIUS_MAX - Field.RADIUS_MIN) * \
                         self.window.settings.parameters_widgets["size"].get_value() // 100
            radius = randint(Field.RADIUS_MIN, radius_val)

            delta_per = self.window.settings.parameters_widgets["cor. delta"].get_value()
            x_val = (self.width // 2 - radius - 1) * delta_per // 100
            y_val = (self.height // 2 - radius - 1) * delta_per // 100
            x = randint(self.x + self.width // 2 - x_val, self.x + self.width // 2 + x_val)
            y = randint(self.y + self.height // 2 - y_val, self.y + self.height // 2 + y_val)

            speed_val = Field.SPEED_MIN + (Field.SPEED_MAX - Field.SPEED_MIN) * \
                        self.window.settings.parameters_widgets["speed"].get_value() // 100
            vx = randint(-speed_val, speed_val)
            vy = randint(-speed_val, speed_val)
            self.balls.add(Ball(x, y, vx, vy, radius, self))

    def handle(self, event):
        pass

    def update(self):
        self.balls.update()

    def draw(self):
        self.horizontal_borders.draw(self.window.screen)
        self.vertical_borders.draw(self.window.screen)
        self.balls.draw(self.window.screen)
