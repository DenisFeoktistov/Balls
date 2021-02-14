import pygame


class Settings:
    def __init__(self, window, x, y, width, height):
        self.window = window
        self.window = window

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.create_interface()

    def create_interface(self):
        self.create_restart_button()

    def create_restart_button(self):
        font = pygame.font.Font(None, 70)
        self.restart_text = font.render('REGENERATE', False, (255, 255, 255))
        self.restart_rect = self.restart_text.get_rect()
        self.restart_rect.center = (self.x + self.width / 2, self.y + self.height * 0.9)

    def handle(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.restart_rect.collidepoint(event.pos):
            self.restart()

    def restart(self):
        self.window.field.restart()

    def update(self):
        pass

    def draw(self):
        self.draw_buttons()

    def draw_buttons(self):
        self.window.screen.blit(self.restart_text, self.restart_rect)

