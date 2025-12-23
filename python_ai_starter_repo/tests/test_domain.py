import pytest
from src.myproject.domain.models import Grid, GemType, Gem

def test_grid_initialization():
    grid = Grid()
    assert len(grid.cells) == 8
    assert len(grid.cells[0]) == 8
    # Ensure no initial matches
    assert len(grid.find_matches()) == 0

def test_swap_gems():
    grid = Grid()
    # Force specific setup for testing
    gem1 = Gem(GemType.RED)
    gem2 = Gem(GemType.BLUE)
    grid.cells[0][0] = gem1
    grid.cells[0][1] = gem2
    
    grid.swap_gems(0, 0, 1, 0)
    
    assert grid.cells[0][0] == gem2
    assert grid.cells[0][1] == gem1

def test_find_horizontal_matches():
    grid = Grid()
    # Create a match
    grid.cells[0][0] = Gem(GemType.RED)
    grid.cells[0][1] = Gem(GemType.RED)
    grid.cells[0][2] = Gem(GemType.RED)
    
    matches = grid.find_matches()
    assert (0, 0) in matches
    assert (1, 0) in matches
    assert (2, 0) in matches
    assert len(matches) >= 3

def test_gravity():
    grid = Grid()
    # Clear a column
    for y in range(8):
        grid.cells[y][0] = None
    
    # Place one gem at top
    target_gem = Gem(GemType.RED)
    grid.cells[0][0] = target_gem
    
    grid.apply_gravity()
    
    # Gem should fall to bottom
    assert grid.cells[7][0] == target_gem
    assert grid.cells[0][0] is None
