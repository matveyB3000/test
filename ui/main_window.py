from typing import Tuple
from  PyQt5.QtWidgets import QWidget ,QHBoxLayout , QVBoxLayout
from  PyQt5.QtCore import Qt
from .quiz_view import QuizView
from .result_view import ResultView
from events.global_event import on_restart , on_end
import style

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("тест")
        self.resize(800,800)
        self.layout_main = QVBoxLayout()
        self.setLayout(self.layout_main)
        self.quiz_view = QuizView()
        self.layout_main.addWidget(self.quiz_view)
        self.result_view = ResultView()
        self.layout_main.addWidget(self.result_view)
        on_restart.connect(self.on_start)
        on_end.connect(self.on_end)
        self.on_start()
        self.setStyleSheet(style.MAIN_STYLE)

    def on_start(self,*args,**kwargs):
        self.result_view.hide()
        self.quiz_view.show()

    def on_end(self,*args,**kwargs):
        self.result_view.show()
        self.quiz_view.hide()
        