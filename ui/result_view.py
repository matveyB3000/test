from PyQt5.QtWidgets import QWidget , QLabel, QCheckBox , QPushButton , QGridLayout ,QVBoxLayout
from PyQt5.QtCore import Qt
from typing import Tuple , List
from events.global_event import on_end,on_restart

class ResultView(QWidget):
    def __init__(self):
        super().__init__()
        self.label_result = QLabel(f"вы прошли тест")
        self.layout_main = QVBoxLayout()
        self.button_restart = QPushButton("перепройти")
        self.setLayout(self.layout_main)
        self.layout_main.addWidget(self.label_result,alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout_main.addWidget(self.button_restart)
        on_end.connect(self.set_results)
        self.button_restart.clicked.connect(self._on_restart)


    def set_results(self,s,score:int,amount_questions:int):
        self.label_result.setText(f"вы прошли тест на {score} из {amount_questions}")

    def _on_restart(self):
        on_restart.send("RESULT_VIEW")