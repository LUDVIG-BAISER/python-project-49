import random
import math


def is_prime(number) -> bool:
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    if number < 2:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True


def generate_question_and_answer() -> tuple[str, str]:
    number: int = random.randint(1, 100)
    question: str = str(number)
    correct_answer: str = "yes" if is_prime(number) else "no"

    return question, correct_answer
