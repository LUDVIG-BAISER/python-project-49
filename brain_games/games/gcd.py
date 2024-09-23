import random
import math


def generate_question_and_answer():

    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)

    question = f"{num1} {num2}"
    correct_answer = math.gcd(num1, num2)

    return question, str(correct_answer)
