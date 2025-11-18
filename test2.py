from dataclasses import asdict
from typing import Tuple
from domain.quiz import Quiz
from domain.question import Question, Answer
from blinker import Signal
import json
from random import shuffle 
from services.quiz_loader import Loader
from services.quiz_session import Session

loader = Loader()
quiz = loader.load("math.json")

session = Session()
session.start(quiz)
answers = ["3 в степени 2","9","перебираю а так не знаю"]
print(session._check(answers))