MAX_ROUNDS = 3


def play_game(game):
    print("Welcome to the Brain Games!")
    name = input("May I have your name? ")
    print(f"Hello, {name}!")

    for _ in range(MAX_ROUNDS):
        question, correct_answer = game.generate_question_and_answer()
        print(f"Question: {question}")
        user_answer = input("Your answer: ")

        if user_answer == correct_answer:
            print("Correct!")
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was "
                  f"'{correct_answer}'.")

            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
