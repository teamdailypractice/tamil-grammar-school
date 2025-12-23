import pygame
import random
import math
from typing import List, Tuple
from src.flight_sim.domain.models import Jet, Terrain

# Colors
DARK_GREEN = (0, 50, 0)
NEON_GREEN = (50, 255, 50)
ALERT_RED = (255, 50, 50)
SKY_BLUE = (10, 10, 30) # Dark night sky
HUD_COLOR = (0, 255, 0)

class Particle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.life = 20
        self.size = random.randint(2, 6)
        self.color = (255, random.randint(100, 200), 0) # Fire colors

    def update(self):
        self.x -= 5 # Move left relative to jet
        self.life -= 1
        self.size = max(0, self.size - 0.1)

class FlightRenderer:
    def __init__(self, screen: pygame.Surface, font: pygame.font.Font):
        self.screen = screen
        self.font = font
        self.particles: List[Particle] = []
        self.width = screen.get_width()
        self.height = screen.get_height()

    def draw_game(self, jet: Jet, terrain: Terrain, radar_ceiling: float, distance: float, game_over: bool, win: bool):
        self.screen.fill(SKY_BLUE)
        
        # 1. Draw Terrain
        terrain_points = []
        # Draw from x=0 to width with step
        step = 5
        for x in range(0, self.width + step, step):
            h = terrain.get_height_at(x)
            terrain_points.append((x, h))
        
        # Close the polygon at the bottom
        terrain_points.append((self.width, self.height))
        terrain_points.append((0, self.height))
        
        pygame.draw.polygon(self.screen, DARK_GREEN, terrain_points)
        pygame.draw.lines(self.screen, NEON_GREEN, False, terrain_points[:-(2)], 2) # Wireframe top

        # 2. Draw Radar Ceiling
        pygame.draw.line(self.screen, ALERT_RED, (0, radar_ceiling), (self.width, radar_ceiling), 1)
        # Warning text if close
        if jet.pos.y < radar_ceiling + 50:
            text = self.font.render("WARNING: RADAR DETECTION", True, ALERT_RED)
            self.screen.blit(text, (self.width//2 - 100, radar_ceiling + 10))
            # Blink effect
            if (pygame.time.get_ticks() // 200) % 2 == 0:
                 pygame.draw.rect(self.screen, (255, 0, 0, 50), (0, 0, self.width, radar_ceiling))

        # 3. Draw Jet
        self._draw_jet(jet)

        # 4. Draw HUD
        self._draw_hud(jet, distance)

        # 5. Game Over / Win
        if game_over:
            msg = "MISSION FAILED" if not win else "MISSION ACCOMPLISHED"
            color = ALERT_RED if not win else NEON_GREEN
            text = self.font.render(msg, True, color)
            self.screen.blit(text, (self.width//2 - text.get_width()//2, self.height//2))
            
            sub = self.font.render("Press R to Restart", True, (255, 255, 255))
            self.screen.blit(sub, (self.width//2 - sub.get_width()//2, self.height//2 + 40))

    def _draw_jet(self, jet: Jet):
        # Center of jet on screen (X is fixed, Y moves)
        cx, cy = 150, jet.pos.y
        
        # Rotation
        angle_rad = math.radians(jet.angle)
        cos_a = math.cos(angle_rad)
        sin_a = math.sin(angle_rad)

        def rotate_pt(x, y):
            # Rotate around 0,0 then translate to cx, cy
            rx = x * cos_a - y * sin_a
            ry = x * sin_a + y * cos_a
            return (cx + rx, cy - ry) # Screen Y is inverted (up is down) so -ry

        # Jet Shape (Triangle-ish)
        points = [
            rotate_pt(20, 0),   # Nose
            rotate_pt(-10, 10), # Left Wing
            rotate_pt(-5, 0),   # Tail center
            rotate_pt(-10, -10) # Right Wing
        ]
        
        pygame.draw.polygon(self.screen, (200, 200, 200), points)
        pygame.draw.lines(self.screen, (255, 255, 255), True, points, 2)

        # Afterburner particles
        if jet.thrust_power > 0.1:
            # Emit particles from tail
            tail_x, tail_y = rotate_pt(-10, 0)
            for _ in range(int(jet.thrust_power * 5)):
                self.particles.append(Particle(tail_x, tail_y))

        # Draw particles
        for p in self.particles[:]:
            p.update()
            if p.life <= 0:
                self.particles.remove(p)
            else:
                pygame.draw.circle(self.screen, p.color, (int(p.x), int(p.y)), int(p.size))

    def _draw_hud(self, jet: Jet, distance: float):
        # Speed Bar
        speed_ratio = (jet.vel.x / jet.MAX_SPEED)
        pygame.draw.rect(self.screen, (50, 50, 50), (20, 20, 200, 20))
        pygame.draw.rect(self.screen, NEON_GREEN, (20, 20, 200 * speed_ratio, 20))
        self.screen.blit(self.font.render("THRUST", True, NEON_GREEN), (20, 45))

        # Altitude
        alt_text = self.font.render(f"ALT: {int(self.height - jet.pos.y)}", True, NEON_GREEN)
        self.screen.blit(alt_text, (20, 70))

        # Distance
        dist_text = self.font.render(f"DIST: {int(distance)}m / 10000m", True, NEON_GREEN)
        self.screen.blit(dist_text, (self.width - 300, 20))
