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
        # Create Sky Gradient
        self.sky_surface = pygame.Surface((self.width, self.height))
        self._create_sky_gradient()

    def _create_sky_gradient(self):
        # Deep blue (top) to Light blue (bottom)
        top_color = (0, 0, 50)
        bottom_color = (135, 206, 235)
        for y in range(self.height):
            ratio = y / self.height
            r = int(top_color[0] + (bottom_color[0] - top_color[0]) * ratio)
            g = int(top_color[1] + (bottom_color[1] - top_color[1]) * ratio)
            b = int(top_color[2] + (bottom_color[2] - top_color[2]) * ratio)
            pygame.draw.line(self.sky_surface, (r, g, b), (0, y), (self.width, y))

    def draw_game(self, jet: Jet, terrain: Terrain, radar_ceiling: float, distance: float, game_over: bool, win: bool):
        self.screen.blit(self.sky_surface, (0, 0))
        
        # Camera Logic: Keep Jet roughly in center vertically
        target_cam_y = jet.pos.y - self.height // 2
        
        # Clamp camera so we don't see above sky or too far below ground (optional)
        # For now, let's just use the target to allow following the jet deep into canyons
        camera_y = target_cam_y

        # 1. Draw Terrain with varied colors
        step = 4
        base_h = terrain.base_height
        
        for x in range(0, self.width + step, step):
            # Get height for this column (left side)
            h1 = terrain.get_height_at(x)
            # Get height for next column (right side)
            h2 = terrain.get_height_at(x + step)
            
            # Apply Camera transform
            screen_h1 = h1 - camera_y
            screen_h2 = h2 - camera_y
            
            # Determine Color based on absolute height (lower value = higher peak)
            # h1 relative to base_h
            # Peak: < base - 350
            # Rock: < base - 150
            # Grass: > base - 150
            
            val = h1
            if val < base_h - 350:
                color = (240, 240, 255) # Snow
            elif val < base_h - 150:
                color = (100, 100, 100) # Rock
            elif val < base_h - 50:
                color = (34, 139, 34)   # Forest Green
            else:
                color = (107, 142, 35)  # Olive/Dirt Green
            
            # Draw quad
            points = [
                (x, screen_h1),
                (x + step, screen_h2),
                (x + step, self.height), # Extend to bottom
                (x, self.height)
            ]
            pygame.draw.polygon(self.screen, color, points)

        # 2. Draw Radar Ceiling (fixed relative to world 0, so moves with camera)
        radar_y = radar_ceiling - camera_y
        if 0 <= radar_y <= self.height:
             pygame.draw.line(self.screen, ALERT_RED, (0, radar_y), (self.width, radar_y), 2)

        # Warning text if close to radar
        if jet.pos.y < radar_ceiling + 50:
            text = self.font.render("WARNING: RADAR DETECTION", True, ALERT_RED)
            self.screen.blit(text, (self.width//2 - 100, 50)) # Fixed on HUD
            
        # 3. Draw Jet (relative to camera)
        self._draw_jet(jet, camera_y)

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

    def _draw_jet(self, jet: Jet, camera_y: float):
        # Center of jet on screen (X is fixed)
        cx = 150
        cy = jet.pos.y - camera_y # Apply camera transform
        
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
                # Particles are stored in world space or screen space? 
                # Simplest is screen space, but then they move with camera which looks weird if cam moves fast.
                # Let's store them in world space for correctness?
                # Actually, graphics class shouldn't simulate world.
                # For this simple arcade feel, screen space (relative to jet) is fine, 
                # but we need to adjust their Y by camera_delta every frame? Too complex.
                # Let's just spawn them at current screen pos and let them drift.
                self.particles.append(Particle(tail_x, tail_y))

        # Draw particles
        for p in self.particles[:]:
            p.update()
            # If we wanted them to move with camera, we'd need to store world pos. 
            # Current Particle class is simple screen-space. It will look okay for small cam movements.
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
