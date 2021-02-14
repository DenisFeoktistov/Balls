import pygame

from Field import Field
from Settings import Settings


class MainWindow:
    SIZE = WIDTH, HEIGHT = 1000, 600
    FPS = 120

    FIELD_X = WIDTH * 0.02
    FIELD_Y = SETTINGS_y = HEIGHT * 0.02

    FIELD_WIDTH = (WIDTH - FIELD_X * 2) / 2
    FIELD_HEIGHT = SETTINGS_HEIGHT = (HEIGHT - FIELD_Y * 2)
    FIELD_LINE_WIDTH = 3

    def __init__(self):
        self.screen = pygame.display.set_mode(MainWindow.SIZE)
        self.time = pygame.time.Clock()

        self.field = Field(window=self, x=MainWindow.FIELD_X, y=MainWindow.FIELD_Y, width=MainWindow.FIELD_WIDTH,
                           height=MainWindow.FIELD_HEIGHT,
                           line_width=MainWindow.FIELD_LINE_WIDTH)
        self.settings = Settings(self)

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

    def update(self):
        self.field.update()
        self.settings.update()
