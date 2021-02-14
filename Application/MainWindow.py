import pygame
import sys

from Application.MainWindowClasses.Field.Field import Field
from Application.MainWindowClasses.Settings.Settings import Settings


class MainWindow:
    SIZE = WIDTH, HEIGHT = 1000, 600
    FPS = 120

    FIELD_X = WIDTH * 0.02
    FIELD_Y = SETTINGS_Y = HEIGHT * 0.02

    FIELD_WIDTH = WIDTH * 0.48
    FIELD_HEIGHT = SETTINGS_HEIGHT = (HEIGHT - FIELD_Y * 2)
    FIELD_LINE_WIDTH = 3

    SETTINGS_X = WIDTH * 0.52
    SETTINGS_WIDTH = WIDTH * 0.48

    def __init__(self):
        self.screen = pygame.display.set_mode(MainWindow.SIZE)
        self.time = pygame.time.Clock()

        count_of_balls = 10
        self.field = Field(window=self, x=MainWindow.FIELD_X, y=MainWindow.FIELD_Y, width=MainWindow.FIELD_WIDTH,
                           height=MainWindow.FIELD_HEIGHT,
                           line_width=MainWindow.FIELD_LINE_WIDTH, count_of_balls=count_of_balls)
        self.settings = Settings(window=self, x=MainWindow.SETTINGS_X, y=MainWindow.SETTINGS_Y,
                                 width=MainWindow.SETTINGS_WIDTH, height=MainWindow.SETTINGS_HEIGHT)

    def show(self):
        self.start_cycle()

    def start_cycle(self):
        running = True

        while running:
            for event in pygame.event.get():
                self.handle(event)

            self.time.tick(self.FPS)

            self.update()
            self.update_screen()
            self.draw()
            pygame.display.flip()

    def update_screen(self):
        self.screen.fill((120, 120, 120))

    def draw(self):
        self.field.draw()
        self.settings.draw()

    def handle(self, event):
        self.field.handle(event)
        self.settings.handle(event)

        if event.type == pygame.QUIT:
            self.terminate()

    def update(self):
        self.field.update()
        self.settings.update()

    def terminate(self):
        pygame.quit()
        sys.exit()
