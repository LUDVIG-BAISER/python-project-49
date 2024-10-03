import random
import math


def generate_question_and_answer() -> [str, str]:
    print('Find the greatest common divisor of given numbers.')
    num1: int = random.randint(1, 20)
    num2: int = random.randint(1, 20)

    question: str = f"{num1} {num2}"
    correct_answer = math.gcd(num1, num2)

    return question, str(correct_answer)
