from brain_games.game_engine.base import play_game
from brain_games.games import gcd

def main():
    print('Find the greatest common divisor of given numbers')
    play_game(gcd)

if __name__ == "__main__":
    main()