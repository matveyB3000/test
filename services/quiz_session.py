from dataclasses import asdict
from typing import Tuple
from domain.quiz import Quiz
from domain.question import Question, Answer
from blinker import Signal
from events.global_event import on_change_question ,on_answer , on_end,on_restart
import json
from random import shuffle 
from .quiz_loader import Loader

class Session():
    score:int = 0
    current_question_id:int = 0 
    quiz:Quiz = None
    is_end:bool = False
    
    def __init__(self):
        on_answer.connect(self.answer)
        on_restart.connect(self.restart)

    def start(self,quiz:Quiz):
        self.quiz = quiz 
        self.restart()
    
    def restart(self,*args,**kwargs):
        self.score = 0
        self.current_question_id = 0
        shuffle(self.quiz.questions)
        self.is_end = False
        on_change_question.send("SESSION",
                                question = self.question.text,
                                answers =  [i.text for i in self.question.answers])

    def _check(self,answers:Tuple[str]):
        #correct_answers = []
        # for i in self.question.answers:
        #     if i.is_correct :
        #         correct_answers.append(i)
        
        # correct_answers = filter(check,answers)
        correct_answers = list(filter(lambda a: a.is_correct ,self.question.answers))
        correct_answers = [i.text for i in correct_answers]
        correct_answers.sort()
        if len(correct_answers) != len(answers):
            return False
        answers.sort()
        for i,e in  enumerate(correct_answers):
            if answers[i] != e:
                return False 
        return True 

    def answer(self,sender:str,answers:Tuple[str]):
        if answers.__len__() == 0:
            return
        if self._check(answers):
            self.score+=1
        if self.current_question_id < len(self.quiz.questions)-1:
            self.current_question_id+=1
            on_change_question.send("SESSION",
                                question = self.question.text,
                                answers =  [i.text for i in self.question.answers])
        else :
            on_end.send("SESSION",
                        score = self.score,
                        amount_questions = self.quiz.questions.__len__())
        print("что то")
            

    @property
    def question(self)->Question:
        return self.quiz.questions[self.current_question_id]

