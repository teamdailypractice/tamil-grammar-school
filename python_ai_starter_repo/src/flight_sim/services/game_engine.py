import pygame
from src.flight_sim.domain.models import Jet, Terrain
from src.flight_sim.infrastructure.graphics import FlightRenderer

class FlightSimEngine:
    def __init__(self):
        pygame.init()
        self.width = 1000
        self.height = 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Stealth Canyon Run")
        
        self.font = pygame.font.Font(None, 36)
        self.renderer = FlightRenderer(self.screen, self.font)
        self.clock = pygame.time.Clock()
        self.running = True
        
        self.reset_game()

    def reset_game(self):
        self.jet = Jet(150, 300) # Fixed X, Start Y
        self.terrain = Terrain(self.width, self.height)
        self.distance = 0.0
        self.game_over = False
        self.win = False
        self.radar_ceiling = 100 # Top 100 pixels is death zone

    def run(self):
        while self.running:
            self.handle_events()
            if not self.game_over and not self.win:
                self.update()
            self.draw()
            self.clock.tick(60)
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if (self.game_over or self.win) and event.key == pygame.K_r:
                    self.reset_game()

        # Continuous Input
        keys = pygame.key.get_pressed()
        if not self.game_over and not self.win:
            if keys[pygame.K_UP]:
                self.jet.rotate(-1)
            if keys[pygame.K_DOWN]:
                self.jet.rotate(1)
            
            # Auto-center slightly if no key pressed? No, let it be manual.
            
            if keys[pygame.K_SPACE] or keys[pygame.K_w]:
                self.jet.set_thrust(1.0)
            else:
                self.jet.set_thrust(0.0)

    def update(self):
        self.jet.update()
        
        # Horizontal movement is relative (terrain moves left)
        ground_speed = self.jet.vel.x * 5 # Scale for visual scrolling
        self.terrain.update(ground_speed)
        self.distance += ground_speed

        # Collision Checks
        
        # 1. Radar Ceiling
        if self.jet.pos.y < self.radar_ceiling:
            self.game_over = True
            print("Detected by Radar!")

        # 2. Terrain Collision
        # Check collision at jet's position (x=150)
        # We check a few points for the jet body
        jet_x = 150
        ground_h = self.terrain.get_height_at(jet_x)
        
        if self.jet.pos.y > ground_h - 10: # Simple point check with margin
            self.game_over = True
            print("Crashed into terrain!")

        # 3. Win Condition
        if self.distance > 10000:
            self.win = True

    def draw(self):
        self.renderer.draw_game(
            self.jet, 
            self.terrain, 
            self.radar_ceiling, 
            self.distance, 
            self.game_over, 
            self.win
        )
        pygame.display.flip()
