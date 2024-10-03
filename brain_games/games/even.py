import random


def is_even(number: int) -> bool:
    print('Answer "yes" if the number is even, otherwise answer "no".')
    return number % 2 == 0


def generate_question_and_answer() -> tuple[str, str]:
    number: int = random.randint(1, 100)
    question: str = str(number)
    correct_answer: str = "yes" if is_even(number) else "no"

    return question, correct_answer
