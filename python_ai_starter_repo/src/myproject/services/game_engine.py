import pygame
import time
from typing import Optional, Tuple
from src.myproject.domain.models import Grid
from src.myproject.infrastructure.graphics import GameRenderer

class GameEngine:
    def __init__(self):
        pygame.init()
        self.width = 800
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Gem Shuffle")
        
        self.font = pygame.font.Font(None, 36)
        self.renderer = GameRenderer(self.screen, self.font)
        self.grid = Grid()
        self.clock = pygame.time.Clock()
        self.running = True
        
        self.selected_cell: Optional[Tuple[int, int]] = None
        self.score = 0
        self.is_processing = False

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not self.is_processing:
                if event.button == 1:  # Left click
                    self.handle_click(event.pos)

    def handle_click(self, pos: Tuple[int, int]):
        coords = self.renderer.get_grid_coords(pos)
        if not coords:
            self.selected_cell = None
            return

        if self.selected_cell is None:
            self.selected_cell = coords
        else:
            # Second click - try swap
            x1, y1 = self.selected_cell
            x2, y2 = coords
            
            # Check adjacency
            if abs(x1 - x2) + abs(y1 - y2) == 1:
                self.grid.swap_gems(x1, y1, x2, y2)
                # Check if swap results in a match
                matches = self.grid.find_matches()
                if matches:
                    self.is_processing = True
                    self.selected_cell = None
                else:
                    # Invalid swap (no match), swap back
                    # In a polished game we'd animate this, here we just instantaneous swap back
                    # Optional: Add delay or animation
                    self.grid.swap_gems(x1, y1, x2, y2)
                    self.selected_cell = coords # Select the new one instead? Or deselect? Let's select new.
            else:
                self.selected_cell = coords

    def update(self):
        if self.is_processing:
            # Cascading logic
            matches = self.grid.find_matches()
            if matches:
                # 1. Remove matches
                self.score += len(matches) * 10
                self.grid.remove_gems(matches)
                self.draw() # Force redraw to show empty
                pygame.display.flip()
                pygame.time.delay(300) # Small delay for "animation"

                # 2. Gravity
                self.grid.apply_gravity()
                self.draw()
                pygame.display.flip()
                pygame.time.delay(300)

                # 3. Fill
                self.grid.fill_empty()
                self.draw() # Show the filled board
                pygame.display.flip()
                pygame.time.delay(300) # Pause so user sees the new gems
                # Loop continues next update
            else:
                self.is_processing = False

    def draw(self):
        self.renderer.draw_game(self.grid, self.selected_cell, self.score)
        pygame.display.flip()
