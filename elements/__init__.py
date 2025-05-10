import pygame.draw


class Button:
    def __init__(self, label, position):
        self.screen = pygame.display.get_surface()
        self.label = label
        self.position = position
        self.color = (0, 0, 255)  # Blue color for the button
        self.size  = (100, 50)
        self.font = pygame.font.SysFont("roboto", 25)
    def render(self):
        # Code to render the button on the screen
        # Draw the button rectangle
        pygame.draw.rect(self.screen ,self.color , (*self.position,*self.label))
        # render the button label
        text_surface = self.font.render(self.label, True,self.color)
        text_rect = text_surface.get_rect(center=(self.position[0] + self.size[0] // 2,
                                                  self.position[1] + self.size[1] // 2))
        self.screen.blit(text_surface, text_rect)

        pass

    def on_click(self):
        # Code to handle button click
        pass


class Label:
    def __init__(self, text, position):
        self.text = text
        self.position = position

    def render(self):
        # Code to render the label on the screen
        pass