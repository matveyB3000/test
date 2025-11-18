from dataclasses import asdict
from domain.quiz import Quiz
from domain.question import Question, Answer

import json


class Loader():
    def __init__(self):
        pass

    def load(self, test_path: str) -> Quiz:
        with open(test_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            questions = [Question(q['text'], [Answer(a['text'], a['is_correct']) for a in q['answers']]) for q in data['questions']]
            return Quiz(data['title'], questions)

    def save(self, path: str, quiz: Quiz):
        with open(path, "w", encoding="utf-8") as file:
            json.dump(asdict(quiz), file, ensure_ascii=False, indent=4)


