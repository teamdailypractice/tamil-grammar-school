import pygame
from typing import Tuple, Optional, Dict
from src.myproject.domain.models import Grid, Gem, GemType

# Color definitions
COLORS = {
    GemType.RED: (255, 80, 80),      # Soft Red
    GemType.GREEN: (80, 255, 80),    # Soft Green
    GemType.BLUE: (80, 80, 255),     # Soft Blue
    GemType.YELLOW: (255, 255, 80),  # Soft Yellow
    GemType.PURPLE: (200, 80, 255),  # Soft Purple
    GemType.ORANGE: (255, 160, 60),  # Soft Orange
}

BACKGROUND_COLOR = (40, 40, 50)
GRID_COLOR = (60, 60, 70)
HIGHLIGHT_COLOR = (255, 255, 255)

class GameRenderer:
    CELL_SIZE = 64
    MARGIN = 50  # Margin around the grid

    def __init__(self, screen: pygame.Surface, font: pygame.font.Font):
        self.screen = screen
        self.font = font
        self.offset_x = (screen.get_width() - (Grid.WIDTH * self.CELL_SIZE)) // 2
        self.offset_y = (screen.get_height() - (Grid.HEIGHT * self.CELL_SIZE)) // 2

    def draw_game(self, grid: Grid, selected_cell: Optional[Tuple[int, int]] = None, score: int = 0):
        self.screen.fill(BACKGROUND_COLOR)
        
        # Draw Score
        score_text = self.font.render(f"Score: {score}", True, (255, 255, 255))
        self.screen.blit(score_text, (20, 20))

        # Draw Grid Background
        for y in range(Grid.HEIGHT):
            for x in range(Grid.WIDTH):
                rect = pygame.Rect(
                    self.offset_x + x * self.CELL_SIZE,
                    self.offset_y + y * self.CELL_SIZE,
                    self.CELL_SIZE,
                    self.CELL_SIZE
                )
                pygame.draw.rect(self.screen, GRID_COLOR, rect, 1)

        # Draw Gems
        for y in range(Grid.HEIGHT):
            for x in range(Grid.WIDTH):
                gem = grid.get_gem(x, y)
                if gem:
                    self._draw_gem(gem, x, y, selected=(selected_cell == (x, y)))

    def _draw_gem(self, gem: Gem, x: int, y: int, selected: bool):
        center_x = self.offset_x + x * self.CELL_SIZE + self.CELL_SIZE // 2
        center_y = self.offset_y + y * self.CELL_SIZE + self.CELL_SIZE // 2
        radius = (self.CELL_SIZE // 2) - 8
        color = COLORS.get(gem.type, (255, 255, 255))

        if gem.type == GemType.RED: # Heart
            # Simple heart shape using two circles and a triangle
            r = radius // 2
            pygame.draw.circle(self.screen, color, (center_x - r + 4, center_y - r), r)
            pygame.draw.circle(self.screen, color, (center_x + r - 4, center_y - r), r)
            points = [
                (center_x - 2 * r + 4, center_y - r + 5),
                (center_x + 2 * r - 4, center_y - r + 5),
                (center_x, center_y + radius),
            ]
            pygame.draw.polygon(self.screen, color, points)

        elif gem.type == GemType.GREEN: # Square (Rounded)
            rect_size = radius * 1.6
            rect = pygame.Rect(center_x - rect_size//2, center_y - rect_size//2, rect_size, rect_size)
            pygame.draw.rect(self.screen, color, rect, border_radius=8)

        elif gem.type == GemType.BLUE: # Diamond
            points = [
                (center_x, center_y - radius),
                (center_x + radius, center_y),
                (center_x, center_y + radius),
                (center_x - radius, center_y),
            ]
            pygame.draw.polygon(self.screen, color, points)

        elif gem.type == GemType.YELLOW: # Star
            points = []
            import math
            outer_radius = radius
            inner_radius = radius * 0.4
            for i in range(10):
                angle = i * 36 # 360 / 10
                r = outer_radius if i % 2 == 0 else inner_radius
                # Rotate by -90 deg (math.pi/2) to point up
                rad = math.radians(angle - 90)
                px = center_x + r * math.cos(rad)
                py = center_y + r * math.sin(rad)
                points.append((int(px), int(py)))
            pygame.draw.polygon(self.screen, color, points)

        elif gem.type == GemType.PURPLE: # Circle
            pygame.draw.circle(self.screen, color, (center_x, center_y), radius)

        elif gem.type == GemType.ORANGE: # Triangle
            points = [
                (center_x, center_y - radius),
                (center_x + radius, center_y + radius),
                (center_x - radius, center_y + radius),
            ]
            pygame.draw.polygon(self.screen, color, points)
        
        else: # Fallback Circle
            pygame.draw.circle(self.screen, color, (center_x, center_y), radius)

        # Draw generic shine/highlight on all shapes to keep the style
        pygame.draw.circle(self.screen, (255, 255, 255), (center_x - radius//3, center_y - radius//3), 3)

        if selected:
            pygame.draw.rect(self.screen, HIGHLIGHT_COLOR, 
                           (self.offset_x + x * self.CELL_SIZE, self.offset_y + y * self.CELL_SIZE, self.CELL_SIZE, self.CELL_SIZE), 
                           3, border_radius=5)

    def get_grid_coords(self, mouse_pos: Tuple[int, int]) -> Optional[Tuple[int, int]]:
        mx, my = mouse_pos
        
        rel_x = mx - self.offset_x
        rel_y = my - self.offset_y
        
        if rel_x < 0 or rel_y < 0:
            return None
            
        grid_x = rel_x // self.CELL_SIZE
        grid_y = rel_y // self.CELL_SIZE
        
        if 0 <= grid_x < Grid.WIDTH and 0 <= grid_y < Grid.HEIGHT:
            return (grid_x, grid_y)
        return None
