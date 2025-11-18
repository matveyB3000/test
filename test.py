from domain.quiz import Quiz
from domain.question import Question, Answer
from services.quiz_loader import Loader
quiz = Quiz(
    "математика",
    [
        Question(
            "сколько будет корень из 81",
            [
                Answer("9", True),
                Answer("6")
            ],
        ),
        Question("2+2?",[
            Answer("5"),
            Answer("4",True)
        ])
    ],
)
loader = Loader()
loader.save("math.json",quiz)
data = loader.load("math.json")
assert data == quiz
