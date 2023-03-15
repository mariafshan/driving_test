import json
import random

data = json.load(open("questions.json"))
NUM_OF_QUESTIONS = len(data["questions"])

def random_questions_array(max=NUM_OF_QUESTIONS):
    """
    Create an array of random question numbers.
    max: maximum number of questions (default = the number of questions in the json file)
    """
    random_array = []

    for i in range(max):
        random_num = random.randint(0, NUM_OF_QUESTIONS - 1)
        while random_num in random_array:
            random_num = random.randint(0, NUM_OF_QUESTIONS - 1)

        random_array.append(random_num)

    return random_array