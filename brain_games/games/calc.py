import random

OPERATIONS = ['+', '-', '*']


def generate_question_and_answer():
    print('What is the result of the expression?')
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operation = random.choice(OPERATIONS)

    if operation == '+':
        correct_answer = num1 + num2
    elif operation == '-':
        correct_answer = num1 - num2
    elif operation == '*':
        correct_answer = num1 * num2

    question = f"Question: {num1} {operation} {num2}"

    return question, str(correct_answer)
