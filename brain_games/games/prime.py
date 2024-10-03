import random


def is_prime(number):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def generate_question_and_answer():
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = "yes" if is_prime(number) else "no"

    return question, correct_answer
