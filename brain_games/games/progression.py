import random


def generate_question_and_answer():
    print('What number is missing in the progression?')
    start = random.randint(1, 10)
    step = random.randint(1, 5)
    length = 10
    progression = [start + i * step for i in range(length)]

    hidden_index = random.randint(0, length - 1)

    progression[hidden_index], correct_answer = "..", progression[hidden_index]

    question = " ".join(map(str, progression))

    return question, str(correct_answer)
