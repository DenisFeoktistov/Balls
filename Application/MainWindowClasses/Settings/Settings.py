import pygame


class ParameterWidget:
    FONT_SIZE = 50

    def __init__(self, x, y, width, height, text, value):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.value = value

        self.create_interface()

    def create_interface(self):
        self.create_arrows()
        self.create_parameter_text()
        self.create_value_text()

    def create_arrows(self):
        self.up_button = pygame.image.load('data/pictures/triangle_2.png')
        self.up_button = pygame.transform.scale(
            self.up_button, (int(self.width * 0.2), int(self.height * 0.4)))
        self.up_rect = self.up_button.get_rect()
        self.up_rect.x = self.x + int(self.width * 0.35)
        self.up_rect.bottom = self.y + int(self.height * 0.5)

        self.down_button = pygame.image.load('data/pictures/triangle_2.png')
        self.down_button = pygame.transform.scale(
            self.down_button, (int(self.width * 0.2), int(self.height * 0.4)))
        self.down_button = pygame.transform.rotate(self.down_button, 180)
        self.down_rect = self.down_button.get_rect()
        self.down_rect.x = self.x + int(self.width * 0.35)
        self.down_rect.top = self.y + int(self.height * 0.5)

    def create_parameter_text(self):
        font = pygame.font.Font(None, ParameterWidget.FONT_SIZE)
        self.parameter_text = font.render(self.text, False, (255, 255, 255))
        self.parameter_text_rect = self.parameter_text.get_rect()
        self.parameter_text_rect.center = (self.x + int(self.width * 0.1), self.y + int(self.height * 0.5))

    def create_value_text(self):
        font = pygame.font.Font(None, ParameterWidget.FONT_SIZE)
        self.value_text = font.render(f'{self.value}%', False, (255, 255, 255))
        self.value_text_rect = self.value_text.get_rect()
        self.value_text_rect.center = (self.x + int(self.width * 0.7), self.y + int(self.height * 0.5))

    def update(self):
        if pygame.mouse.get_pressed(3)[0] and self.up_rect.collidepoint(pygame.mouse.get_pos()):
            self.value = min(100, self.value + 1)
        if pygame.mouse.get_pressed(3)[0] and self.down_rect.collidepoint(pygame.mouse.get_pos()):
            self.value = max(0, self.value - 1)
        self.create_value_text()

    def draw(self, screen):
        screen.blit(self.up_button, self.up_rect)
        screen.blit(self.down_button, self.down_rect)
        screen.blit(self.parameter_text, self.parameter_text_rect)
        screen.blit(self.value_text, self.value_text_rect)

    def get_value(self):
        return self.value


class Settings:
    def __init__(self, window, x, y, width, height, parameters, parameters_default):
        self.window = window

        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.parameters = parameters
        self.parameters_default = parameters_default

        self.create_interface()

    def create_interface(self):
        self.create_restart_button()
        self.create_parameters_widgets()

    def create_parameters_widgets(self):
        self.parameters_widgets = dict()

        for i, key in enumerate(self.parameters):
            self.parameters_widgets[key] = ParameterWidget(x=self.x + self.width * 0.2,
                                                           y=self.y + self.y * 0.2 + i * (self.height * 0.8 / (
                                                               len(self.parameters_default))),
                                                           width=self.width * 0.6,
                                                           height=(self.height / (len(self.parameters_default))) * 0.8,
                                                           text=key, value=self.parameters_default[key])

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
        for key in self.parameters_widgets:
            self.parameters_widgets[key].update()

    def draw(self):
        self.draw_buttons()
        self.draw_widgets()

    def draw_widgets(self):
        for key in self.parameters_widgets:
            self.parameters_widgets[key].draw(self.window.screen)

    def draw_buttons(self):
        self.window.screen.blit(self.restart_text, self.restart_rect)
