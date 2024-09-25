from brain_games.game_engine.base import play_game
from brain_games.games import even

def main():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    play_game(even)

if __name__ == "__main__":
    main()
