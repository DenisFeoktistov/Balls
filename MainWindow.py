import pygame


class MainWindow:
    SIZE = WIDTH, HEIGHT = 1000, 600
    FPS = 120

    def __init__(self):
        self.screen = pygame.display.set_mode(MainWindow.SIZE)
        self.time = pygame.time.Clock()

    def show(self):
        self.start_cycle()

    def start_cycle(self):
        running = True
        while running:
            self.time.tick(self.FPS)
            pygame.display.flip()
