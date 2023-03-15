import json
from random_questions import random_questions_array

FILE = "questions.json"

def load_data():
    return json.load(open(FILE))

def generate_questions(questions, answers, random_array, num_practice_questions):
    score = 0
    n_completed_questions = 0  # number of questions completed
    wrong_questions = []

    for i in random_array:
        n_completed_questions += 1
        print("Question", str(n_completed_questions), "out of", num_practice_questions)
        print(questions[i])

        user_answer = str(input("Answer: ")).lower()

        if user_answer == answers[i].lower():
            score += 1
            print("Correct!\n")

        else:
            wrong_questions.append([questions[i], user_answer, answers[i]])
            print("Incorrect. The correct answer is", str(answers[i]) + "\n")

    return wrong_questions, score

def main():
    max_questions = int(input("Max number of questions: "))

    data = load_data()
    questions = data["questions"]
    answers = data["answers"]

    global NUM_OF_QUESTIONS
    NUM_OF_QUESTIONS = len(questions)

    if max_questions > NUM_OF_QUESTIONS:
        random_array = random_questions_array()
    else:
        random_array = random_questions_array(max = max_questions)

    num_practice_questions = len(random_array)

    wrong_questions, score = generate_questions(questions, answers, random_array, num_practice_questions)

    # calculate the percentage of correct answers
    score_per = round((score / num_practice_questions) * 100, 2)

    print("You got", score, "questions out of", num_practice_questions, "questions correct.")
    print("You answered", str(score_per) + "% correctly.\n")
    if score_per >= 80:
        print("You are ready to take the written driving test!")
    else:
        print("You score less than 80%, try to study the materials again before taking the test.")

    if len(wrong_questions) == 0:
        print("\nCongratulations for acing the practice test. But don't stop here, continue studying the guide book!")
    else:
        print("\nReview the following questions:")
        for ele in wrong_questions:
            print("\nQuestion:", ele[0])
            print("Your answer:", ele[1])
            print("Answer:", ele[2])

if __name__ == '__main__':
    main()
