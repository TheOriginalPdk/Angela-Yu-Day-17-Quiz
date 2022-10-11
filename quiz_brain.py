class Quizbrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.user_score =0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)
        #the above^ is the same as below
        # if self.question_number < len(self.question_list):
        #     return True
        # else:
        #     False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        # print(current_question.text)
        self.question_number += 1
        correct_answer = current_question.answer
        user_answer = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.checkanswer(user_answer,correct_answer)

    def check_answer(self, user_answer,correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right")
            self.user_score +=1
        else:
            print("That's wrong!")
        print(f"The correct answer was:  {correct_answer}")
        print(f"Your score is: {self.user_score}/{self.question_number}")
        print("\n")

