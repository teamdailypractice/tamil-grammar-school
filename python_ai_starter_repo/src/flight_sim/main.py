import sys
import os

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..")))

from src.flight_sim.services.game_engine import FlightSimEngine

def main():
    game = FlightSimEngine()
    game.run()

if __name__ == "__main__":
    main()
