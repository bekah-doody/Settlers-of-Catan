import pygame.mouse


class Road:
    def __init__(self, start_pos, end_pos):
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.color = (210, 180, 140)
        self.width = 8
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


        if min_x+10 <= pos[0] <= max_x-10 and min_y+10 <= pos[1] <= max_y-10 and self.claimed == False and pygame.mouse.get_pressed()[0] == 1:
            self.claimed = True
            self.color = (255,0,0)
            return True
        if(x1 == x2 and min_x <= pos[0] <= max_x and min_y <= pos[1] <= max_y and self.claimed == False and pygame.mouse.get_pressed()[0] == 1):
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

        if min_x+10 <= mouse_x <= max_x-10 and min_y+10 <= mouse_y <= max_y-10:
            self.claimed = True
            self.color = (255, 0, 0)  # Change color to indicate it's claimed
