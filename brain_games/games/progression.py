import random


def generate_question_and_answer() -> tuple[str, str]:
    print('What number is missing in the progression?')
    start: int = random.randint(1, 10)
    step: int = random.randint(1, 5)
    length: int = 10
    progression: list[int] = [start + i * step for i in range(length)]

    hidden_index: int = random.randint(0, length - 1)

    progression[hidden_index], correct_answer = "..", progression[hidden_index]

    question: str = " ".join(map(str, progression))

    return question, str(correct_answer)
