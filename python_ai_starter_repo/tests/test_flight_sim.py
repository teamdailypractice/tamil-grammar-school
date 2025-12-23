import pytest
import numpy as np
from src.flight_sim.domain.models import Jet, Terrain

def test_jet_initialization():
    jet = Jet(100, 200)
    assert jet.pos.x == 100
    assert jet.pos.y == 200
    assert jet.vel.x == 0
    assert jet.vel.y == 0
    assert jet.angle == 0

def test_jet_gravity():
    jet = Jet(100, 200)
    jet.update()
    # Gravity should increase Y velocity (downwards)
    assert jet.vel.y > 0
    assert jet.pos.y > 200

def test_jet_thrust():
    jet = Jet(100, 200)
    jet.set_thrust(1.0)
    jet.update()
    # Thrust should increase X velocity
    assert jet.vel.x > 0

def test_jet_lift():
    jet = Jet(100, 200)
    # Give it high speed
    jet.vel.x = 10.0
    jet.vel.y = 0.0
    
    # Update
    jet.update()
    
    # Gravity (0.15) pulls down, Lift (10 * 0.02 = 0.2) pulls up.
    # Net acceleration should be negative (upwards) or at least less than gravity alone.
    # Initial vy=0 -> +Gravity -Lift = 0.15 - 0.2 = -0.05
    assert jet.vel.y < 0 

def test_terrain_generation():
    terrain = Terrain(800, 600)
    height = terrain.get_height_at(100)
    # Check bounds (base height 600, minus [50, 450])
    # Expected range roughly [150, 550].
    assert 100 < height < 650

def test_terrain_scrolling():
    terrain = Terrain(800, 600)
    h1 = terrain.get_height_at(100)
    
    # Scroll forward by 100 units
    terrain.update(100)
    
    # Now get_height_at(0) should be what get_height_at(100) was (conceptually), 
    # but the implementation uses world_x = screen_x + scroll_offset.
    # Before: world_x = 100 + 0 = 100.
    # After: world_x = 0 + 100 = 100.
    h2 = terrain.get_height_at(0)
    
    assert abs(h1 - h2) < 0.001
