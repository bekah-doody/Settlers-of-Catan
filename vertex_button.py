import pygame


class VertexButton:
    """
    This class stores data relating to vertex buttons
    Attributes:
        center(int, int)
        radius(int)
        clicked(bool)
        topleft(int, int)
        rect(Rect)
        color(int, int, int)
    """
    def __init__(self, center_x: int, center_y: int, radius: int):
        """
        Constructor of the vertex button class
        """
        x = center_x
        y = center_y
        self.center = (x, y)
        self.radius = radius
        self.clicked = False
        self.topleft = (x-radius, y-radius)
        self.rect = pygame.rect.Rect(self.topleft, (self.radius*2, self.radius*2))
        self.color = (225, 225, 225)
        self.clicked = False

    def draw(self, surface) -> bool:
        """
        Draws the vertex button using pygame
        """
        action = False
        color = self.color
        radius = self.radius

        # gets mouse position
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            # checks if mouse is on button
            # if mouse is hovering over circle then makes circle yellow
            color = (255, 255, 0)

            if pygame.mouse.get_pressed()[0] == 1:
                # if mouse is clicked down, it makes the button smaller

                radius = self.radius * 10 / 11

                if not self.clicked:
                    # sets clicked to true
                    self.clicked = True
                    action = True

            if pygame.mouse.get_pressed()[0] == 0:

                action = False

            if pygame.mouse.get_pressed()[0] == 0 and self.clicked == True:
                # returns true if buttons is clicked and released while still on button

                action = True
                self.clicked = False

        pygame.draw.circle(surface, color, self.center, radius)
        return action

