import numpy as np
import random
from dataclasses import dataclass

@dataclass
class Vector2:
    x: float
    y: float

class Jet:
    def __init__(self, x: float, y: float):
        self.pos = Vector2(x, y)
        self.vel = Vector2(0.0, 0.0)
        self.angle = 0.0  # Degrees, 0 is flat, positive is up
        self.thrust_power = 0.0 # 0.0 to 1.0
        
        # Physics Constants
        self.GRAVITY = 0.15
        self.LIFT_FACTOR = 0.02
        self.MAX_SPEED = 15.0
        self.MIN_SPEED = 3.0
        self.ROTATION_SPEED = 2.0

    def update(self):
        # Apply Gravity
        self.vel.y += self.GRAVITY

        # Apply Thrust (Vector based on angle)
        # Convert angle to radians for math
        rad = np.radians(self.angle)
        thrust_x = np.cos(rad) * self.thrust_power * 0.5
        thrust_y = -np.sin(rad) * self.thrust_power * 0.5
        
        self.vel.x += thrust_x
        self.vel.y += thrust_y

        # Apply Drag (Air resistance)
        self.vel.x *= 0.98
        self.vel.y *= 0.98

        # Apply Lift (Faster you go x, more you float up)
        # Lift acts perpendicular to velocity, but for simplicity, we just counter gravity
        lift = self.vel.x * self.LIFT_FACTOR
        self.vel.y -= lift

        # Limit Speed
        speed = np.sqrt(self.vel.x**2 + self.vel.y**2)
        if speed > self.MAX_SPEED:
            factor = self.MAX_SPEED / speed
            self.vel.x *= factor
            self.vel.y *= factor
            
        # Update Position
        # We don't update X position in world space because the world scrolls.
        # But we do update Y (height).
        self.pos.y += self.vel.y

    def rotate(self, direction: int):
        """ -1 for up (nose up), 1 for down (nose down) """
        self.angle += direction * self.ROTATION_SPEED
        # Clamp angle
        self.angle = max(-60, min(60, self.angle))

    def set_thrust(self, power: float):
        self.thrust_power = max(0.0, min(1.0, power))

class Terrain:
    def __init__(self, width: int, height: int):
        self.width = width
        self.base_height = height
        self.chunk_size = 100
        self.scroll_offset = 0.0
        self.points = []
        self._generate_initial()

    def _generate_initial(self):
        # Generate initial terrain points
        for x in range(0, self.width + self.chunk_size, 10):
            self.points.append(self._noise(x))

    def _noise(self, x: float) -> float:
        # Simple composition of sine waves for mountains
        # Low frequency (Big mountains)
        y = np.sin(x * 0.005) * 150 
        # High frequency (Roughness)
        y += np.sin(x * 0.02) * 50
        # Offset to bottom of screen
        return self.base_height - 100 + y

    def update(self, speed: float):
        self.scroll_offset += speed
        
        # Remove points that are off screen left
        # We shift the "logical" x coordinate.
        # In a real implementation we'd probably use a fixed array and shift values,
        # but recalculating based on absolute X is smoother for noise functions.
        pass 
        
    def get_height_at(self, screen_x: int) -> float:
        # Map screen_x + scroll_offset to world x
        world_x = screen_x + self.scroll_offset
        return self._noise(world_x)
