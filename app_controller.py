from dataclasses import asdict
from typing import Tuple
from domain.quiz import Quiz
from domain.question import Question, Answer
from blinker import Signal
import json
from random import shuffle 
from services.quiz_loader import Loader
from services.quiz_session import Session
from ui.main_window import MainWindow
from PyQt5.QtWidgets import QApplication
from events.global_event import on_answer

def start():
    app = QApplication([])
    loader = Loader()
    session = Session()
    window = MainWindow()
    
    window.show()
    quiz = loader.load("math.json")
    session.start(quiz)

    app.exec_()
    