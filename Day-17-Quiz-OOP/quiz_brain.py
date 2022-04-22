class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, current_answer):

        if user_answer.lower() == current_answer.lower():
            self.score += 1
            print("You were right!")
        else:
            print("You were wrong!")
        print(f"{self.score}/{self.question_number}")

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f"Q.{self.question_number}: {current_question.text} (True/False)?:")
        self.check_answer(user_answer, current_question.answer)
