from brain_games.game_engine.base import play_game
from brain_games.games import progression

def main():
    print('What number is missing in the progression?')
    play_game(progression)

if __name__ == "__main__":
    main()