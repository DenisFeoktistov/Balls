import pygame


from Field import Field
from Settings import Settings


class MainWindow:
    SIZE = WIDTH, HEIGHT = 1000, 600
    FPS = 120

    def __init__(self):
        self.screen = pygame.display.set_mode(MainWindow.SIZE)
        self.time = pygame.time.Clock()

        self.field = Field(self)
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
            pygame.display.flip()

    def update_screen(self):
        self.screen.fill((0, 0, 0))

        self.draw()
        self.settings.draw()
        self.field.draw()

    def draw(self):
        pass

    def handle(self, event):
        self.field.handle(event)
        self.settings.handle(event)

    def update(self):
        self.field.update()
        self.settings.update()
