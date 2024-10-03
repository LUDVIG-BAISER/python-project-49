import random
from typing import Tuple

OPERATIONS = ['+', '-', '*']


def generate_question_and_answer() -> Tuple[str, str]:
    print('What is the result of the expression?')
    num1: int = random.randint(1, 20)
    num2: int = random.randint(1, 20)
    operation: str = random.choice(OPERATIONS)

    if operation == '+':
        correct_answer: int = num1 + num2
    elif operation == '-':
        correct_answer: int = num1 - num2
    elif operation == '*':
        correct_answer: int = num1 * num2

    question = f"Question: {num1} {operation} {num2}"

    return question, str(correct_answer)
