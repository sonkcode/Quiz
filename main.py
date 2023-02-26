import time
from datetime import datetime


class Quiz:
    def __init__(self, question, answers, correct_answer):
        self.question = question
        self.answers = answers
        self.correct_answer = correct_answer
        self.user_answer = None
        self.points = 0
        self.hint_used = False

    def ask_question(self):
        print(self.question)
        for i in range(len(self.answers)):
            print(str(i + 1) + ") " + self.answers[i])
        while True:
            try:
                self.user_answer = int(input("Please enter the number of your answer: "))
                if self.user_answer < 1 or self.user_answer > len(self.answers):
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter a number between 1 and " + str(
                    len(self.answers)) + " or 'h' for a hint.")

    def check_answer(self):
        if int(self.user_answer) == self.correct_answer:
            self.points += 1
            print("Correct! You have earned 1 point.")
        else:
            print("Incorrect. The correct answer was " + str(self.correct_answer) + ".")

    def remove_wrong_answer(self):
        removed_answers = 0
        for i in range(len(self.answers)):
            if i + 1 != self.correct_answer and removed_answers < 1:
                self.answers[i] = ''
                removed_answers += 1
        self.answers = list(filter(None, self.answers))
        self.hint_used = True


def start_quiz():
    q1 = Quiz("What is the capital of France?", ["Paris", "London", "Berlin"], 1)
    q2 = Quiz("What is the capital of Germany?", ["Paris", "Berlin", "Madrid"], 2)
    q3 = Quiz("What is the capital of Spain?", ["Rome", "Madrid", "Paris"], 2)
    questions = [q1, q2, q3]
    print("Welcome to the quiz! You have 20 seconds to answer each question. Good luck!")
    hint_used = False
    for q in questions:
        start_time = time.time()
        q.ask_question()
        while True:
            time_left = int(20 - (time.time() - start_time))
            if time_left <= 0:
                print("Time's up! No points awarded.")
                break
            print("Time left: {} seconds".format(time_left))
            if not hint_used:
                print("Enter 'h' for a hint.")
            if isinstance(q.user_answer, int):
                answer = str(q.user_answer)
            else:
                answer = q.user_answer.lower()
            if answer == 'hint' and not q.hint_used:
                q.remove_wrong_answer()
                hint_used = True
                print("One wrong answer has been removed.")
                q.ask_question()
            elif answer.isdigit():
                q.check_answer()
                break
            else:
                print("Invalid input. Please enter a number or 'hint' for a hint.")
        if time_left <= 0:
            continue
    print("You have finished the quiz! You have earned " + str(q1.points + q2.points + q3.points) + " points.")


start_quiz()