# filepath: /keyboard-screen-manager/keyboard-screen-manager/src/main.py

import pygame
from elements import Button, Label
from input import listen_for_input
from utils import load_resources

# from utils import get_screen_dimensions, center_element
class ScreenManager:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        self.clock = pygame.time.Clock()
        self.elements = []
        self.running = True

#self.load_resources()
    def add_element(self, element):
        self.elements.append(element)

# render method
    def render(self):
        self.screen.fill((255, 255, 255))
        for element in self.elements:
            element.render(self.screen)
        pygame.display.flip()

# handle_input method
    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                listen_for_input(event.key)

#    def load_resources(self):
    def main_loop(self):
        while self.running:
            self.handle_input()
            self.render()
            self.clock.tick(60)

if __name__ == "__main__":
    manager = ScreenManager()
    # Example elements
    button = Button("Click Me", (100, 100))
    label = Label("Hello, World!", (100, 200))
    manager.add_element(button)
    manager.add_element(label)
    manager.main_loop()
    pygame.quit()