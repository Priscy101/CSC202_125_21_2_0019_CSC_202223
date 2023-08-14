#Creating a class in python
class User:

    def __init__(self, user_id, username):
        self.id  = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1
    
user_1 = User("001", "angela")
user_2 = User("002", "Jack")

print(user_1.followers)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

#Quiz Game
#Creating the Question class
class Question:

    def __init__(self, q_text, q_answer):
       self.text = q_text
       self.answer = q_answer
if Day17 == Question:
Data == question_data
from Quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You have completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

