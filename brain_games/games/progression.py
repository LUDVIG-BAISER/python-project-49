import random


def generate_question_and_answer():
    start = random.randint(1, 10)
    step = random.randint(1, 5)
    length = 10
    progression = [start + i * step for i in range(length)]

    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]

    progression[hidden_index] = ".."

    question = " ".join(map(str, progression))

    return question, str(correct_answer)
