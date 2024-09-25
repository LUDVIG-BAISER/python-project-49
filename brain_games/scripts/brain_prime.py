from brain_games.game_engine.base import play_game
from brain_games.games import prime

def main():
    print('"yes" if given number is prime. Otherwise answer "no"')
    play_game(prime)

if __name__ == "__main__":
    main()