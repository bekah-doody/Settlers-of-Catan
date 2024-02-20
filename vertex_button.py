import pygame


class VertexButton:
    def __init__(self, center_x, center_y, radius):
        x = center_x
        y = center_y
        self.center = (x, y)
        self.radius = radius
        self.clicked = False
        self.topleft = (x-radius, y-radius)
        self.rect = pygame.rect.Rect(self.topleft, (self.radius*2, self.radius*2))
        self.color = (225, 225, 225)

    def draw(self, surface) -> bool:
        clicked = False
        action = False
        color = self.color
        radius = self.radius
        # gets mouse position
        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            # checks if mouse is on button
            color = (255, 255, 0)
            if pygame.mouse.get_pressed()[0] == 1:
                # if mouse is clicked down, it makes the button smaller

                radius = self.radius * 10 / 11

                if not clicked:
                    # sets clicked to true

                    clicked = True

            if pygame.mouse.get_pressed()[0] == 0:
                # if mouse is hovering over circle then makes circle yellow

                pygame.draw.circle(surface, (200, 200, 0), self.center, self.radius, )
                action = False

            if pygame.mouse.get_pressed()[0] == 0 and clicked == True:
                # returns true if buttons is clicked and released while still on button

                action = True
                clicked = False

        pygame.draw.circle(surface, color, self.center, radius)
        return action

