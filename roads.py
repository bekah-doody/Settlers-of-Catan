import pygame.mouse


class Road:
    def __init__(self, start_pos, end_pos):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.color = (150, 150, 150)
        self.width = 5
        self.claimed = False

    def draw(self, screen):
        pos = pygame.mouse.get_pos()
        # Check if the mouse click is within the bounding box of the road
        x1, y1 = self.start_pos
        x2, y2 = self.end_pos
        min_x = min(x1, x2) - self.width / 2
        max_x = max(x1, x2) + self.width / 2
        min_y = min(y1, y2) - self.width / 2
        max_y = max(y1, y2) + self.width / 2


        if min_x <= pos[0] <= max_x and min_y <= pos[1] <= max_y and self.claimed == False and pygame.mouse.get_pressed()[0] == 1:
            self.claimed = True
            self.color = (255,0,0)
            return True

        pygame.draw.line(screen, self.color, self.start_pos, self.end_pos, self.width)
        return False

    def click(self, mouse_pos):
        # Get the coordinates of the mouse click
        mouse_x, mouse_y = mouse_pos

        # Check if the mouse click is within the bounding box of the road
        x1, y1 = self.start_pos
        x2, y2 = self.end_pos
        min_x = min(x1, x2) - self.width / 2
        max_x = max(x1, x2) + self.width / 2
        min_y = min(y1, y2) - self.width / 2
        max_y = max(y1, y2) + self.width / 2

        if min_x <= mouse_x <= max_x and min_y <= mouse_y <= max_y:
            self.claimed = True
            self.color = (255, 0, 0)  # Change color to indicate it's claimed
