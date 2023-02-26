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
            print(str(i+1) + ") " + self.answers[i])
        self.user_answer = input("Please enter the number of your answer: ")

    def check_answer(self):
        if int(self.user_answer) == self.correct_answer:
            self.points += 1
            print("Correct! You have earned 1 point.")
        else:
            print("Incorrect. The correct answer was " + str(self.correct_answer) + ".")

    def remove_wrong_answer(self):
        for i in range(len(self.answers)):
            if i + 1 != self.correct_answer:
                self.answers[i] = ''
                break
        self.hint_used = True

def start_quiz():
    q1 = Quiz("What is the capital of France?", ["Paris", "London", "Berlin"], 1)
    q2 = Quiz("What is the capital of Germany?", ["Paris", "Berlin", "Madrid"], 2)
    q3 = Quiz("What is the capital of Spain?", ["Rome", "Madrid", "Paris"], 2)
    questions = [q1, q2, q3]
    print("Welcome to the quiz! You have 5 seconds to answer each question. Good luck!")
    start_time = datetime.now()
    hint_used = False
    for q in questions:
        q.ask_question()
        if (datetime.now() - start_time).total_seconds() > 20:
            print("Time's up! No points awarded.")
            break
        if not hint_used:
            print("Enter 'h' for a hint.")
        while True:
            answer = q.user_answer.lower()
            if answer == 'h' and not q.hint_used:
                q.remove_wrong_answer()
                hint_used = True
                print("One wrong answer has been removed.")
                q.ask_question()
            elif answer.isdigit():
                q.check_answer()
                break
            else:
                print("Invalid input. Please enter a number or 'h' for a hint.")
    print("You have finished the quiz! You have earned " + str(q1.points + q2.points + q3.points) + " points.")

start_quiz()