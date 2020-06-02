import random


def this_or_that(text: str) -> str:
    random.seed()
    text = text.split(',')
    return text[random.randint(0, len(text)-1)].strip()
