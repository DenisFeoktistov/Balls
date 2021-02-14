import pygame


from Application.MainWindow import MainWindow


class App:
    def __init__(self):
        self.main_window = MainWindow()

    def show(self):
        self.main_window.show()


if __name__ == '__main__':
    pygame.init()
    pygame.font.init()

    app = App()
    app.show()

    pygame.quit()
    pygame.font.quit()
