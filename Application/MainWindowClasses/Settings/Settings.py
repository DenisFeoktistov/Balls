import pygame


class ParameterWidget:
    def __init__(self, x, y, width, height, text, font_size, value):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.font_size = font_size
        self.value = value

        self.create_interface()

    def create_interface(self):
        self.create_arrows()
        self.create_text()

    def create_arrows(self):
        self.up_button = pygame.image.load('data/pictures/backgrounds/purple_background1.jpg')
        self.up_button = pygame.transform.scale(
            self.up_button, (self.width * 0.1, self.height * 0.4))
        self.up_rect = self.up_button.get_rect()

        self.down_button = pygame.image.load('data/pictures/backgrounds/purple_background1.jpg')
        self.down_button = pygame.transform.scale(
            self.down_button, (self.width * 0.1, self.height * 0.4))
        self.down_button = pygame.transform.rotate(self.down_button, 90)
        self.down_rect = self.down_button.get_rect()

    def create_text(self):
        font = pygame.font.Font(None, self.font_size)
        self.parameter_text = font.render(self.text, False, (255, 255, 255))

    def create_value_text(self):
        font = pygame.font.Font(None, self.font_size)
        self.value_text = font.render(self.value, False, (255, 255, 255))

    def update(self):
        if pygame.mouse.get_pressed(1) and self.up_rect.collidepoint(pygame.mouse.get_pos()):
            self.value += 1
        if pygame.mouse.get_pressed(1) and self.down_rect.collidepoint(pygame.mouse.get_pos()):
            self.value -= 1
        self.create_value_text()


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

