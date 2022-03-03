from question import Question
from quiz_brain import QuizBrain
from data import quiz_data

question_bank = [Question(quiz_data['results'][question]['question'], quiz_data['results'][question]['correct_answer'])
                 for question in range(len(quiz_data['results']))]

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print('You\'ve completed the quiz.')
print(f'Final Score: {quiz.score}/{quiz.question_number}')