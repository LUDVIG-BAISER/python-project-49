

from brain_games.game_engine.base import play_game
from brain_games.games import calc

def main():
    print('What is the result of the expression?')
    play_game(calc)

if __name__ == "__main__":
    main()
