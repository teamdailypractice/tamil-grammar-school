import pytest
import pygame
from unittest.mock import MagicMock
from src.myproject.infrastructure.graphics import GameRenderer
from src.myproject.domain.models import Gem, GemType

def test_draw_gem_shapes():
    # Setup
    pygame.init()
    # Use a real surface instead of a mock so pygame.draw functions accept it
    mock_screen = pygame.Surface((800, 600))
    mock_font = MagicMock()
    
    # Mock font.render to return a surface
    mock_font.render.return_value = pygame.Surface((100, 20))
    
    renderer = GameRenderer(mock_screen, mock_font)
    
    # Test drawing each gem type to ensure no syntax errors in shape logic
    for gem_type in GemType:
        gem = Gem(gem_type)
        try:
            renderer._draw_gem(gem, 0, 0, selected=False)
            renderer._draw_gem(gem, 0, 0, selected=True)
        except Exception as e:
            pytest.fail(f"Drawing {gem_type} failed: {e}")

def test_get_grid_coords():
    # Setup
    mock_screen = MagicMock()
    mock_font = MagicMock()
    mock_screen.get_width.return_value = 800
    mock_screen.get_height.return_value = 600
    
    renderer = GameRenderer(mock_screen, mock_font)
    
    # Calculate expected offset
    # WIDTH=8, HEIGHT=8, CELL_SIZE=64 -> Grid is 512x512
    # Offset X = (800 - 512) // 2 = 144
    # Offset Y = (600 - 512) // 2 = 44
    
    # Test valid click
    # Click at 150, 50 -> (150-144)//64 = 0, (50-44)//64 = 0 -> (0,0)
    assert renderer.get_grid_coords((150, 50)) == (0, 0)
    
    # Test invalid click (outside margin)
    assert renderer.get_grid_coords((0, 0)) is None
