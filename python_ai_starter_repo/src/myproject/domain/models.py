import random
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import List, Optional, Set, Tuple


class GemType(Enum):
    RED = auto()
    GREEN = auto()
    BLUE = auto()
    YELLOW = auto()
    PURPLE = auto()
    ORANGE = auto()


@dataclass
class Gem:
    type: GemType
    # You might add unique IDs or special properties here later


class Grid:
    WIDTH = 8
    HEIGHT = 8

    def __init__(self):
        self.cells: List[List[Optional[Gem]]] = [
            [None for _ in range(self.WIDTH)] for _ in range(self.HEIGHT)
        ]
        self._initialize_grid()

    def _initialize_grid(self) -> None:
        """Fill the grid ensuring no initial matches exist."""
        for y in range(self.HEIGHT):
            for x in range(self.WIDTH):
                while True:
                    gem_type = random.choice(list(GemType))
                    # Prevent initial match-3
                    if (
                        x >= 2
                        and self.cells[y][x - 1]
                        and self.cells[y][x - 2]
                        and self.cells[y][x - 1].type == gem_type  # type: ignore
                        and self.cells[y][x - 2].type == gem_type  # type: ignore
                    ):
                        continue
                    if (
                        y >= 2
                        and self.cells[y - 1][x]
                        and self.cells[y - 2][x]
                        and self.cells[y - 1][x].type == gem_type  # type: ignore
                        and self.cells[y - 2][x].type == gem_type  # type: ignore
                    ):
                        continue
                    
                    self.cells[y][x] = Gem(type=gem_type)
                    break

    def get_gem(self, x: int, y: int) -> Optional[Gem]:
        if 0 <= x < self.WIDTH and 0 <= y < self.HEIGHT:
            return self.cells[y][x]
        return None

    def swap_gems(self, x1: int, y1: int, x2: int, y2: int) -> None:
        """Swap two gems (does not check validity, just swaps)."""
        if (
            0 <= x1 < self.WIDTH
            and 0 <= y1 < self.HEIGHT
            and 0 <= x2 < self.WIDTH
            and 0 <= y2 < self.HEIGHT
        ):
            self.cells[y1][x1], self.cells[y2][x2] = (
                self.cells[y2][x2],
                self.cells[y1][x1],
            )

    def find_matches(self) -> Set[Tuple[int, int]]:
        """Return a set of (x, y) coordinates that are part of a match."""
        matched: Set[Tuple[int, int]] = set()

        # Horizontal matches
        for y in range(self.HEIGHT):
            for x in range(self.WIDTH - 2):
                gem = self.cells[y][x]
                if gem and self.cells[y][x + 1] and self.cells[y][x + 2]:
                    if (
                        gem.type == self.cells[y][x + 1].type  # type: ignore
                        and gem.type == self.cells[y][x + 2].type  # type: ignore
                    ):
                        matched.add((x, y))
                        matched.add((x + 1, y))
                        matched.add((x + 2, y))

        # Vertical matches
        for x in range(self.WIDTH):
            for y in range(self.HEIGHT - 2):
                gem = self.cells[y][x]
                if gem and self.cells[y + 1][x] and self.cells[y + 2][x]:
                    if (
                        gem.type == self.cells[y + 1][x].type  # type: ignore
                        and gem.type == self.cells[y + 2][x].type  # type: ignore
                    ):
                        matched.add((x, y))
                        matched.add((x, y + 1))
                        matched.add((x, y + 2))

        return matched

    def remove_gems(self, coords: Set[Tuple[int, int]]) -> None:
        """Set specified coordinates to None."""
        for x, y in coords:
            self.cells[y][x] = None

    def apply_gravity(self) -> bool:
        """Drop gems down to fill empty spaces. Return True if changes happened."""
        moved = False
        for x in range(self.WIDTH):
            # Process each column
            write_idx = self.HEIGHT - 1
            for read_idx in range(self.HEIGHT - 1, -1, -1):
                if self.cells[read_idx][x] is not None:
                    if write_idx != read_idx:
                        self.cells[write_idx][x] = self.cells[read_idx][x]
                        self.cells[read_idx][x] = None
                        moved = True
                    write_idx -= 1
        return moved

    def fill_empty(self) -> bool:
        """Fill empty cells with new random gems. Return True if gems were added."""
        filled = False
        for y in range(self.HEIGHT):
            for x in range(self.WIDTH):
                if self.cells[y][x] is None:
                    self.cells[y][x] = Gem(type=random.choice(list(GemType)))
                    filled = True
        return filled
