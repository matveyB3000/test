from PyQt5.QtWidgets import QWidget , QLabel, QCheckBox , QPushButton , QGridLayout ,QVBoxLayout
from PyQt5.QtCore import Qt
from typing import Tuple , List
from events.global_event import on_answer , on_change_question
from random import shuffle

class QuizView(QWidget):
    def __init__(self):
        super().__init__()
        self.amount_columns = 2
        self.buttons_list:List[QCheckBox] = []
        self._create_ui()
        self.set_answers(("правильно","неправильно","точно не правильно","может правильно но это не точно"))
        self.button_answer.clicked.connect(self._on_click)
        on_change_question.connect(self.on_change_question)

    def _create_ui(self):
        self.label_question = QLabel(text="тут будет вопрос")
        self.button_answer = QPushButton(text ="ответить")
        self.grid_layout = QGridLayout()
        self.layout_main = QVBoxLayout()
        self.setLayout(self.layout_main)
        self.layout_main.addWidget(self.label_question,alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout_main.addLayout(self.grid_layout)
        self.layout_main.addWidget(self.button_answer)

        
    def set_answers(self,answers:Tuple[str]):
        self._clear_answers()
        for i,t in enumerate(answers):
            row = i//self.amount_columns
            col = i%self.amount_columns
            checkbox_answer = QCheckBox(text=t)
            self.buttons_list.append(checkbox_answer)
            self.grid_layout.addWidget(checkbox_answer,row , col , Qt.AlignmentFlag.AlignCenter)

    def _clear_answers(self):
        for i in self.buttons_list:
            self.grid_layout.removeWidget(i)
        self.buttons_list.clear()
    
    def set_question(self,question:str):
        self.label_question.setText(question)

    def _on_click(self):
        on_answer.send("ANY",answers=  self._get_answers())
    
    def _get_answers(self)->List[str]:
        return [i.text() for i in self.buttons_list if i.isChecked()]

    def on_change_question(self,sender,question,answers):
        self.set_question(question)
        shuffle(answers)
        self.set_answers(answers)